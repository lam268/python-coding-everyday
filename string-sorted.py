#! /usr/local/bin python3 
# -*- coding: utf-8 -*-
from sys import stdin, stdout

def is_num(num):  
    try:  
        int(num)  
        return True  
    except ValueError: 
        return False 

def string_sorted(s):

	s_sorted = sorted(s)
	digit_index, str_index = 0, sum(1 for item in s if is_num(item))

	for i in range(len(s)):
		if is_num(s[i]):
			s[i] = s_sorted[digit_index]
			digit_index = digit_index + 1
		else:
			s[i] = s_sorted[str_index]
			str_index = str_index + 1

	return ' '.join(s)

if __name__ == '__main__':

	line = stdin.readline()
	stdout.writelines(string_sorted(line.split(' ')))
