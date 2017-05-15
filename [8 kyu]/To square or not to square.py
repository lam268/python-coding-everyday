#! /usr/local/bin python3
# -*- coding: utf-8 -*-
"""
	Description:
		Write a function, that will get an integer array as its parameters and will
		process every number from this array.

		Retrun a new array with processing every number of the input-array like this:

		If the number has an integer square root, take this, otherwise square the number.

		[4,3,9,7,2,1] -> [2,9,3,49,4,1]

		The input array will always contaion only positive number and will never be empty
		or null

    Author:
    	yangxw163@gmail.com

    Created:
    	11 May 2017
"""	

def square_or_square_root(arr):
	result = []
	for item in arr:
		if pow(item, 0.5) / 1:
			result.append(int(pow(item, 0.5)))
		else:
			result.append(item * item)
	return result
if __name__ == '__main__':
	print(pow(9, 0.5))