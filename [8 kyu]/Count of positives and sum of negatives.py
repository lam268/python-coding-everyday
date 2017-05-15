#! /usr/local/bin python3
# -*- coding: utf-8 -*-
"""
	Description:
		Given an array of integers. Return an array where the first element
		is the count of positives numbers and the second element is sum of 
		negatives numbers

		If the input array is empty or null, return an empty array.

	Example:
		input [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15]
		return [10, -65].

    Author:
    	yangxw163@gmail.com

    Created:
    	11 May 2017
"""	
def count_positives_sum_negatives(arr):
	result = [0,0]
	if not arr: return []
	for i in arr:
		if i > 0:
			result[0] = result[0] + 1
		else:
			result[1] = result[1] + i
	return result

if __name__ == '__main__':
	