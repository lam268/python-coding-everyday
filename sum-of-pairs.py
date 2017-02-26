#! /usr/local/bin python3 
# -*- coding: utf-8 -*-
"""
	Description: 
		Given a list of integers and a single sum value, 
		return the first two values (parse from the left please) 
		in order of appearance that add up to form the sum.

    Args:
		ints (list), s (int)
	
	Examples:
		sum_pairs([11, 3, 7, 5],         10)
		#              ^--^      3 + 7 = 10
		== [3, 7]

		sum_pairs([4, 3, 2, 3, 4],         6)
		#          ^-----^         4 + 2 = 6, indices: 0, 2 *
		#             ^-----^      3 + 3 = 6, indices: 1, 3
		#                ^-----^   2 + 4 = 6, indices: 2, 4
		#  * entire pair is earlier, and therefore is the correct answer
		== [4, 2]

		sum_pairs([0, 0, -2, 3], 2)
		#  there are no pairs of values that can be added to produce 2.
		== None/nil/undefined (Based on the language)

		sum_pairs([10, 5, 2, 3, 7, 5],         10)
		#              ^-----------^   5 + 5 = 10, indices: 1, 5
		#                    ^--^      3 + 7 = 10, indices: 3, 4 *
		#  * entire pair is earlier, and therefore is the correct answer
		== [3, 7]

    Author: 
    	yangxw163@gmail.com
        
    Created:
    	25 Ferbary 2017
"""

"""
	解题思路：
		成功的pairs(x,y)放在dist中，x: ints[i], y: index of ints[y] 
		循环列表一次，判断每个值是否已在dist中
"""

def sum_pairs(ints, s):
	temp = {ints[0]:len(ints)} 
	resutl = [ints[0],len(ints)]

	for i in range(1, len(ints)):
		if s-ints[i] in temp:
			temp[s-ints[i]] = i
			if resutl[1] > i:
				resutl = [s-ints[i],i] 
		else:
			temp[ints[i]] = len(ints)
	if resutl[1] != len(ints):
		return [resutl[0], ints[resutl[1]]]
	else:
		return None

if __name__ == '__main__':
	l1= [1, 4, 8, 7, 3, 15]
	l2 = [20, -13, 40]
	l3 = [1, 2, 3, 4, 1, 0] 

	print(sum_pairs(l1, 2))
	# print(l4.keys()[0].keys())