# -*- coding: UTF-8 -*-
from transformers import pipeline
import pandas as pd
from opencc import OpenCC
import pickle
df = pd.read_csv('./data/city_data.csv')
cc = OpenCC('t2s')  # 繁體中文 -> 簡體中文 https://yanwei-liu.medium.com/python%E8%87%AA%E7%84%B6%E8%AA%9E%E8%A8%80%E8%99%95%E7%90%86-%E5%9B%9B-%E7%B9%81%E7%B0%A1%E8%BD%89%E6%8F%9B%E5%88%A9%E5%99%A8opencc-74021cbc6de3
df['embedding'] = ''
# transformers & chinese legal large electra https://github.com/ymcui/Chinese-ELECTRA#%E5%BF%AB%E9%80%9F%E5%8A%A0%E8%BD%BD
classifier = pipeline('feature-extraction', model='hfl/chinese-legal-electra-large-discriminator',
                      tokenizer='hfl/chinese-legal-electra-large-discriminator')
for idx, row in df.iterrows():
    try:
        sentence_embedding = (classifier(cc.convert(df['JFULL'][idx])[0:500]))
        sentence_embedding_sum = [sum(x) for x in zip(*sentence_embedding[0])]
        df['embedding'][idx] = sentence_embedding_sum
    except:
        pass
with open('./data/embedding.pickle', 'wb') as handle:
    pickle.dump(df, handle, protocol=pickle.HIGHEST_PROTOCOL)
print()