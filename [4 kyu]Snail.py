#! /usr/local/bin python3
# -*- coding: utf-8 -*-
"""
	Description:
		Snail Sort

		Given an n x n array, return the array elements arranged from 
		outermost elements to the middle element, traveling clockwise.

		array = [[1,2,3],
         		[4,5,6],
         		[7,8,9]]
		snail(array) #=> [1,2,3,6,9,8,7,4,5]
		For better understanding, please follow the numbers of the next 
		array consecutively:

		array = [[1,2,3],
		         [8,9,4],
		         [7,6,5]]
		snail(array) #=> [1,2,3,4,5,6,7,8,9]
		This image will illustrate things more clearly:



		NOTE: The idea is not sort the elements from the lowest value 
		to the highest; the idea is to traverse the 2-d array in a clockwise 
		snailshell pattern.

		NOTE 2: The 0x0 (empty matrix) is represented as [[]]

    Args:
        array (array)

    Author:
    	yangxw163@gmail.com

    Created:

    	14 March 2017
"""

def snail(array):
	if not array:
	 	return [[]]

	return list(array[0]) + snail(list(zip(*array[1:]))[::-1]) if len(array) > 1 else list(array[0])

if __name__ == '__main__':
	a = [[1,2,3],
		 [8,9,4],
		 [7,6,5]]
	
	c = [4,5]
	d = []
	
	print(snail(a))
	# print(list(zip(*d[1:]))[::-1])
	# print(type(list(zip(*a[1:]))[::-1][0]))
