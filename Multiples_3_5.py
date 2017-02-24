#! /usr/local/bin python3 
# -*- coding: utf-8 -*-
"""
	Description: 
		If we list all the natural numbers below 10 that are multiples of 3 or 5, 
        we get 3, 5, 6 and 9. The sum of these multiples is 23.

        This function returns the sum of all the multiples of 3 or 5
        below the number passed in
        
        Note: If the number is a multiple of both 3 and 5, only count it once.

    Args:
        number (int)

    Author: 

    	yangxw163@gmail.com
        
    Created:
    	24 Ferbary 2017
"""

def solution(number):

    mul_sum = sum(set(i for i in range(1, number) if i % 3 == 0 or i % 5 == 0))

    return mul_sum

if __name__ == '__main__':
    print(list(i for i in range(1, 22) if i % 3 == 0 or i % 5 == 0))