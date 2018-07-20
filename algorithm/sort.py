# -*- coding: utf-8 -*-

# 升序排列，直接插入排序，稳定算法，空间复杂度O(1)，时间复杂度O(n**2)
def InsertSort(sort_list=None):
    length = len(sort_list)
    for i in range(1,length):
        for k in range(i,0,-1):
            if sort_list[k] < sort_list[k-1]:
                sort_list.insert(k-1, sort_list.pop(k))
                # sort_list[k], sort_list[k-1] = sort_list[k-1], sort_list[k] # 与上条语句功能相同
            else:
                break
# 升序排列，冒泡排序，稳定算法，空间复杂度O(1)，时间复杂度O(n**2)
def BubbleSort(sort_list=None):

    length = len(sort_list)
    for i in range(1, length):
        flag = False
        for k in range(length-i):
            if sort_list[k] > sort_list[k+1]:
                sort_list[k+1], sort_list[k] = sort_list[k], sort_list[k+1]
                flag = True
        if flag == False:
            break
# 升序排列，快速排序，不稳定算法，平均空间复杂度O(logN)，最坏空间复杂度O(N)；平均时间复杂度O(NlogN)，最坏的时间复杂度O(N**2)
def QuickSort(sort_list=None, low=0, high=0):
    if low < high:
        temp = sort_list[low]
        flag = False
        while low < high:
            k = high
            while (k >= 0) and (k > low):
                if sort_list[k] < temp:
                    sort_list[low] = sort_list[k]
                    high = k
                k -= 1
            i = low
            while (i >= 0) and (i < high):
                if sort_list[i] > temp:
                    sort_list[high] = sort_list[i]
                    low = i
                i += 1
            low += 1
            high -= 1
        sort_list[low] = temp
        print sort_list
        QuickSort(sort_list, low=0, high=low-1)
        QuickSort(sort_list, low=low+1, high=len(sort_list))
    # return sort_list


if __name__ == '__main__':
    ll = [9, 8, 7, 6, 1, 2, 3]
    # print InsertSort(sort_list=ll)
    print ll
    # BubbleSort(ll)
    # print ll
    QuickSort(ll, low=0, high=6)


