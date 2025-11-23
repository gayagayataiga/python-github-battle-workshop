
# Pythonサークル GitHub体験会 ＋ ミニモデル対決

このリポジトリは、Pythonサークルで行う **GitHub 基本操作体験会** と  
**GAN風ミニ対決（モデルバトル）** のための教材です。

参加者は、ブランチを作成してモデルを作り、Pull Request で提出します。

---

## 🚀 ワークショップ概要

- GitHub の基本操作（clone / branch / commit / push / PR）を学ぶ
- Python で簡単なモデルを作成し、評価スコアを競うミニ対決を実施
- 参加者はそれぞれのブランチで独自モデルを作成し、PR で提出

---

## 🗓 当日の流れ

1. リポジトリの説明（5分）
2. GitHub 基本操作の解説（10分）
3. リポジトリを clone する
4. 自分のブランチを作成する  
   例：`git checkout -b yourname-model`
5. `model.py` を編集して独自モデルを作成
6. 動作確認 → `evaluation.py` を実行
7. GitHub に push
8. Pull Request を作成して提出
9. 運営が全モデルを評価
10. 結果発表

---

## 🥇 勝敗の決め方

- `evaluation.py` によって各モデルを自動評価します
- 使用する評価指標：**例：分類精度（Accuracy）**
- もっとも高いスコアのモデルが勝利
- スコアが同点の場合：
  - コードの簡潔さ
  - 実行速度  
  の順に優先して判定します

---

## 📘 対決ルール

- **編集してよいのは `model.py` のみ**
- 外部APIは禁止
- 追加ライブラリは禁止（標準ライブラリ＋付属ライブラリのみ）
- 人のコードをコピーしてはいけない
- PR のタイトルは次の形式  
  → `Add model: yourname`
- PR の説明には、工夫点を2行以上書く

---

## 🛠 GitHub 基本操作（最小セット）

### リポジトリを取得
```

git clone <このリポジトリURL>

```

### ブランチを作る
```

git checkout -b yourname-model

```

### 変更をコミット
```

git add .
git commit -m "Add my model"

```

### ブランチを push
```

git push origin yourname-model

```

### PR を作成
GitHub 上で **Compare & pull request** をクリック → 作成

---

## 📁 リポジトリ構成

```

.
├── model.py         # ここを編集して提出
├── evaluation.py    # 運営が評価に使用
├── dataset/         # 評価用データ
├── participants/    # 提出モデルの保存先
└── README.md

```

---

## ⚠️ 注意事項

- Python 3.x を使用
- 提出締切は運営が指定
- PR が出ないと評価対象になりません

---

楽しみながら GitHub と Python を身につけましょう！💻🔥
```

