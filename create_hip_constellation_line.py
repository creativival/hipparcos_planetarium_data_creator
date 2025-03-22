import json
import csv

# JSONファイルを読み込む
with open('stellarium/skycultures/modern/index.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# CSVファイルを作成
with open('data/hip_constellation_line.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    # # ヘッダー行を書き込む
    # writer.writerow(['Constellation', 'Star1_HIP', 'Star2_HIP'])

    # 各星座についてループ
    for constellation in data['constellations']:
        # 星座の三文字略号を取得 (例: "CON modern And" から "And" を抽出)
        abbr = constellation['id'].split()[2]

        # 各星座線についてループ
        for line in constellation['lines']:
            # 線を形成する連続した星のペアについてループ
            for i in range(len(line) - 1):
                # 星1と星2のHipparcos IDを取得
                star1_hip = line[i]
                star2_hip = line[i + 1]

                # CSVに行を書き込む
                writer.writerow([abbr, star1_hip, star2_hip])

print("data/hip_constellation_line.csv ファイルが作成されました。")