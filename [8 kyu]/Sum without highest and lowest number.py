#! /usr/local/bin python3
# -*- coding: utf-8 -*-
"""
	Description:
		Sum all the numbers of the array expect the highest and lowest element(the value,
		not the index).The highest and lowest is respectively only one element at each edge,
		even if there are more than one value with the same value!
		
		If array is null or None,or if only one element exists, return 0

	Example:
		{ 6, 2, 1, 8, 10 } => 16
		{ 1, 1, 11, 2, 3 } => 6

    Author:
    	yangxw163@gmail.com

    Created:
    	9 May 2017
"""	

def sum_array(arr):
	if not arr:
		return 0

	return sum(arr) - min(arr) - max(arr)

if __name__ == '__main__':
	a = [6, 2, 1, 8, 10]
	b = [6, 0, 1, 10, 10]
	c = [3, 5]
	print(sum_array(c))


