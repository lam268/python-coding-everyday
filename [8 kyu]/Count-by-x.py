#! /usr/local/bin python3
# -*- coding: utf-8 -*-
"""
	Description:
		Create a function with two parameters that will return a list of length(n)
		with multiples of (x)

		Assume that the given number and the numbers of times to count will be positive
		numbers greater than 0

		Return the results as an array

		count_by(1,10) #should return [1,2,3,4,5,6,7,8,9,10]
		count_by(2,5) #should return [2,4,6,8,10]

    Author:
    	yangxw163@gmail.com

    Created:
    	12 May 2017
"""	
def count_by(x, n):
	retutn list( x *i for i in range(1, n + 1))

if __name__ == '__main__':
	main()