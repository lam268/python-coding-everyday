#! /usr/local/bin python3
# -*- coding: utf-8 -*-
"""
	Description:
		You get an array of numbers, return the sum of all of the positives ones.

        Example [1,-4,7,12] => 1 + 7 + 12 = 20

        Note: array may be empty, in this case return 0.
    Args:
        arr (list)

    Author:
    	yangxw163@gmail.com

    Created:
    	22 March 2017
"""	

def positive_sum(arr):
	return sum(i for i in arr if i > 0)

if __name__ == '__main__':
    a = [1,2,3,4,5]
    b = [-1,2,3,4,-5]
    print(positive_sum(b))