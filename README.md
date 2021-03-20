# vec2seq
研究のコード
## ファイル
- `data/data.csv`
    - GSL単語の内、名詞のみを抽出
    - 上記で抽出した単語からランダムに402組の単語ペアを取得
    - 手法1にその単語ペアを入力し、文を生成
    - 手法2への教師データとして上記の生成文を以下の条件で抽出
        - 文章における単語数: 15〜25
        - 1ペアあたりに抽出する文章数の上限: 500
    - FEが複数単語の場合は教師データから除く

- `data/data_v2.csv`
    - `data/data.csv`において「同じ入力に対して正解出力を複数与えている」問題を解消

- `data/data_v3.csv`
    - ミニバッチ学習のために`data/shuffle_csv_row.py`を用いてシャッフル