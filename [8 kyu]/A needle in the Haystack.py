#! /usr/local/bin python3
# -*- coding: utf-8 -*-
"""
	Description:
		Can you find the needle in the haystack?
		Write a function findNeedle() that takes an array full of junk but 
		containing one 'needle'

		After your functions find the needle it should return a message(a string)
		that says:
			“found the needle at positon” plus the index it found the needle 

	Example:
		{ 6, 2, 1, 8, 10 } => 16
		{ 1, 1, 11, 2, 3 } => 6

    Author:
    	yangxw163@gmail.com

    Created:
    	9 May 2017
"""	
def find_needle(haystack):
	return 'found the needle at positon {index}'.format(index = haystack.index('needle'))


if __name__ == '__main__':
	print(find_needle(['hay', 'junk', 'hay', 'hay', 'moreJunk', 'needle', 'randomJunk']))