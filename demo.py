# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 14:00:30 2015

@author: hehe
"""
from easy_tfidf import tfidf_for_files

input_path = './test_data_zh'
cn = tfidf_for_files(input_path)
tfidf = cn.compute_tfidf()

for item in tfidf.items():
    print item[0], item[1]
