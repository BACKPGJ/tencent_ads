#!/usr/bin/python
# -*- coding: utf-8 -*-

import csv
import numpy as np
from collections import Counter
import matplotlib.pyplot as plt
import sys
import pickle as pk
#sys.path.append('../')

'''
数据统计：
总的训练样本数: 8798814
广告数总数: 173
平均每个广告样本数：50860
每个广告的正负样本比
每个广告下训练样本数
每个用户出现的广告数

用户的category特征的分布情况
    最大值，最小值，频数等
'''

# ads positive&negative distribution


def train_set_analyze():

    ads_pn = {}
    users = []
    train_num = 0
    with open('../data/preliminary_contest_data/train.csv') as f:
        reader = csv.reader(f)
        for rd in reader:
            if reader.line_num == 1:
                continue
            if rd[0] not in ads_pn:
                ads_pn[rd[0]] = []
            ads_pn[rd[0]].append(rd[-1])
            train_num += 1
            users.append(rd[1])

    print(train_num)
    print(len(ads_pn))

    '''
    训练集大小：8798814
    广告数：173
    '''

    users_counter = Counter(users)
    users_counter_list = [users_counter[uid] for uid in users_counter]

    print(len(users_counter_list))
    '''
    用户数：7883466
    '''

    print(np.min(users_counter_list))
    print(np.max(users_counter_list))
    print(np.mean(users_counter_list))

    '''
    单个用户对应最少广告数：1
    单个用户对应最多广告数：16
    平均单个用户对应广告数：1.116
    '''

    plt.figure()
    plt.plot(sorted(users_counter_list))
    plt.title("users related ads num")
    plt.xlabel("users")
    plt.ylabel("ads num")
    plt.savefig("../pngs/users_ads_num.png")

    ads_pn_counter = {}
    ads_pn_rate = {}
    rates = []
    nums = []
    for aid in ads_pn:
        ads_pn_counter[aid] = Counter(ads_pn[aid])
        ads_pn_rate[aid] = ads_pn_counter[aid]['-1']/ads_pn_counter[aid]['1']
        rates.append(ads_pn_rate[aid])
        nums.append(len(ads_pn[aid]))

    print(np.min(rates))
    print(np.max(rates))
    print(np.mean(rates))

    '''
    单个广告最小负正样本比：17.15
    单个广告最大负正样本比：21.50
    单个广告平均正负样本比：19.94
    '''

    print(np.min(nums))
    print(np.max(nums))
    print(np.mean(nums))

    '''
    单个广告对应样本数最小：6624
    单个广告对应样本数最大：553109
    单个广告对应样本数平局：50860.19
    '''

    plt.figure()
    plt.plot(sorted(rates))
    plt.title("ads negative/positive")
    plt.xlabel("ads")
    plt.ylabel("negative/positive")
    plt.savefig("../pngs/ads_pos_neg.png")

    plt.figure()
    plt.plot(sorted(nums))
    plt.title("ads sample num")
    plt.xlabel("ads")
    plt.ylabel("sample num")
    plt.savefig("../pngs/ads_sample_num.png")

    return


def user_feature_analyze():
    keys = ['uid', 'age', 'gender', 'marriageStatus', 'education', 'consumptionAbility', 'LBS',
            'interest1', 'interest2', 'interest3', 'interest4', 'interest5',
            'kw1', 'kw2', 'kw3', 'topic1', 'topic2', 'topic3', 'appIdInstall',
            'appIdAction', 'ct', 'os', 'carrier', 'house']
    users = []
    counters = {}
    k = 0
    for key in keys:
    	counters[key] = Counter()
    with open('../data/preliminary_contest_data/userFeature.data', 'r') as f:
        for l in f:
            features = l.strip().split('|')
            user = {}
            for key in keys:
                user[key] = []

            for f in features:
                f_name = f.split(' ')[0]
                for v in f.split(' ')[1:]:
                    user[f_name].append(int(v))
                    counters[f_name].update([int(v)])
            users.append(user)
            k += 1
            if k % 100000 == 0:
                print (k)
                #break
    print (len(users))
    pk.dump(counters, open("../data/counters.pkl", "wb"))
    return


def counter_analyze():
    keys = ['uid', 'age', 'gender', 'marriageStatus', 'education', 'consumptionAbility', 'LBS',
            'interest1', 'interest2', 'interest3', 'interest4', 'interest5',
            'kw1', 'kw2', 'kw3', 'topic1', 'topic2', 'topic3', 'appIdInstall',
            'appIdAction', 'ct', 'os', 'carrier', 'house']
    counters = pk.load(open("../data/counters.pkl", "rb"))
    for k in keys:
        print (k)
        wt = open("../data/features/%s.csv" % k, "w", encoding="utf-8")
        csv_writer = csv.writer(wt)
        counter_list = [(ck, counters[k][ck]) for ck in counters[k]]
        sorted_counter_list = sorted(counter_list, key=lambda x:x[0])
        if sorted_counter_list[0][0] == 0:
            print (k, "0")
        csv_writer.writerows(sorted_counter_list)
        wt.close()
    #    break
    #print (keys[12], len(counters[keys[12]]))
    return 

counter_analyze()
#user_feature_analyze()
