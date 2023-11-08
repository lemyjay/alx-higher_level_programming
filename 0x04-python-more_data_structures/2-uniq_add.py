#!/usr/bin/python3

def uniq_add(my_list=[]):
    dup = my_list.copy()
    dup.sort()
    temp =[]
    temp.append(dup[0])
    for i in range(1, len(dup)):
        if dup[i] > dup[i - 1]:
            temp.append(dup[i])
    total = 0
    for a in temp:
        total += a
    return total
