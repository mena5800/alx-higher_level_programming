#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    """
    returns a set of all elements present in only one set.

    Args:
        set_1 (set): first set
        set_2 (set): second set
    
    Return:
        a set of all elements present in only one set.
    """
    items = set()
    for item in set_1:
        if (item not in set_2):
            items.add(item)
            
    for item in set_2:
        if (item not in set_1):
            items.add(item)

    return items

set_1 = { "Python", "C", "Javascript" }
set_2 = { "Bash", "C", "Ruby", "Perl" }
od_set = only_diff_elements(set_1, set_2)
print(sorted(list(od_set)))
