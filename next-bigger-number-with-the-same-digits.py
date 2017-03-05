#! /usr/local/bin python3 
# -*- coding: utf-8 -*-

"""
	Description: 
		You have to create a function that takes a 
		positive integer number and returns the next bigger number 
		formed by the same digits:

	Example
		next_bigger(12)==21
		next_bigger(513)==531
		next_bigger(2017)==2071

		If no bigger number can be composed using those digits, return -1:
		next_bigger(9)==-1
		next_bigger(111)==-1
		next_bigger(531)==-1
    Args:
        n (int)

    Author: 

    	yangxw163@gmail.com
        
    Created:

    	3 March 2017
"""
# 穷举
from itertools import permutations

def next_bigger1(n):
	if len(str(n)) == 1:
		return -1
	l = sorted(int(''.join(item)) for item in set(permutations(str(n), len(str(n)))))

	return -1 if l.index(n) == len(str(n)) - 1 else l[l.index(n) + 1]

def next_bigger(n):
	i = len(str(n)) - 1
	for i in range(len(str(n)) - 1, 0, -1):
		if str(n)[i] > str(n)[i - 1]:
			right_list = sorted(str(n)[i:])
			for item in range(len(right_list)):
				if str(n)[i - 1] < right_list[item]:
					temp = right_list[item]
					right_list[item] = str(n)[i - 1]
					return int(str(n)[0:i-1] + temp + ''.join(right_list))

		if str(n)[i] <= str(n)[i - 1] and i == 1:
			return -1
	
	if i == 0:
		return -1


if __name__ == '__main__':
	# print(next_bigger(144))
	s = ['1', '8','5', '4', '4']
	# print(sorted(s, key = lambda x: ))
	# print(next_bigger(551))