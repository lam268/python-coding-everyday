#! /usr/local/bin python3 
# -*- coding: utf-8 -*-
"""
	Description: 
		Write a function called validBraces that takes a string of braces, 
		and determines if the order of the braces is valid. 
		validBraces should return true if the string is valid, 
		and false if it's invalid.

		All input strings will be nonempty, 
		and will only consist of open parentheses '(' , closed parentheses ')', 
		open brackets '[', closed brackets ']', 
		open curly braces '{' and closed curly braces '}'.

    Args:
        braces (str)

    Author: 

    	yangxw163@gmail.com
        
    Created:

    	24 Ferbary 2017

    Examples:
    '(){}[]' and '([{}])' would be considered valid, 
    while '(}', '[(])', and '[({})](]' would be considered invalid.
"""

def validBraces(string):
	result = []
	for i in range(0,len(string)):
		if string[i] == '(' or string[i] == '{'  or string[i] == '[':
			result.append(string[i])
		else:
			if len(result) == 0:
				return False
			lastOpenParenthesis = result.pop()
			if (string[i] == ')' and lastOpenParenthesis != '(') or (string[i] == '}' and lastOpenParenthesis != '{') or (string[i] == ']' and lastOpenParenthesis != '['):
				return False
	if len(result) == 0:
		return True
	else:
		return False

if __name__ == '__main__':
	s = '(((({{'
	print(validBraces(s))
	
		
	