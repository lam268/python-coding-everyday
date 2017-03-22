#! /usr/local/bin python3
# -*- coding: utf-8 -*-
"""
	Description:
		Common denominators

		You will have a list of rationals in the form

 		[ [numer_1, denom_1] , ... [numer_n, denom_n] ]

		where all numbers are positive ints.

		You have to produce a result in the form

 		[ [N_1, D] ... [N_n, D] ]

		in which D is as small as possible and

 		N_1/D == numer_1/denom_1 ... N_n/D == numer_n,/denom_n.
		Example:

		convertFracs [(1, 2), (1, 3), (1, 4)] `shouldBe` [(6, 12), (4, 12), (3, 12)]

    Args:
        lst (list)
    Author:

    	yangxw163@gmail.com

    Created:

    	13 March 2017
"""
# 最小公倍数
def gcd1(a, b):
	if a > b:
		r = a % b
		if r:
			return gcd(b, r)
		else:
			return b
	else:
		r = b % a
		if r:
			return gcd(a, r)
		else:
			return a

from functools import reduce
from fractions import gcd

def convertFracts(lst):
	fract = int(reduce(lambda x, y: x * y/gcd(x,y), [y for x,y in lst]))
	return [[(fract//y)*x, fract] for x,y in lst]

if __name__ == '__main__':
	a = [[27115, 5262], [87546, 11111111], [43216, 255689]]
	print(convertFracts(a))

	
