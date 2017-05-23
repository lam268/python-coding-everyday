#! /usr/local/bin python3
# -*- coding: utf-8 -*-
"""
	Description:
		You need to write a function thar reverses the words in a string.
		A word can also fit an empty string. 

		reverse('Hello World') == 'World Hello'
		reverse('Hi There.') == 'There. Hi'

    Author:
    	yangxw163@gmail.com

    Created:
    	12 May 2017
"""	

def reverse(st):
	return ' '.join(st.split(' ')[::-1])

if __name__ == '__main__':
	st = 'Hello World'
	print(len(st.split(' ')))
	print(reverse(st))