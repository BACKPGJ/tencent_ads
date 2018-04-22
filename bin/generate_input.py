#!/usr/bin/python
# -*- coding: utf-8 -*-
import csv
import numpy as np
from collections import Counter

def split_train():
    train_set = []
    with open("../data/preliminary_contest_data/train.csv", "r") as f:
        reader = csv.reader(f)
        for rd in reader:
            if reader.line_num == 1:
                continue
            train_set.append(rd)
    tlen = len(train_set)
    split_cut = int(4.0*tlen/5)
    split_train_set = train_set[:split_cut]
    split_valid_set = train_set[split_cut:]
    train_wt = open("../data/preliminary_contest_data/splited_train.csv", "w")
    csv_writer = csv.writer(train_wt)
    csv_writer.writerows(split_train_set)
    train_wt.close()
    valid_wt = open("../data/preliminary_contest_data/splited_valid.csv", "w")
    csv_writer = csv.writer(valid_wt)
    csv_writer.writerows(split_valid_set)
    valid_wt.close()
    print (len(split_train_set))
    print (len(split_valid_set))
    train_ads_pn = {}
    for l in split_train_set:
        if l[0] not in train_ads_pn:
            train_ads_pn[l[0]] = []
        train_ads_pn[l[0]].append(l[-1])
    valid_ads_pn = {}
    for l in split_valid_set:         
        if l [0] not in valid_ads_pn:
            valid_ads_pn[l[0]] = []
        valid_ads_pn[l[0]].append(l[-1])
    
    train_ads_pn_counter = {}
    train_ads_pn_rate = {}
    train_rates = []
    train_num = []
    for aid in train_ads_pn:
        train_ads_pn_counter[aid] = Counter(train_ads_pn[aid])
        train_ads_pn_rate[aid] = train_ads_pn_counter[aid]['-1']/train_ads_pn_counter[aid]['1']
        train_rates.append(train_ads_pn_rate[aid])
        train_num.append(len(train_ads_pn[aid]))
    
    valid_rates = []
    valid_num = []
    valid_ads_pn_counter = {}
    valid_ads_pn_rate = {}
    for aid in valid_ads_pn:
        valid_ads_pn_counter[aid] = Counter(valid_ads_pn[aid])
        valid_ads_pn_rate[aid] = valid_ads_pn_counter[aid]['-1']/valid_ads_pn_counter[aid]['1']
        valid_rates.append(valid_ads_pn_rate[aid])
        valid_num.append(len(valid_ads_pn[aid]))
     
    print (len(train_ads_pn))
    print (len(valid_ads_pn))    
    print ("train set")
    print (np.min(train_rates))
    print (np.max(train_rates))
    print (np.mean(train_rates))
    print (np.min(train_num))
    print (np.max(train_num))
    print (np.mean(train_num))
    print ("valid set")
    print (np.min(valid_rates))
    print (np.max(valid_rates))
    print (np.mean(valid_rates))
    print (np.min(valid_num))
    print (np.max(valid_num))
    print (np.mean(valid_num))


def generate_input_lr():
    keys = ['uid', 'age', 'gender', 'marriageStatus', 'education', 'consumptionAbility', 'LBS',
            'interest1', 'interest2', 'interest3', 'interest4', 'interest5',
            'kw1', 'kw2', 'kw3', 'topic1', 'topic2', 'topic3', 'appIdInstall',
            'appIdAction', 'ct', 'os', 'carrier', 'house']
    keys_dim = {}
    keys_dim['age'] = 6
    keys_dim['gender'] = 3
    keys_dim['marriageStatus'] = 16
    keys_dim['eduction'] = 8
    keys_dim['consumptionAbility'] = 3
    keys_dim['LBS'] = 1000
    keys_dim['interest1'] = 122
    keys_dim['interest2'] = 82
    keys_dim['interest3'] = 10
    keys_dim['interest4'] = 10
    keys_dim['interest5'] = 136
    keys_dim['kw1'] = 0
    keys_dim['kw2'] = 0
    keys_dim['kw3'] = 0
    keys_dim['topic1'] = 10000
    keys_dim['topic2'] = 10000
    keys_dim['topic3'] = 10000
    keys_dim['appIdInstall'] = 0
    keys_dim['appIdAction'] = 0
    keys_dim['ct'] = 5
    keys_dim['os'] = 3
    keys_dim['carrier'] = 4
    keys_dim['house'] = 1     

split_train()
