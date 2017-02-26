#! /usr/local/bin python3 
# -*- coding: utf-8 -*-
"""
	Description: 
		Return the number (count) of vowels in the given string.

    Args:
        inputStr (str)

    Return:
        int: numbers os vowels

    Author: 

    	yangxw163@gmail.com
    Created:
    
    	22 Ferbary 2017
"""

def getCount1(inputStr):
    num_vowels = 0
    if not isinstance(inputStr, str):
    	return 'not a string'

    num_vowels = len(list(filter(lambda x : x in ['a','e','i','o','u'], inputStr)))
    return num_vowels

"""
	更加优雅的方式
"""

def getCount(inputStr):
	return sum(1 for i in inputStr if i in "aeiouAEIOU")

if __name__ == '__main__':
	print(getCount("abracadabra"))

	
