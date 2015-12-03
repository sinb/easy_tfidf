# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 14:04:25 2015

@author: hehe
"""
import re
from os import listdir
from os.path import isfile, join
from itertools import groupby
from operator import itemgetter
import jieba
class tfidf_for_files:
    def __init__(self,dir):
        """
        initialize file paths
        """
        self.dirname = dir
        self.filenames = [name for name in listdir(dir) if isfile(join(dir, name))]

    def compute_tf_by_file(self,separator=' '):
        """
        for each file, calcute term frequency
        return format is :
            'word', 'file_name', term-frequency
        """
        word_docid_tf = []
        for name in self.filenames:
            with open(join(self.dirname, name), 'r') as f:
                tf_dict = dict()
                for line in f:
                    line = self.process_line(line)
                    words = jieba.cut(line.strip(), cut_all=False)
                    #words = line.rstrip().split(separator)
                    for word in words:
                        tf_dict[word] = tf_dict.get(word, 0) + 1
            tf_list = tf_dict.items()
            word_docid_tf += [[item[0], name, item[1]] for item in tf_list]
        return word_docid_tf                
    def compute_tfidf(self):
        """
        do some statistics, i.e, calcute document frequency
        """
        word_docid_tf = self.compute_tf_by_file()
        word_docid_tf.sort()
        tfidf = dict()
        for current_word, group in groupby(word_docid_tf, itemgetter(0)):
            doclist = []
            df = 0
            for current_word, file_name, tf in group:
                doclist.append((file_name, tf))
                df += 1
            tfidf[current_word] = [df, doclist]
        return tfidf
    def process_line(self, line):
        line = line.decode("utf8")
        line = re.sub("]-·[\s+\.\!\/_,$%^*(+\"\']+|[+——！，。？、~@#￥%……&*（）]+".decode("utf8"),
                      " ".decode("utf8"),line)
        return line
    def printFileNames(self):
        for name in self.filenames:
            print join(self.dirname, name)
