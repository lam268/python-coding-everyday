#! /usr/local/bin python3
# -*- coding: utf-8 -*-
"""
	Description:
		very simple, given a number, find its opposite
		But need you do it in one line of code and without any conditionals

	Example:
		1: -1
		14: -14
	   -34: 34

    Author:
    	yangxw163@gmail.com

    Created:
    	9 May 2017
"""

def digitize(n):
	return list(map(int,str(n)[::-1]))

if __name__ == '__main__':
	print(digitize(35231))

