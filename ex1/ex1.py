#!/usr/bin/env python3

import sys


def get_arg():
    my_list = []
    for line in sys.stdin:
        # Split the line into individual values
        values = line.strip().split()
        my_list.append(values)
    # Process the values as needed
    # print("Processing:", values)
    # print("my_list:", my_list)
    return my_list


def see_less(my_list):
    name_first = my_list[0][0]
    f_first = my_list[0][1]
    p_first = my_list[0][2]
    r_first = my_list[0][3]
    name_second = my_list[1][0]
    f_second = my_list[1][1]
    p_second = my_list[1][2]
    r_second = my_list[1][3]
    tmp_number_first = int(p_first) + int(r_first)
    tmp_number_second = int(p_second) + int(r_second)
    number_first = int(f_first) * tmp_number_first
    number_second = int(f_second) * tmp_number_second
    if number_first < number_second:
        print(name_first)
    elif number_first > number_second:
        print(name_second)
    else:
        print("Tie")


if __name__ == '__main__':
    the_list = get_arg()
    see_less(the_list)
