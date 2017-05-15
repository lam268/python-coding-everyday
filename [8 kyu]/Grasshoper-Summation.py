#! /usr/local/bin python3
# -*- coding: utf-8 -*-
"""
	Description:
		write a function that finds the summation of every number between 1 and num. 
		The number will always be a positive integer greater than 0

	Example:
		summation(2) -> 3
		1 + 2

		summation(8) -> 36
		1 + 2 + 3 + 4 + 5 + 6 + 7 + 8

    Author:
    	yangxw163@gmail.com

    Created:
    	11 May 2017
"""	
def summation(num):
	return sum (i for i in range(0, num + 1))

if __name__ == '__main__':
	print(summation(1))
	print(min([-52, 56, 30, 29, -54, 0, -110]))