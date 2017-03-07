#! /usr/local/bin python3 
# -*- coding: utf-8 -*-
"""
	Description: 
		Given an array, find the int that appears an odd number of times.

		There will always be only one integer that appears an odd number of times.

    Args:
        seq (list)

    Author: 

    	yangxw163@gmail.com
        
    Created:

    	7 March 2017
"""
def find_int(seq):
	result = list(number for number in set(seq) if seq.count(number) % 2 != 0)
	return result[0] if len(result) != 0 else None

if __name__ == '__main__':
	s = [20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5]
	print(find_int(s))
	# print(s.count(20))
