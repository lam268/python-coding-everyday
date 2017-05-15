#! /usr/local/bin python3
# -*- coding: utf-8 -*-
"""
	Description:
		In this assignment you are given a number and have to make it negative
		.But maybe the number is already negative?

		The number can be already negative, in which case no change is required.
		zero(0) can not be negative.

	Example:
		make_negative(1);  # return -1
		make_negative(-5); # return -5
		make_negative(0);  # return 0

    Author:
    	yangxw163@gmail.com

    Created:
    	11 May 2017
"""	
def make_negative(number):
	return -number if number > 0 else number

if __name__ == '__main__':
	main()