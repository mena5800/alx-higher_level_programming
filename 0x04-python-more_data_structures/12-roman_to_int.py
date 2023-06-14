#!/usr/bin/python3
def roman_to_int(roman_string):
    my_dict = {"M":1000,"D":500,"C":100,"L":50,"X":10,"V":5,"I":1}
    sum = 0
    for i in range(len(roman_string)):
        if (my_dict[roman_number[i]] < my_dict[roman_number[i+1]]):
            sum += my_dict[rom]
        sum += my_dict[]
    
    return sum

roman_number = "X"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "VII"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "IX"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "LXXXVII"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "DCCVII"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))
