#! /usr/local/bin python3 
# -*- coding: utf-8 -*-
"""
	Description: 
		Divisors of 42 are : 1, 2, 3, 6, 7, 14, 21, 42. 
        These divisors squared are: 1, 4, 9, 36, 49, 196, 441, 1764. 
        The sum of the squared divisors is 2500 which is 50 * 50, a square!

        Given two integers m, n (1 <= m <= n) we want to find all integers 
        between m and n whose sum of squared divisors is itself a square. 
        42 is such a number.

        The result will be an array of arrays(in C an array of Pair), 
        each subarray having two elements, 
        first the number whose squared divisors is a square and 
        then the sum of the squared divisors.

    Args:
        integers: m,n(1 <= m <= n)
    
    Examples:

        list_squared(1, 250) --> [[1, 1], [42, 2500], [246, 84100]]
        list_squared(42, 250) --> [[42, 2500], [246, 84100]]

    Author: 
    	yangxw163@gmail.com

    Created:
    	23 Ferbary 2017

"""

def list_squared(m, n):
    result = []
    for i in range(m, n + 1):
        b = 0
        # 开根方次循环
        a = sum(let * let + (i / let) * (i / let) for let in range(1, int(i ** 0.5) + 1) if i % let == 0)
        
        # 如果本身能被开根方，则减去，因为循环求和时多算了一次
        if (i ** 0.5) % 1 == 0:
            a = a - (i ** 0.5) * (i ** 0.5)

        if (a ** 0.5) % 1 == 0:
            result.append([i, int(a)])
    return result  

if __name__ == '__main__':

    examples = list_squared(1, 250)
    print(examples)

