#!/usr/bin/python 
#-*- coding: utf-8 -*-

from collections import Counter


a = [1, 23]
c = Counter(a)
c.update([34])
# c.update(1)
# print (c)
# c.update(23)
print (c)