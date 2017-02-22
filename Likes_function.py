#! /usr/local/bin python3 
# -*- coding: utf-8 -*-
#  Author:			xiaowei yang
#  Created:         22 Ferbary 2017
#  Email:           yangxw163@gmail.com

#Functions Instructions

# You probably know the "like" system from Facebook and other pages. 
# People can "like" blog posts, pictures or other items. 
# We want to create the text that should be displayed next to such an item.

# Implement a function likes :: [String] -> String, 
# which must take in input array, containing the names of people who like an item. 
# It must return the display text as shown in the examples:

# likes [] // must be "no one likes this"
# likes ["Peter"] // must be "Peter likes this"
# likes ["Jacob", "Alex"] // must be "Jacob and Alex like this"
# likes ["Max", "John", "Mark"] // must be "Max, John and Mark like this"
# likes ["Alex", "Jacob", "Mark", "Max"] // must be "Alex, Jacob and 2 others like this"

def likes1(names):
	left_count = 0
	len_args = len(names)

	if not isinstance(names, list):
		return 'bad value'
	else:
		if len_args == 0:
			return 'no one likes this'
		elif len_args == 1:
			return '{names[0]} likes this'.format(names = names)
		elif len_args > 1 and len_args < 3:
			return '{names[0]} and {names[1]} like this'.format(names = names)
		elif len_args == 3:
			return '{names[0]}, {names[1]} and {names[2]} like this'.format(names = names)
		else:
			left_count = len_args - 2
			return '{names[0]}, {names[1]} and {left_count} other like this'.format(names = names, left_count = left_count)

#优雅实现
def likes(names):
	n = len(names)
	return {
		0: 'no one likes this',
		1: '{} likes this',
		2: '{} and {} like this',
		3: '{}, {} and {} like this',
		4: '{}, {} and {left_count} other like this'
	}[min(n, 4)].format(*names, left_count = n - 2)

if __name__ == '__main__':
	print(likes([])) 
	print(likes(["Peter"]))
	print(likes (["Jacob", "Alex"]))
	print(likes (["Max", "John", "Mark"]))
	print(likes (["Alex", "Jacob", "Mark", "Max"]))
	print(likes (["Alex", "Jacob", "Mark", "Max", "yangxw"]))
