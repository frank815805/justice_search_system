from transformers import pipeline, BertModel, BertTokenizer
import torch
import numpy as np
from scipy.spatial import distance
from opencc import OpenCC

# 使用huggingface pipeline

cc = OpenCC('t2s') #繁體中文 -> 簡體中文 https://yanwei-liu.medium.com/python%E8%87%AA%E7%84%B6%E8%AA%9E%E8%A8%80%E8%99%95%E7%90%86-%E5%9B%9B-%E7%B9%81%E7%B0%A1%E8%BD%89%E6%8F%9B%E5%88%A9%E5%99%A8opencc-74021cbc6de3

# tokenizers = BertTokenizer.from_pretrained('hfl/chinese-legal-electra-large-discriminator')
# model = BertModel.from_pretrained('hfl/chinese-legal-electra-large-discriminator')
# inputs = tokenizers(cc.convert('我不是辰峰'), return_tensors='pt')
# outputs = model(**inputs)
# inputs = tokenizers(cc.convert('撞車囉'), return_tensors='pt')
# outputs2 = model(**inputs)
# cos = torch.nn.CosineSimilarity(dim=1, eps=1e-6)
# dist = cos(outputs.pooler_output, outputs2.pooler_output)

# transformers & chinese legal large electra https://github.com/ymcui/Chinese-ELECTRA#%E5%BF%AB%E9%80%9F%E5%8A%A0%E8%BD%BD
classifier = pipeline('feature-extraction', model='hfl/chinese-legal-electra-large-discriminator', tokenizer='hfl/chinese-legal-electra-large-discriminator')
sentence_embedding = (classifier(cc.convert('我不是辰峰')))
sentence_embedding2 = (classifier(cc.convert('撞車囉')))
Aflat = [sum(x) for x in zip(*sentence_embedding[0])]
Bflat = [sum(x) for x in zip(*sentence_embedding2[0])]
dist2 = distance.cosine(Aflat, Bflat)
print()