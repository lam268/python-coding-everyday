#! /usr/local/bin python3
# -*- coding: utf-8 -*-
"""
	Description:
		Write a function called repeatStr which repeats the given string
		string exactly n times

	Example:
		repeatStr(6, "I") // "IIIIII"
		repeatStr(5, "Hello") // "HelloHelloHelloHelloHello"

    Author:
    	yangxw163@gmail.com

    Created:
    	11 May 2017
"""	
def repeat_str(repeat, string):
	result = ''
	for i in range(0, repeat):
		result = result + string
	return result

if __name__ == '__main__':
	print('a' * 2)