from random import randint
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


