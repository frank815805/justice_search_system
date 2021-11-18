from scipy.spatial import distance
from opencc import OpenCC
import pandas as pd

# 使用huggingface pipeline

if __name__ == '__main__':
    df = pd.read_csv('./data/city_data.csv')
    cc = OpenCC('t2s')  # 繁體中文 -> 簡體中文 https://yanwei-liu.medium.com/python%E8%87%AA%E7%84%B6%E8%AA%9E%E8%A8%80%E8%99%95%E7%90%86-%E5%9B%9B-%E7%B9%81%E7%B0%A1%E8%BD%89%E6%8F%9B%E5%88%A9%E5%99%A8opencc-74021cbc6de3

    total_city = df['CITY'].unique()
    while True:
        condition_list = []
        search_mode = input('請選擇搜尋模式：0:精確, 1:模糊')
        if search_mode != '0' and search_mode != '1':
            print('错误：請選擇模式0或者1唷！')
            continue
        location = input('請選擇地區：') #透過UI可決定 地區 在此假設不亂輸入地區(台北依照opendata或者自行建立的對應dict 來將臺北與士林接納入臺北 高雄與橋頭納入高雄)
        condition_number = input('請選擇搜尋條件個數：') #透過UI到時候依據空白split
        if condition_number.isdigit():
            if 0 < int(condition_number):
                break
        else:
            print('错误：要求输入的是正整數唷！')
    for condition_idx in range(int(condition_number)):
        condition_list.append(input('請輸入搜尋字串' + str(condition_idx + 1) + '：'))
    if search_mode == '0':
        if location == '臺北':
            ans = df[df['JFULL'].str.contains('|'.join(condition_list)) & ( (df['CITY'] =='士林') | (df['CITY'] =='臺北') ) ]
        elif location == '高雄':
            ans = df[df['JFULL'].str.contains('|'.join(condition_list)) & ( (df['CITY'] =='高雄') | (df['CITY'] =='橋頭') ) ]
        else:
            ans = df[df['JFULL'].str.contains('|'.join(condition_list)) & (df['CITY'] == location)]
    elif search_mode == '1':
        if location == '臺北':
            ans = df[( (df['CITY'] == '士林') | (df['CITY'] == '臺北') ) ]
        elif location == '高雄':
            ans = df[( (df['CITY'] == '高雄') | (df['CITY'] == '橋頭') ) ]
        else:
            ans = df[(df['CITY'] == location)]

# sentence_embedding = (classifier(cc.convert('我不是辰峰')))
# sentence_embedding2 = (classifier(cc.convert('撞車囉')))
# Aflat = [sum(x) for x in zip(*sentence_embedding[0])]
# Bflat = [sum(x) for x in zip(*sentence_embedding2[0])]
# dist2 = distance.cosine(Aflat, Bflat)
print(ans)
