#! /usr/local/bin python3
# -*- coding: utf-8 -*-
"""
	Description:
		Remove the spaces from the string, then return the resultant string.
    Author:
    	yangxw163@gmail.com

    Created:
    	15 May 2017
"""
def no_space(string):
	return ''.join([i for i in string if i != ' '])