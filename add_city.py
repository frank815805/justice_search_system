import pandas as pd
df = pd.read_csv('./data/地方法院.csv')
road_data = pd.read_csv('./data/opendata110road.csv') # 也可以用其他opendata去比對地區給予城市
new_df = pd.DataFrame(columns=['JID', 'JYEAR', 'JCASE', 'JNO', 'JDATE', 'JTITLE', 'JFULL', 'PLACE', 'CITY'])
df = df.drop(columns=['Unnamed: 0'])
# df[df['JFULL'].str.contains('碰撞')]
# print(df.loc[10831]['JFULL'])
for idx, row in df.iterrows():
    try:
        row['JFULL'] = row['JFULL'].replace('\u3000', '').replace('\r', '').replace('\n', '')
        row['CITY'] = row['PLACE'][2:4]
        new_df = new_df.append(row, ignore_index=True)
    except:
        pass
print()