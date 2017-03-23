#! /usr/local/bin python3
# -*- coding: utf-8 -*-
"""
	Description:
		This time no story, no theory. The examples below show you how to write function accum:

        Examples:

        accum("abcd")    # "A-Bb-Ccc-Dddd"
        accum("RqaEzty") # "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
        accum("cwAt")    # "C-Ww-Aaa-Tttt"
        The parameter of accum is a string which includes only letters from a..z and A..Z.

    Args:
        s (string)

    Author:
    	yangxw163@gmail.com

    Created:
    	22 March 2017
"""	
def accum(s):
    return '-'.join('{:{char}<{number}}'.format(s[i].upper(), char = s[i].lower(), number = i + 1) for i in range(len(s)))
        

if __name__ == '__main__':
    s = 'ZpglnRxqenU'
    print(accum(s))
    # print('{:{i}<{d}}'.format('Z',i = 3, d = 2))