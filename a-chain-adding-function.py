#! /usr/local/bin python3 
# -*- coding: utf-8 -*-
"""
	Description: 
		We want to create a function 
		that will add numbers together when called in succession.

		add(1)(2); // returns 3
		add(1)(2)(3); // 6
		add(1)(2)(3)(4); // 10
		add(1)(2)(3)(4)(5); // 15

		We should be able to store the returned values and reuse them.

		var addTwo = add(2);
		addTwo // 2
		addTwo + 5 // 7
		addTwo(3) // 5
		addTwo(3)(5) // 10

    Args:
        number (int)

    Author: 

    	yangxw163@gmail.com
        
    Created:

    	26 Ferbary 2017
"""

class add(int):
	def __call__(self, n):
		return add(self + n)

if __name__ == '__main__':
	print(add(1))
	# print(result)

