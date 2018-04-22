#!/usr/bin/python
# -*- coding: utf-8 -*-


def split_train():
    

def generate_input_lr():
    keys = ['uid', 'age', 'gender', 'marriageStatus', 'education', 'consumptionAbility', 'LBS',
            'interest1', 'interest2', 'interest3', 'interest4', 'interest5',
            'kw1', 'kw2', 'kw3', 'topic1', 'topic2', 'topic3', 'appIdInstall',
            'appIdAction', 'ct', 'os', 'carrier', 'house']
    
users = []

keys = ['uid', 'age', 'gender', 'marriageStatus', 'education', 'consumptionAbility', 'LBS',
        'interest1', 'interest2', 'interest3', 'interest4', 'interest5',
        'kw1', 'kw2', 'kw3', 'topic1', 'topic2', 'topic3', 'appIdInstall',
        'appIdAction', 'ct', 'os', 'carrier', 'house']


with open('../data/preliminary_contest_data/userFeature.data', 'r') as f:
    for l in f:
        features = l.strip().split('|')
        user = {}
        for key in keys:
            user[key] = []

        for f in features:
            f_name = f.split(' ')[0]
            print (f_name)
            for v in f.split(' ')[1:]:
                user[f_name].append(v)
        users.append(user)
        # tc + 1
        # if tc > 10:
        break

print (users)
