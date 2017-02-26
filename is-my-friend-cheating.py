#! /usr/local/bin python3 
# -*- coding: utf-8 -*-
"""
	Description: 
		A friend of mine takes a sequence of numbers from 1 to n (where n > 0).
		Within that sequence, he chooses two numbers, a and b.
		He says that the product of a and b should be equal to 
		the sum of all numbers in the sequence, excluding a and b.
		Given a number n, could you tell me the numbers he excluded from the sequence?
		The function takes the parameter: 
		n (don't worry, n is always strictly greater than 0 
		and small enough so we shouldn't have overflow) and 
		returns an array of the form:
		[(a, b), ...] or [[a, b], ...] or {{a, b}, ...} or or [{a, b}, ...]
		with all (a, b) which are the possible removed numbers in the sequence 1 to n.
		[(a, b), ...] or [[a, b], ...] or {{a, b}, ...} or ...will be sorted in increasing order of the "a".

	Examples:

		removNb(26) should return [(15, 21), (21, 15)]

    Args:
        n (int)

    Author: 

    	yangxw163@gmail.com
        
    Created:

    	25 Ferbary 2017
"""

def removeNb(n):

	sum_n = sum(range(0, n + 1))
	result = []
	for i in range(1, n + 1):
		temp = (sum_n - i) / (i + 1)
		if temp % 1 == 0 and temp <= n:
			result.append((i, int(temp)))

	return sorted(result, key = lambda a : result[:][0])

if __name__ == '__main__':
	print(removeNb(26))
