#! /usr/local/bin python3
# -*- coding: utf-8 -*-
"""
	Description:
		Your task is to make two functions, max and min that takes an
		array of integers list as inputs, the largest and lowest number
		in that array

	Example:
		max([4,6,2,1,9,63,-134,566]) returns 566
		min([-52, 56, 30, 29, -54, 0, -110]) returns -110
		max([5]) returns 5
		min([42, 54, 65, 87, 0]) returns 0

    Author:
    	yangxw163@gmail.com

    Created:
    	11 May 2017
"""	
def min(arr):
	t = arr[0]
	for i in arr:
		if i < t:
			t = i
	return t

def max(arr):
	t = arr[0]
	for i in arr:
		if i > t:
			t = i
	return t
