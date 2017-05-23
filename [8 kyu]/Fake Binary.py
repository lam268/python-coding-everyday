#! /usr/local/bin python3
# -*- coding: utf-8 -*-
"""
	Description:
		Given a string of digits, you should replace any digit below 5 with '0' 
		and any digit 5 and above with '1'.

    Author:
    	yangxw163@gmail.com

    Created:
    	15 May 2017
"""


def fake_bin(x):
    result = ''
    for i in x:
        if int(i) < 5:
            result = result + '0'
        else:
        	result = result + '1'
    return result


def to_alternating_case(s):
    # your code here
    return ''.join([i.lower() if i.isupper() else i.upper() for i in s])


def sort_priority(values, group):
	def helper(x):
		if x in group:
			print((0, x))
			return (0, x)
		return (1, x)
	values.sort(key = helper)

if __name__ == '__main__':
    # s = "HeLLo WoRLD"
    # print(to_alternating_case(s))

    group = {2, 3, 5, 7}
    numbers = [8, 3, 1, 2, 5, 4, 7, 6]
    # sort_priority(numbers, group)
    print([(0,3),(1,3)].sort())
