#! /usr/local/bin python3
# -*- coding: utf-8 -*-
"""
	Description:
		Create a function that takes an integer as an argument and returns "Even" for even numbers or "Odd" for odd numbers.
	
    Args:
        number (int)

    Author:
    	yangxw163@gmail.com

    Created:
    	22 March 2017
"""	

def even_or_odd(number):
	return 'Even' if number % 2 == 0 else 'Odd'