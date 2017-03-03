#! /usr/local/bin python3 
# -*- coding: utf-8 -*-
"""
You are to write a program that takes a list of strings 
containing integers and words and returns a sorted version of the list. 
The output should maintain the positions of strings and 
numbers as they appeared in the original string (See example 4 below).

The goal is to sort this list in such a way 
that all words are in alphabetical order and 
all integers are in numerical order. Furthermore, 
if the nth element in the list is an integer it must
remain an integer, and if it is a word it must remain a word.


Input:
------

The input will contain a single, possibly empty, 
line containing a space-separated list of strings to be sorted. 
Words will not contain spaces, will contain only the lower-case letters a-z.  
Integers will be in the range -999999 to 999999, inclusive. 
The line will be at most 1000
characters long.


Output:
-------

The program must output the list of strings, 
sorted per the requirements above. 
Strings must be separated by a single space, 
with no leading space at the beginning of the line or 
trailing space at the end of the line.


Constraints:
------------

The code you submit must take input from stdin and 
produce output to stdout as specified above. 
No other output is permitted. You can assume the input will be valid. 
Feel free to use standard libraries to assist in sorting.

In the examples below, the text "Input:" and "Output:" are not part of the output, 
and neither are the blank lines.


Example 1:
----------
Input:

1

Output:

1


Example 2:
----------
Input:

car truck bus

Output:

bus car truck


Example 3:
----------
Input:

8 4 6 1 -2 9 5

Output:

-2 1 4 5 6 8 9


Example 4:
----------
Input:

car truck 8 4 bus 6 1

Output:

bus car 1 4 truck 6 8
"""

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
