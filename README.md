##easy_tfidf
计算TFIDF,使用一个文件夹作为输入,文件夹中是要计算的输入文件.
使用结巴分词作为分词工具.
##安装
先装结巴分词
```
sudo pip install jieba
```
再装easy_tfidf
```
sudo python setup.py --record record.txt
```

##例子:
```
$ ls test_data_zh/
file1  file2  file3
```
在python终端里输入:
```
from easy_tfidf import tfidf_for_files
input_path = './test_data_zh'
zh_tfidf = tfidf_for_files(input_path)
tfidf = zh_tfidf.compute_tfidf()
```
部分输出
```
for word, data in tfidf.items():
    print word, data

最高 [2, [('file1', 1), ('file3', 1)]]
沿 [1, [('file3', 1)]]
影响 [2, [('file1', 1), ('file3', 1)]]
大浪 [1, [('file2', 1)]]
全州 [1, [('file2', 1)]]
北面 [2, [('file2', 1), ('file3', 1)]]
预警 [2, [('file1', 1), ('file2', 4)]]
```
格式为:
```
词语, [文档频率, [(文档1, 词频), (文档2, 词频) ... (文档n, 词频)]]
```

Compute TFIDF for several files in a folder.
User jieba as word split tool.

For example:
```
$ ls test_data_en/
file1  file2  file3
```
In your python terminal:
```
from easy_tfidf import tfidf_for_files
input_path = './test_data_en'
en_tfidf = tfidf_for_files(input_path)
tfidf = en_tfidf.compute_tfidf()
```
Example output
```
for word, data in tfidf.items():
    print word, data

five [1, [('file2', 2)]]
the [3, [('file1', 37), ('file2', 19), ('file3', 43)]]
years [2, [('file1', 1), ('file2', 11)]]
make [1, [('file3', 1)]]
came [1, [('file3', 2)]]

```