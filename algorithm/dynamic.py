# -*- coding: utf-8 -*-
'''
def print_dict(dict=None):
	for key in dict.keys():
		print str(key) + ": " + str(dict[key])

money = 199

coin_label = [1,5,3,]
max_coin_num = money/min(coin_label)
min_coin_num = money/max(coin_label)

dict_coin = {}
for per in coin_label:
	dict_coin.update({per:0})

sum_coin = 0
coin_label.sort()
print coin_label
for i in range(min_coin_num,0,-1):
	yu = money - i*coin_label[-1]
    if yu == 0:
        dict_coin[coin_label[-1]] += 1
        print_dict(dict=dict_coin)
        break
    else:
        pass

'''