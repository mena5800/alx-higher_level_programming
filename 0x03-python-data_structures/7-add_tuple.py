#!/usr/bin/python3
def clean_tuple(tup=()):
    if len(tup) == 0:
        return (0, 0)
    elif len(tup) == 1:
        return (tup[0], 0)
    else:
        return tup


def add_tuple(tuple_a=(), tuple_b=()):
    tuple_a = clean_tuple(tuple_a)
    tuple_b = clean_tuple(tuple_b)
    tuple_c = (tuple_a[0]+tuple_b[0], tuple_a[1]+tuple_b[1])
    return tuple_c
