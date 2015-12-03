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
计算TFIDF,使用一个文件夹作为输入,文件夹中是要计算的文件.
使用结巴分词作为分词工具.

例子:
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