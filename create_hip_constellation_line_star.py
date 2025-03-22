import json
import pandas as pd
from astroquery.vizier import Vizier
import numpy as np

# 出力ファイル名を定義
input_file = "data/hip_constellation_line_star_processed.csv"
output_file = "data/hip_constellation_line_star.csv"

# JSONファイルを読み込む
with open('stellarium/skycultures/modern/index.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# すべての星IDを格納するセット（重複を自動的に排除）
all_star_ids = set()

# 各星座の星座線からHipparcos IDを抽出
for constellation in data['constellations']:
    for line in constellation['lines']:
        for star_id in line:
            # 数値のIDのみを処理
            try:
                # 文字列であれば数値に変換してみる
                if isinstance(star_id, str):
                    star_id = int(star_id)
                all_star_ids.add(star_id)
            except (ValueError, TypeError):
                # 非数値IDは無視
                pass

print(f"数値のHipparcos ID数: {len(all_star_ids)}")

# Vizier設定 - より多くの列を取得
v = Vizier(
    columns=["HIP", "RAhms", "DEdms", "Vmag", "Plx", "pmRA", "pmDE", "SpType", "B-V"],
    row_limit=-1  # 取得制限を無効化
)

try:
    # 重要な修正：IDs を文字列のリストに変換
    hip_ids_str = [str(hip_id) for hip_id in all_star_ids]

    # IDが多すぎる場合はバッチ処理
    batch_size = 100
    all_results = []

    for i in range(0, len(hip_ids_str), batch_size):
        batch = hip_ids_str[i:i + batch_size]
        print(f"バッチ {i // batch_size + 1}/{(len(hip_ids_str) + batch_size - 1) // batch_size} を処理中...")
        result = v.query_constraints(catalog="I/239/hip_main", HIP=batch)
        if result and len(result) > 0:
            all_results.append(result[0])

    if all_results:
        # 結果を結合
        from astropy.table import vstack

        catalog = vstack(all_results)

        # DataFrameに変換
        df = catalog.to_pandas()

        # カラム順を指定
        columns = ["HIP", "RAhms", "DEdms", "Vmag", "Plx", "pmRA", "pmDE", "SpType", "B-V"]
        available_columns = [col for col in columns if col in df.columns]
        df = df[available_columns]

        # CSVとして保存
        df.to_csv(input_file, index=False, header=False)

        print(f"取得した星の数: {len(df)}")
        print(f"{input_file} ファイルが作成されました。")

        # 結果の最初の数行を表示
        print("\n最初の5行のデータ:")
        print(df.head())

        # 見つからなかったHIPの星を確認
        missing_ids = set(all_star_ids) - set(df['HIP'].astype(int).tolist())
        if missing_ids:
            print(f"\n見つからなかったHIP ID数: {len(missing_ids)}")
            print("最初の10個の見つからなかったID:", list(missing_ids)[:10])

        # ファイルを読み込んで置換処理
        with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
            for line in infile:
                # 置換処理を実行
                # スペースをカンマ (,) に置換
                line = line.replace(' ', ',')

                # 処理済みの行を書き込み
                outfile.write(line)

        print(f"{output_file} ファイルが作成されました。")
    else:
        print("Vizierからデータを取得できませんでした。")

except Exception as e:
    print(f"エラーが発生しました: {e}")
    import traceback

    traceback.print_exc()