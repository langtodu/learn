# -*- coding: utf-8 -*-

def fun(x=1, **kwargs):
    print x
    # print args
    print kwargs

if __name__ == '__main__':
    fun(2, yy=9)
    print "***************************"
    source_list = []
    for i in range(4):
        source_list.append(i)
    last_index = 0
    delete_length = 2
    delete_index = delete_length-last_index
    while source_list and (delete_index < len(source_list)):
        deleting_list = []
        source_list_length = len(source_list)
        while delete_index < source_list_length:
            deleting_list.append(delete_index)
            delete_index += 2
        delete_index = delete_index - (source_list_length - 1)
        print deleting_list
        print source_list
        print delete_index
        deleting_list.sort(reverse=True)
        last_num = source_list[deleting_list[0]]
        for i in deleting_list:
            source_list.pop(i)
    print last_num

