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

def copy_dllist(a_dllist, start, end):
    if start == None:
        start = 0
    if end == None:
        end = a_dllist.count() - 1
    a_copy = DLList()
    a_copy.begin = a_dllist.find_by_index(start)
    a_copy.begin.prev = None
    a_copy.end = a_dllist.find_by_index(end)
    a_copy.end.next = None
    return a_copy

def bs_dllist(num, a_ordered_dllist):
    length = a_ordered_dllist.count()
    if length == 1:
        return a_ordered_dllist.begin.value == num and num or None

    mid = length // 2
    mid_value = a_ordered_dllist.find_by_index(mid).value
    if mid_value == num:
        return num
    elif mid_value > num:

        return bs_dllist(num, copy_dllist(a_ordered_dllist, None, mid-1))
    else:

        if a_ordered_dllist.find_by_index(mid+1):
            return bs_dllist(num, copy_dllist(a_ordered_dllist, mid+1, None))
        else:
            return None
