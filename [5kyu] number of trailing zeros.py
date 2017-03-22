#! /usr/local/bin python3
# -*- coding: utf-8 -*-
"""
	Description:
		Write a program that will calculate the number of trailing 
		zeros in a factorial of a given number.

		N! = 1 * 2 * 3 * 4 ... N

		zeros(12) = 2 # 1 * 2 * 3 .. 12 = 479001600 
		that has 2 trailing zeros 4790016(00)
		Be careful 1000! has length of 2568 digital numbers.

    Args:
        n (int)

    Author:

    	yangxw163@gmail.com

    Created:

    	9 March 2017
"""

def zeros(n):
	num = 0
	i = 5
	while i <= n:
		num += n / i
		i = i * 5

	return int(num)


if __name__ == '__main__':
	print(zeros(30))