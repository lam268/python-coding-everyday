#! /usr/local/bin python3
# -*- coding: utf-8 -*-
"""
	Description:
		Consider a sequence u where u is defined as follows:

		The number u(0) = 1 is the first one in u.
		For each x in u, then y = 2 * x + 1 and z = 3 * x + 1 must be in u too.
		There are no other numbers in u.
		Ex: u = [1, 3, 4, 7, 9, 10, 13, 15, 19, 21, 22, 27, ...]

		1 gives 3 and 4, then 3 gives 7 and 10, 4 gives 9 and 13, 
		then 7 gives 15 and 22 and so on...

		Task:

		Given parameter n the function dbl_linear (or dblLinear...) 
		returns the element u(n) of the ordered (with <) sequence u.

	Example:

		dbl_linear(10) should return 22

    Args:
        n (int)

    Author:
    	yangxw163@gmail.com

    Created:
    	13 March 2017
"""	
from collections import deque
def dbl_linear(n):
	queue = [1]
	x , y = 0, 0
	while len(queue) < n + 1:
		xvalue = 2 * queue[x] + 1
		yvalue = 3 * queue[y] + 1
		if xvalue < yvalue:
			if queue[-1] == xvalue:
				x += 1
				continue
			queue.append(xvalue)
			x += 1
		else:
			if queue[-1] == yvalue:
				y += 1
				continue
			queue.append(yvalue)
			y += 1

	return queue[n]

if __name__ == '__main__':
	u = [1, 3, 4, 7, 9, 10, 13, 15, 19, 21, 22, 27]
	# print(dbl_linear(10))
	# print(next(gen_linear()))
	print(dbl_linear(10))
