import os
import numpy as np
from ultralytics import YOLO
from sklearn.metrics.pairwise import cosine_similarity

# モデル読み込み (YOLOv8 Nano Classification)
model = YOLO('yolov8n-cls.pt')

def get_yolo_embedding(img_path):
    """画像から特徴ベクトルを抽出"""
    try:
        # 特徴量抽出 (Tensor取得)
        results = model.predict(
            source=img_path, 
            embed=[len(model.model.model) - 2], 
            verbose=False
        )
        return results[0].cpu().numpy().flatten()
    except Exception as e:
        print(f"Error processing {img_path}: {e}")
        return None

def get_base_name(filename):
    """拡張子を除いたファイル名を取得 (例: image.jpg -> image)"""
    return os.path.splitext(filename)[0]

def main():
    query_dir = "photo"        # テストしたい画像
    database_dir = "photouse30" # データベース画像
    
    # 判定閾値 (これ以上なら「含まれている」とAIが判定)
    THRESHOLD = 0.95

    # 1. データベース(photouse30)の特徴量とファイル名リストを作成
    db_features = []
    db_names = []      # 表示用(拡張子あり)
    db_base_names = set() # 正解判定用(拡張子なし・検索高速化のためsetを使用)
    
    print(f"[{database_dir}] を読み込み中...")
    if not os.path.exists(database_dir):
        print(f"エラー: {database_dir} が見つかりません")
        return

    for img_name in os.listdir(database_dir):
        if not img_name.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.webp')):
            continue
        
        img_path = os.path.join(database_dir, img_name)
        feat = get_yolo_embedding(img_path)
        if feat is not None:
            db_features.append(feat)
            db_names.append(img_name)
            db_base_names.add(get_base_name(img_name))

    if not db_features:
        print("データベースに画像がありません。")
        return

    # 2. 判定ループ
    print(f"\n[{query_dir}] の画像を判定開始...\n")
    
    total_count = 0
    correct_count = 0
    
    # 詳細ログ用カウンター
    tp = 0 # True Positive (あると予測して、本当にあった)
    tn = 0 # True Negative (ないと予測して、本当になかった)
    fp = 0 # False Positive (あると予測したが、本当はなかった)
    fn = 0 # False Negative (ないと予測したが、本当はあった)

    if not os.path.exists(query_dir):
        print(f"エラー: {query_dir} が見つかりません")
        return

    for query_name in os.listdir(query_dir):
        if not query_name.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.webp')):
            continue

        total_count += 1
        query_path = os.path.join(query_dir, query_name)
        query_feat = get_yolo_embedding(query_path)
        
        if query_feat is None:
            continue
            
        # --- A. AIによる予測 ---
        similarities = cosine_similarity([query_feat], db_features)[0]
        max_idx = np.argmax(similarities)
        max_score = similarities[max_idx]
        
        # AIの答え: 閾値を超えていれば True(含まれている)、そうでなければ False
        ai_prediction = max_score >= THRESHOLD
        
        # --- B. 本当の正解 (Ground Truth) ---
        # ファイル名(拡張子なし)がDB内に存在するかチェック
        actual_truth = get_base_name(query_name) in db_base_names
        
        # --- C. 答え合わせ ---
        is_correct = (ai_prediction == actual_truth)
        
        if is_correct:
            correct_count += 1
            result_str = " 正解"
            if ai_prediction: tp += 1
            else: tn += 1
        else:
            result_str = " 不正解"
            if ai_prediction: fp += 1 # 誤検出
            else: fn += 1 # 見逃し

        # 状況に応じたメッセージ作成
        match_info = f"(AIスコア: {max_score:.4f})"
        if ai_prediction:
            match_info += f" -> {db_names[max_idx]} と一致判定"
        else:
            match_info += " -> 一致なし判定"

        truth_info = "【実は含まれている】" if actual_truth else "【実は含まれていない】"

        print(f"{result_str} | {query_name}")
        print(f"   └ {match_info} / {truth_info}")

    # 3. 最終結果の表示
    if total_count > 0:
        accuracy = (correct_count / total_count) * 100
        print("\n" + "="*40)
        print(f" 最終結果レポート")
        print("="*40)
        print(f" 画像総数 : {total_count} 枚")
        print(f" 正解数   : {correct_count} 枚")
        print(f" 正解率   : {accuracy:.2f}%")
        print("-" * 40)
        print(f" [内訳]")
        print(f" ・正しく検知 (TP): {tp}枚")
        print(f" ・正しく除外 (TN): {tn}枚")
        print(f" ・誤検知 (FP)    : {fp}枚 (ないのに「ある」と言った)")
        print(f" ・見逃し (FN)    : {fn}枚 (あるのに「ない」と言った)")
        print("="*40)
    else:
        print("画像が見つかりませんでした。")

if __name__ == "__main__":
    main()