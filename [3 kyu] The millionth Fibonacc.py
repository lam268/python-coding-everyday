#! /usr/local/bin python3
# -*- coding: utf-8 -*-
"""
	Description:
		The year is 1214. One night, Pope Innocent III awakens to find
		the the archangel Gabriel floating before him.
		Gabriel thunders to the pope:

		Gather all of the learned men in Pisa, especially Leonardo Fibonacci.
		In order for the crusades in the holy lands to be successful,
		these men must calculate the millionth number in Fibonacci's recurrence.
		Fail to do this, and your armies will never reclaim the holy land.
		It is His will.

		The angel then vanishes in an explosion of white light.
		Pope Innocent III sits in his bed in awe. How much is a million?
		he thinks to himself. He never was very good at math.

		He tries writing the number down, but because everyone in Europe
		is still using Roman numerals at this moment in history,
		he cannot represent this number. If he only knew about the
		invention of zero, it might make this sort of thing easier.

		He decides to go back to bed. He consoles himself,
		The Lord would never challenge me thus;
		this must have been some deceit by the devil.
		A pretty horrendous nightmare, to be sure.

		Pope Innocent III's armies would go on to conquer Constantinople
		(now Istanbul), but they would never reclaim the holy land as he desired.

		In this kata you will have to calculate fib(n) where:

		fib(0) := 0
		fib(1) := 1
		fin(n + 2) := fib(n + 1) + fib(n)
		Write an algorithm that can handle n where 1000000 ≤ n ≤ 1500000.

		Your algorithm must output the exact integer answer,
		to full precision. Also, it must correctly handle negative numbers
		as input.

	Args:
        n (int)

    Author:
    	yangxw163@gmail.com

    Created:
    	16 March 2017
"""


def fib(n):
    v1, v2, v3 = 1, 1, 0    # initialise a matrix [[1,1],[1,0]]
    # perform fast exponentiation of the matrix (quickly raise it to the nth
    # power)
    for rec in bin(abs(n))[3:]:
        calc = v2 * v2
        v1, v2, v3 = v1 * v1 + calc, (v1 + v3) * v2, calc + v3 * v3
        if rec == '1':
            v1, v2, v3 = v1 + v2, v1, v2
    if n < 0:
        return v2 * ((-1) ** (abs(n) + 1))

    return v2 if n else 0

if __name__ == '__main__':

    print(fib(99))
