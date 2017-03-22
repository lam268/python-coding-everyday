#! /usr/local/bin python3
# -*- coding: utf-8 -*-
"""
	Description:
		The maximum sum subarry problem consists in finding the maximum
		sum of a contiguous subsequences in an array or list of intergers

		maxSequence([-2, 1, -3, 4, -1, 2, 1, -5, 4])
		# should be 6: [4, -1, 2, 1]

		Easy case is when the list is made up only positive numbers and the
		maximum is the whole list. If the list is made up negative numbers
		return 0 instead

		Empty list is considered to have zero greatest sum. 
		Note that the empty list or array is a valid sublist/subarry

    Args:
        arr (list)

    Author:

    	yangxw163@gmail.com

    Created:

    	7 March 2017
"""
def maxSequence(arr):
	if len(arr) == 0:
		return 0
	sum_value, max_value = 0, arr[0]

	for i in range(len(arr)):
		sum_value += arr[i]
		if sum_value > max_value:
			max_value = sum_value
		if sum_value < 0:
			sum_value = 0

	return max_value if max_value > 0 else 0

if __name__ == '__main__':
	print(maxSequence([-2, 1, -3, 4, -1, 2, 1, -5, 4]))