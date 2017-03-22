#! /usr/local/bin python3
# -*- coding: utf-8 -*-
"""
	Description:
		Write a function called validParentheses that takes a string of parentheses, 
		and determines if the order of the parentheses is valid. 
		validParentheses should return true if the string is valid, 
		and false if it's invalid.

	Examples: 
		validParentheses( "()" ) => returns true 
		validParentheses( ")(()))" ) => returns false 
		validalidParentheses( "(" ) => returns false 
		validParentheses( "(())((()())())" ) => returns true 

	All input strings will be nonempty, 
	and will only consist of open parentheses '(' and/
	or closed parentheses ')'

    Args:
        s (string)
    Author:

    	yangxw163@gmail.com

    Created:

    	13 March 2017
"""
def valid_parentheses(strg):
	result = []
	for i in range(len(strg)):
		if strg[i] == '(' or strg[i] == ')':
			if strg[i] == '(':
				result.append(strg[i])
			else:
				if len(result) == 0:
					return False
				lastParenthese = result.pop()
				if strg[i] == ')' and lastParenthese != '(':
					return False

	return True if len(result) == 0 else False




if __name__ == '__main__':
	print(valid_parentheses("  ("))
	# a = [1,2,3]
	# b = [3,5,6]
	# for i, j in a,b: 
		print(i,j)
	