#! /usr/local/bin python3
# -*- coding: utf-8 -*-
"""
	Description:
		Given a string, you have to return a string in which each character(case-
		sensitive) is repeated once

	Example:
		double_char("String") ==> "SSttrriinngg"

		double_char("Hello World") ==> "HHeelllloo  WWoorrlldd"

		double_char("1234!_ ") ==> "11223344!!__  "

    Author:
    	yangxw163@gmail.com

    Created:
    	12 May 2017
"""	
def double_char(s):
	return ''.join(list(item * 2 for item in s))

if __name__ == '__main__':
	print(double_char('string'))