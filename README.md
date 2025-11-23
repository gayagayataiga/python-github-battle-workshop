# Pythonサークル GitHub体験会 ＋ モデル対決（VSCode & Google Colab対応）

このリポジトリは、Pythonサークルで行う  
**GitHub 基本操作の体験（VSCode）** と  
**Google Colab 上でモデルを開発して GitHub に push する対決企画**  
の両方を学ぶための教材です。

---

# 🚀 ワークショップ概要

1. **VSCode**  
   - clone / branch / commit / pull / push を GUI で練習  
   - GitHub の基本操作に慣れる

2. **Google Colab**  
   - モデル開発（train / 改良）を行う  
   - Colab 上で GitHub に **直接 push** する  
   → Python ファイル以外の成果物も push 可能！

3. **Pull Request の作成**  
   - 完成したモデルを PR で提出  
   - 運営が全モデルを評価し対決！

---

# 🗓 当日の流れ（VSCode & Colab）

## 0. GitHubの基礎説明（5分）
- Git と GitHub の違い  
- clone / commit / branch / push / pull / PR の概念

---

## 1. リポジトリの説明（5分）
- 触るファイル  
  - モデル本体：`model.py`  
  - 必要であれば他設定ファイルも追加OK  
- 提出は Pull Request で行う

---

## 2. VSCode で GitHub 基本操作を練習（10分）
### 練習内容（GUI）
- clone  
- branch作成  
- ファイル編集  
- commit  
- **pull**  
- **push**

※ 実際のモデル開発は Colab で行うが、VSCodeでも Git 操作を必ず触る。

---

## 3. Google Colab で開発

### ① GitHub リポジトリを clone
```bash
!git clone <リポジトリURL>
%cd <フォルダ名>
````

### ② ブランチ作成（Colab内）

```bash
!git checkout -b yourname-model
```

### ③ Colab で自由に開発

* model.py を編集
* notebook 追加もOK
* 結果を保存するフォルダを追加してもOK
  → 画像 / 重み / ノートブック も push できる！

---

## 4. Google Colab から GitHub に push（重要）

### ① GitHub アカウントの設定

```bash
!git config --global user.email "you@example.com"
!git config --global user.name "yourname"
```

### ② 変更の commit & push

```bash
!git add .
!git commit -m "Update model and results"
!git push origin yourname-model
```

※ push できるのは Python だけでなく
Notebook（`.ipynb`）、画像、結果ファイルなど **すべてOK**

---

## 5. Pull Request を作成（GUI）

* GitHub の Web ページへ移動
* 対象ブランチを選択
* 「Compare & pull request」

PR タイトル例：
`Add updated model by yourname`

PR 説明：

* 改良点
* どんな学習をしたか
* 追加したファイルの説明

を2行以上。

---

## 6. 運営が全モデルを評価

* PRを merge
* `evaluation.py` を実行してスコアを算出

---

## 7. 結果発表

* 精度・スコアの順位を公開
* 同点時の判断

  1. コードの簡潔さ
  2. 学習再現性
  3. 実行速度

---

# 📘 勝敗の決め方

* 評価スクリプト `evaluation.py` を使用
* 指標：**Accuracy（精度）** または事前に説明するスコア
* 同点は再現性・速度・コード品質で判定

---

# 📁 リポジトリ構成

```
.
├── model.py          # Colabで開発
├── evaluation.py     # 運営が評価で使用
├── dataset/          # 評価用データ
├── colab/            # Colab用ノート 
├── results/          # モデル結果（画像/重み/ログなど）
└── README.md
```

---

# ⚠ 注意事項

* モデル開発は **Google Colab 推奨**
* Colab で push できるように GitHub 認証が必要
* PR が提出されていないモデルは評価不可
* 大規模外部データセットの使用は禁止（公平性のため）

---

VSCodeでGitを身につけ、Colabでモデルを改善し、
最強モデルを目指して勝負しましょう！🔥

```

どれ欲しい？
```
