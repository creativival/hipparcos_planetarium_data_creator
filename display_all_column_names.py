from astroquery.vizier import Vizier
import pandas as pd

# すべてのカラムを取得するために、columns=["*"]を設定するか省略
v = Vizier(
    columns=["*"],  # すべてのカラムを取得
    row_limit=1     # 1行だけ取得（カラム名を見るため）
)

# カタログ情報を取得
result = v.query_constraints(catalog="I/239/hip_main")
catalog = result[0]

# すべてのカラム名を表示
print("Hipparcosカタログのすべてのカラム名:")
for colname in catalog.colnames:
    # カラム名と説明を表示
    col_desc = catalog[colname].description if hasattr(catalog[colname], 'description') else "説明なし"
    print(f"{colname}: {col_desc}")

# 利用可能なカラム数を表示
print(f"\n合計 {len(catalog.colnames)} カラムが利用可能です")