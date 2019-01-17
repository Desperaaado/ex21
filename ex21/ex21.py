from random import randint
import sys
sys.path.append('C:/Users/xiao0/projects_pro')
from ex14.ex14.ex14 import *
from ex16.ex16.ex16 import *


length = 20

def ordered_list():
    a_list = []
    for i in range(0, length):
        a_list.append(randint(0, 99))

    a_list.sort()
    return a_list

def bs_list(num, a_ordered_list):
    length = len(a_ordered_list)
    if length == 1:
        return a_ordered_list[0] == num and num or None

    mid = length // 2
    if a_ordered_list[mid] == num:
        return num
    elif a_ordered_list[mid] > num:
        return bs_list(num, a_ordered_list[:mid])
    else:

        try:
            a_ordered_list[mid+1]
            return bs_list(num, a_ordered_list[mid+1:])
        except IndexError:
            return None

def ordered_dllist():
    a_dllist = DLList()
    for i in range(0, length):
        value = randint(0, 99)
        a_dllist.push(value)
    quick_sort(a_dllist)
    return a_dllist

def bs_dllist(num, a_ordered_dllist):
    length = a_ordered_dllist.count()
    return _bs_dllist(num, a_ordered_dllist, 0, length - 1)

def _bs_dllist(num, a_ordered_dllist, start ,end):
    # contain start & end
    length = end - start + 1
    if length == 1:
        value = a_ordered_dllist.find_by_index(start).value
        return value == num and num or None

    mid = (start + end) // 2
    mid_value = a_ordered_dllist.find_by_index(mid).value
    if mid_value == num:
        return num
    elif mid_value > num:

        if start <= mid - 1:
            return _bs_dllist(num, a_ordered_dllist, start, mid-1)
        else:
            return None

    else:

        if mid + 1 <= end:
            return _bs_dllist(num, a_ordered_dllist, mid+1, end)
        else:
            return None
