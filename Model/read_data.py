#!/usr/bin/python
# -*- coding: utf-8 -*-

tc  = 0

with open('../data/preliminary_contest_data/userFeature.data', 'r') as f:
	for l in f:
		print (l)
		# tc + 1
		# if tc > 10:
		break

print (tc)