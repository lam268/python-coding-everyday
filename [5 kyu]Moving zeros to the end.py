# -*- coding: utf-8 -*-
"""
	Description:
		Write an algorithm that takes an array and moves all of 
		the zeros to the end, preserving the order of the other elements.

		move_zeros([false,1,0,1,2,0,1,3,"a"]) # returns[false,1,1,2,1,3,"a",0,0]

	Args:
        array (list)

    Author:
    	yangxw163@gmail.com

    Created:
    	20 March 2017
"""
def move_zeros(array):
	count = 0
	result = []
	for i in array:
		if type(i) in (int, float):
			if i:
				result.append(i)
			else:
				count += 1
		else:
			result.append(i)
	
	return result + [0] * count

if __name__ == '__main__':
	a = [9, 0.0, 0,9,1,2,0,1,0,1,0.0,3,0,1,9,0,0,0,0,9]
	b = ["a",0,0,"b","c","d",0,1,0,1,0,3,0,1,9,0,0,0,0,9]
	c = ["a",0,0,"b",None,"c","d",0,1,False,0,1,0,3,[],0,1,9,0,0,{},0,0,9]
	print(move_zeros(c))
	# print(type(False))
