# Python GitHub Battle Workshop

Pythonサークル向け GitHub 体験会用リポジトリ

## 📋 ワークショップ概要

このワークショップでは、**GitHub の基本操作**と**Python プログラミング**を組み合わせた実践的な学習体験を提供します。

### 学習内容
- **GitHub 基本操作**: リポジトリのクローン、ブランチ作成、コミット、プッシュ、プルリクエスト
- **Python ミニ対決**: GAN（敵対的生成ネットワーク）風のモデル対決形式で、参加者が作成したモデルを評価

### 対象者
- Git/GitHub 初心者の方
- Python プログラミングに興味がある方
- チーム開発の基礎を学びたい方

---

## 🚀 当日の流れ

### 1. リポジトリをクローン
```bash
git clone https://github.com/gayagayataiga/python-github-battle-workshop.git
cd python-github-battle-workshop
```

### 2. 自分のブランチを作成
```bash
git checkout -b your-name-model
```
※ `your-name-model` の部分は自分の名前やニックネームに置き換えてください

💡 **Git 2.23以降をお使いの方へ**: 新しいコマンド `git switch -c your-name-model` も使用できます

### 3. モデルを作成
`model.py` ファイルを作成し、自分のモデルを実装します
- 指定された形式に従ってコードを記述
- 創造性を発揮してユニークなアプローチを試してみましょう

### 4. コミット＆プッシュ
```bash
git add model.py
git commit -m "Add my model implementation"
git push origin your-name-model
```

### 5. プルリクエストを作成
- GitHub 上で自分のブランチから `main` ブランチへのプルリクエストを作成
- タイトルと説明を記載

### 6. 評価
- 提出されたモデルを評価指標に基づいて評価
- スコアを算出

### 7. 結果発表
- 最高スコアを獲得した参加者を表彰
- 優秀なアプローチを共有

---

## 🏆 勝敗基準

### 評価指標

モデルは以下の基準で評価されます：

1. **精度（Accuracy）**: 50%
   - モデルの出力精度を評価
   
2. **創造性（Creativity）**: 30%
   - アプローチの独創性
   - コードの工夫
   
3. **コード品質（Code Quality）**: 20%
   - 可読性
   - コメントの適切さ
   - Pythonic な記述

### 総合スコア計算
```
総合スコア = 精度 × 0.5 + 創造性 × 0.3 + コード品質 × 0.2
```

### 同点時の扱い
同点の場合は、以下の優先順位で順位を決定します：
1. 精度が高い方
2. 創造性スコアが高い方
3. 提出時刻が早い方

---

## 📝 参加ルール

### 必須事項

1. **ブランチ作成**
   - 必ず自分専用のブランチを作成してください
   - ブランチ名: `your-name-model` (例: `taro-model`, `hanako-model`)
   - `main` ブランチへの直接コミットは禁止

2. **model.py の提出**
   - ファイル名は必ず `model.py` としてください
   - 指定されたフォーマットに従ってください
   - 他の参加者のファイルを変更しないでください

3. **プルリクエスト作成**
   - 自分のブランチから `main` ブランチへのPRを作成
   - タイトル: `[Your Name] モデル提出`
   - 説明欄にモデルのアプローチを簡潔に記載

### 禁止事項
- 他の参加者のブランチやファイルの変更
- `main` ブランチへの直接プッシュ
- 外部ライブラリの過度な使用（標準ライブラリを推奨）

---

## 💡 GitHub 基本操作ガイド

### 1. Clone（クローン）
リポジトリをローカル環境にコピーします。

```bash
git clone <リポジトリURL>
```

**説明**: GitHub 上のリポジトリを自分のパソコンにダウンロードする操作です。

---

### 2. Branch（ブランチ）
作業用の独立した環境を作成します。

```bash
# ブランチを作成して切り替え
git checkout -b branch-name

# ブランチの一覧を確認
git branch

# 既存のブランチに切り替え
git checkout branch-name
```

💡 **Git 2.23以降の新しいコマンド**:
```bash
# ブランチを作成して切り替え
git switch -c branch-name

# 既存のブランチに切り替え
git switch branch-name
```

**説明**: ブランチは、他の人の作業に影響を与えずに自分の変更を進められる機能です。

---

### 3. Commit（コミット）
変更をローカルリポジトリに記録します。

```bash
# ファイルをステージングエリアに追加
git add <ファイル名>

# すべての変更をステージング
git add .

# コミットを作成
git commit -m "変更内容を説明するメッセージ"
```

**説明**: コミットは、変更の履歴を記録するスナップショットのようなものです。

---

### 4. Push（プッシュ）
ローカルの変更を GitHub に反映します。

```bash
git push origin branch-name
```

**説明**: ローカルで行った変更を GitHub 上のリポジトリにアップロードします。

---

### 5. Pull Request（プルリクエスト）
自分の変更を本流（main ブランチ）に取り込むリクエストを作成します。

**手順**:
1. GitHub のリポジトリページにアクセス
2. "Pull requests" タブをクリック
3. "New pull request" ボタンをクリック
4. ベースブランチに `main`、比較ブランチに自分のブランチを選択
5. タイトルと説明を入力
6. "Create pull request" をクリック

**説明**: プルリクエスト（PR）は、コードレビューを依頼し、変更を統合してもらうための機能です。

---

## 🛠️ トラブルシューティング

### Q1: `git push` でエラーが出る
```bash
# リモートの最新情報を取得
git fetch origin

# ブランチを再作成
git checkout main
git pull origin main
git checkout -b new-branch-name
```

💡 **Git 2.23以降の場合**:
```bash
git switch main
git pull origin main
git switch -c new-branch-name
```

### Q2: コミットメッセージを間違えた
```bash
# 直前のコミットメッセージを修正
git commit --amend -m "正しいメッセージ"
```

### Q3: 間違ったファイルをコミットしてしまった
```bash
# ファイルをステージングから外す
git reset HEAD <ファイル名>
```

---

## 📚 参考リンク

- [GitHub公式ドキュメント](https://docs.github.com/ja)
- [Git入門](https://git-scm.com/book/ja/v2)
- [Python公式ドキュメント](https://docs.python.org/ja/3/)

---

## 📞 お問い合わせ

質問や問題が発生した場合は、運営スタッフまでお気軽にお声がけください。

---

**Happy Coding! 🎉**
