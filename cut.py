#!/usr/bin/env python
# encoding: utf-8
"""
@author: Changsong Li
@contact: lichangsongpku@163.com
@file: train
@time: 2018/9/5 上午11:20
@desc:
"""
import jieba
import io

# 加载自己的词表
jieba.load_userdict("wordlist.txt")


def main():
    with io.open('wenben.txt', 'r', encoding='utf-8') as content:
        for line in content:
            seg_list = jieba.cut(line)
            #print '/'.join(seg_list)
            with io.open('segment.txt', 'a', encoding='utf-8') as output:
                output.write(' '.join(seg_list))


if __name__ == '__main__':
    main()
