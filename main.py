# -*- coding: UTF-8 -*-

from scipy.spatial import distance
from transformers import pipeline
from opencc import OpenCC
import pandas as pd
import pickle
# 使用huggingface pipeline

if __name__ == '__main__':
    classifier = pipeline('feature-extraction', model='hfl/chinese-legal-electra-large-discriminator',
                          tokenizer='hfl/chinese-legal-electra-large-discriminator')
    with open('./data/embedding.pickle', 'rb') as handle:
        df = pickle.load(handle)
    cc = OpenCC('t2s')  # 繁體中文 -> 簡體中文 https://yanwei-liu.medium.com/python%E8%87%AA%E7%84%B6%E8%AA%9E%E8%A8%80%E8%99%95%E7%90%86-%E5%9B%9B-%E7%B9%81%E7%B0%A1%E8%BD%89%E6%8F%9B%E5%88%A9%E5%99%A8opencc-74021cbc6de3
    dist = []
    total_city = df['CITY'].unique() #找出所有城市
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
        if '擦撞' in condition_list:
            ans = ans[(ans['JTITLE'] == '過失傷害') | (ans['JTITLE'] == '損害賠償') | (ans['JTITLE'] == '交通裁決') | (ans['JTITLE'] == '交通裁決等')
            | (ans['JTITLE'] == '公共危險') | (ans['JTITLE'] == '公共危險等') | (ans['JTITLE'] == '過失致死等') | (ans['JTITLE'] == '交通裁決')] #篩選出有可能為擦撞的類別
            ans = ans[~ans['JFULL'].str.contains('.pdf')] #先不納入pdf資料進來考慮
            ans = ans[ans['JFULL'].str.contains('車')] #篩選車資料
        elif '酒駕' in condition_list:
            ans = ans[(ans['JTITLE'] == '過失傷害') | (ans['JTITLE'] == '聲請定其應執行刑') | (ans['JTITLE'] == '交通裁決') | (ans['JTITLE'] == '交通裁決等')
            | (ans['JTITLE'] == '公共危險') | (ans['JTITLE'] == '公共危險等') | (ans['JTITLE'] == '聲明異議') | (ans['JTITLE'] == '交通裁決') | (ans['JTITLE'] == '妨害公務')] #篩選出有可能為擦撞的類別
            ans = ans[~ans['JFULL'].str.contains('.pdf')] #先不納入pdf資料進來考慮
            ans = ans[ans['JFULL'].str.contains('不能安全駕駛')] #篩選不能安全駕駛資料
        convert_str = ''.join(condition_list)
        # convert_str = '第2項所示。八、據上論結，本件原告之訴為無理由，依行政訴訟法第98條第    1項前段、第237條之7、第237條之8第1項，判決如主文。中華民國110 年1 月11日                  行政訴訟庭法官  張百見以上正本係照原本作成。如對本判決上訴，非以其違背法令為理由，不得為之，且須於判決送達後20日內向本院提出上訴狀。中華民國110 年1 月11日                              書記官  李佩玲'
        sentence_embedding = (classifier(cc.convert(convert_str[0:500])))
        sentence_embedding_sum = [sum(x) for x in zip(*sentence_embedding[0])]
        ans['cosine'] = ans['embedding'].map(lambda x: distance.cosine(sentence_embedding_sum, x))
        ans.sort_values(by=['cosine'], inplace=True)
print(ans)
