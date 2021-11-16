import pandas as pd
from os import walk
from os.path import join
import json
# 指定要列出所有檔案的目錄
mypath = "./data"
df = pd.DataFrame(columns=['JID', 'JYEAR', 'JCASE', 'JNO', 'JDATE', 'JTITLE', 'JFULL'])

# 遞迴列出所有檔案的絕對路徑
for root, dirs, files in walk(mypath):
    for f in files:
        fullpath = join(root, f)
        print(fullpath)
        if fullpath.endswith('.json'):
            with open(fullpath) as f:
                data = json.load(f)
                df = df.append(data, ignore_index=True)
                # print()

print()