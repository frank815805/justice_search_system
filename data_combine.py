# -*- coding: UTF-8 -*-

import pandas as pd
from os import walk
from os.path import join
import json
# 指定要列出所有檔案的目錄
data_path = './data'
df = pd.DataFrame(columns=['JID', 'JYEAR', 'JCASE', 'JNO', 'JDATE', 'JTITLE', 'JFULL', 'PLACE'])
city_data = pd.read_csv('./data/opendata110road.csv')
# 遞迴列出所有檔案的絕對路徑
for root, dirs, files in walk(data_path):
    for f in files:
        fullpath = join(root, f)
        print(fullpath)
        if fullpath.endswith('.json'):
            with open(fullpath) as f:
                data = json.load(f)
                data['PLACE'] = root.split('/')[-1]
                df = df.append(data, ignore_index=True)
                # print()
df.to_csv('./data/all_data.csv', index=False)
print()