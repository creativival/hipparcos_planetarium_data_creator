from astroquery.vizier import Vizier
import pandas as pd

# 出力ファイル名を定義
input_file = "data/hip_lite_major_processed.csv"
output_file = "data/hip_lite_major.csv"

# Vizier設定（← ここがポイント）
v = Vizier(
    columns=["HIP", "RAhms", "DEdms", "Vmag"],
    row_limit=-1  # ← 取得制限を無効化
)

# 視等級6.5以下の明るい星だけ取得
result = v.query_constraints(catalog="I/239/hip_main", Vmag="<6.5")
catalog = result[0]

# DataFrameに変換
df = catalog.to_pandas()

# カラム順を指定（念のため）
df = df[["HIP", "RAhms", "DEdms", "Vmag"]]

# CSVとして保存
df.to_csv(input_file, index=False, header=False)

# ファイルを読み込んで置換処理
with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
    for line in infile:
        # 置換処理を実行
        # マイナス記号 (-) を 0 に置換
        line = line.replace('-', '0,')
        # プラス記号 (+) を 1 に置換
        line = line.replace('+', '1,')
        # スペースをカンマ (,) に置換
        line = line.replace(' ', ',')

        # 処理済みの行を書き込み
        outfile.write(line)

print(f"置換処理が完了しました。結果は {output_file} に保存されました。")

print("hip_lite_major.csv ファイルが作成されました。")
