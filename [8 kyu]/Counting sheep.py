#! /usr/local/bin python3
# -*- coding: utf-8 -*-
"""
	Description:
		Consider an array of sheep where some sheep may be missing from their place.
		We need a function that counts the number of sheep present in the array

	Example:
		[True,  True,  True,  False,
  		 True,  True,  True,  True ,
  		 True,  False, True,  False,
  		 True,  False, False, True ,
  		 True,  True,  True,  True ,
  		 False, False, True,  True]

    Author:
    	yangxw163@gmail.com

    Created:
    	9 May 2017
"""	
def count_sheeps(arrayOfSheeps):
	return sum(i for i in arrayOfSheeps if i)

if __name__ == '__main__':
	