# justice_search_system
請使用司法院Opendata (https://opendata.judicial.gov.tw/dataset?categoryTheme4Sys%5B0%5D=051&sort.publishedDate.order=desc&page=1 ) 202101 - 202106年地方法院的判決書

以此規劃一個搜尋系統：提供跟車禍相關的判決書搜尋，以協助使用者找到適合的判決書並參考其判賠金額

1. 不需UI介面，能於程式內輸入搜尋條件即可，搜尋方法可自由設計
2. 請以關鍵字： 台北市  擦撞、高雄市  酒駕   為例展示搜尋後結果
3. 承上，以此結果分析該例子歸納後的判賠金額分佈
4. 額外加分：建立模型預測202107符合任意關鍵字(Ex: 台北市 擦撞 頭)的判決書，可能的 精神賠償金 金額分佈
5. 額外加分：搜尋結果包含類似語意之結果且不需人工事前標注判決書

## How to use it

```bash
$ # Get the code
$ git clone https://github.com/frank815805/justice_search_system.git
$ cd justice_search_system
$
$ # Virtualenv modules installation (Unix based systems)
$ virtualenv env
$ source env/bin/activate
$
$ # Virtualenv modules installation (Windows based systems)
$ # virtualenv env
$ # .\env\Scripts\activate
$
$ pip3 install -r requirements.txt
```

## Download 202101-202107 data set(with embedding)

download this file and put in ./data/

https://drive.google.com/file/d/1vO-bOxDMOSPdP3VR1XyuqRNy0M1TscLC/view?usp=sharing

## Introduction of modules used
Hugging Face: https://huggingface.co/
Build, train and deploy state of the art models powered by the reference open source in machine learning.

Chinese-ELECTRA: https://github.com/ymcui/Chinese-ELECTRA
谷歌与斯坦福大学共同研发的最新预训练模型ELECTRA因其小巧的模型体积以及良好的模型性能受到了广泛关注。 为了进一步促进中文预训练模型技术的研究与发展，哈工大讯飞联合实验室基于官方ELECTRA训练代码以及大规模的中文数据训练出中文ELECTRA预训练模型供大家下载使用。 其中ELECTRA-small模型可与BERT-base甚至其他同等规模的模型相媲美，而参数量仅为BERT-base的1/10。

OpenCC: https://github.com/yichen0831/opencc-python
Open Chinese convert (OpenCC) in pure Python.



