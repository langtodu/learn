# -*- coding: utf-8 -*-

def search_max(data_list=[]):
    val = max(data_list)
    return val



def solution1(data_list=[], st_num=None, select_st_num=0, interval=0):
    val = 1
    if (len(data_list) != st_num) or data_list:
        print len(data_list)
        print st_num
        print "input error"
        return val
    else:
        if (select_st_num == 0) or (interval == 0):
            pass
        elif (select_st_num > st_num) or (interval < 0):
            print "select number error!"
        else:
            if select_st_num > 0:
                max_val = max(data_list)
                print max_val
                max_index = data_list.index(max_val)
                new_list = data_list[max(0, max_index-interval):min(st_num, max_index+interval)]
                new_list.remove(max_val)
                print new_list
                select_st_num -= 1
                return max_val*solution1(data_list=new_list, st_num=len(new_list), select_st_num=1, interval=interval)
def solution(data_list=[], st_num=0, select_st_num=0, interval=None):
    val = 1
    if (len(data_list) != st_num) or (interval <= 0):
        print "input error"
        return 0
    elif (len(data_list) == 0) and (select_st_num > 0):
        return 0
    else:
        if select_st_num > 0:
            max_val = max(data_list)
            max_index = data_list.index(max_val)
            new_list = data_list[max(0, max_index-interval):min(st_num, max_index+interval)]
            new_list.remove(max_val)
            select_st_num -= 1
            return max_val*solution(data_list=new_list, st_num=len(new_list), select_st_num=select_st_num, interval=interval)
        else:
            return val
if __name__ == '__main__':
    stu_list = [7,4,7]
    print solution(data_list=stu_list, st_num=3, select_st_num=2, interval=50)
    print solution(data_list=[29], st_num=1, select_st_num=1, interval=13)
