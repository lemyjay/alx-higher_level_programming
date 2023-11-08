#!/usr/bin/python3

def only_diff_elements(set_1, set_2):
    set_inter = set_1.intersection(set_2)
    set_join = set_1.union(set_2)
    for i in set_inter:
        if i in set_join:
            set_join.discard(i)
    return set_join
