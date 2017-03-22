#! /usr/local/bin python3
# -*- coding: utf-8 -*-
"""
	Description:
		A perfect power is a classification of positive integers:

		In mathematics, a perfect power is a positive integer that 
		can be expressed as an integer power of another positive integer. 
		More formally, n is a perfect power if there exist natural numbers 
		m > 1, and k > 1 such that mk = n.
		Your task is to check wheter a given integer is a perfect power. 
		If it is a perfect power, return a pair m and k with mk = n as a proof. 
		Otherwise return Nothing, Nil, null, None or your language's equivalent.

		Note: For a perfect power, there might be several pairs. 
		For example 81 = 3^4 = 9^2, so (3,4) and (9,2) are valid solutions. 
		However, the tests take care of this, so if a number is a perfect power, 
		return any pair that proves it.

		Examples

		isPP(4) => [2,2]
		isPP(9) => [3,2]
		isPP(5) => None

	Args:
        n (int)

    Author:
    	yangxw163@gmail.com

    Created:
    	19 March 2017
"""
import math
def isPP(n):
	i, reslut = 2, []
	while i < n:
		if math.log(n, i) < 2:
			break
		if i ** round(math.log(n, i)) == n:
			reslut.append([i, round(math.log(n, i))])
		i += 1

	return reslut[0] if reslut else None

if __name__ == '__main__':
    print(isPP(243))
    # print(math.log(459165024,2))
    # print(125 ** (1 / 3))
    print(math.log(243, 3))
