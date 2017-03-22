#! /usr/local/bin python3 
# -*- coding: utf-8 -*-
"""
	Description: 
		Bob is preparing to pass IQ test. The most frequent task in this 
		test is to find out which one of the given numbers differs from the others. 
		Bob observed that one number usually differs from the others in evenness. 
		Help Bob — to check his answers, he needs a program that among 
		the given numbers finds one that is different in evenness, 
		and return a position of this number.

		! Keep in mind that your task is to help Bob solve a real IQ test, 
		which means indexes of the elements start from 1 (not 0)

	Examples :

		iq_test("2 4 7 8 10") => 3 // Third number is odd, while the rest of the numbers are even

		iq_test("1 2 1 1") => 2 // Second number is even, while the rest of the numbers are odd

    Args:
        numbers (int)

    Author: 

    	yangxw163@gmail.com
        
    Created:

    	7 March 2017
"""

def iq_test(numbers):
	odd_result, even_reslut = [], []
	numbers_split = numbers.split()
	for i in range(len(numbers_split)):
		if int(numbers_split[i]) % 2 == 0:
			even_reslut.append(i)
		else:
			odd_result.append(i)
	return odd_result[0] + 1 if len(odd_result) == 1 else even_reslut[0] + 1

if __name__ == '__main__':
	print(iq_test('2 4 7 8 10'))