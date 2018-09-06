#!/usr/bin/env python
# encoding: utf-8
"""
@author: Changsong Li
@contact: lichangsongpku@163.com
@file: test
@time: 2018/9/5 上午11:51
@desc:
"""
from gensim.models import word2vec
import io

model = word2vec.Word2Vec.load('model.bin')      #模型讀取方式
#model.most_similar(positive=['woman', 'king'], negative=['man']) #根据给定的条件推断相似词
#model.doesnt_match("breakfast cereal dinner lunch".split()) #寻找离群词
#model.similarity('学校', '学生') #计算两个单词的相似度
#print model['maybe'] #获取单词的词向量

print model.most_similar('reason')