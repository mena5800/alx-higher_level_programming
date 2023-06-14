#!/usr/bin/python3
def roman_to_int(roman_string):
    '''
    function to convert roman numbers to normal numbers.

    Args:
        roman_string(str): roman numbers
    Return:
        normal number of roman numbers
    '''
    my_dict = {"M": 1000, "D": 500, "C": 100, "L": 50, "X": 10, "V": 5, "I": 1}
    sum = 0
    if (type(roman_string) != str or roman_string is None):
        return sum

    for i in range(len(roman_string)):
        if (i != len(roman_string) - 1 and
                my_dict[roman_string[i]] < my_dict[roman_string[i + 1]]):
            sum -= my_dict[roman_string[i]]
        else:
            sum += my_dict[roman_string[i]]

    return sum
