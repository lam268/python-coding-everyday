# -*- coding: utf-8 -*-
"""
	Description:
		Write function scramble(str1,str2) that returns true
		if a portion of str1 characters can be rearranged to
		match str2, otherwise returns false.

	For example:
		str1 is 'rkqodlw' and str2 is 'world' the output should
		return true.
		str1 is 'cedewaraaossoqqyt' and str2 is 'codewars' should
		return true.
		str1 is 'katas' and str2 is 'steak' should return false.

		Only lower case letters will be used (a-z). No punctuation or digits will be included.
		Performance needs to be considered

	Args:
        s1 (string), s2(string)

    Author:
    	yangxw163@gmail.com

    Created:
    	19 March 2017
"""


def scramble(s1, s2):
	i, s, j = 0, {}, 0
	while i < len(s1):
		if s1[i] in s:
			s[s1[i]] += 1
		s.setdefault(s1[i], 1)
		i = i + 1
	
	while j < len(s2):
		if s2[j] not in s:
			return False
		s[s2[j]] -= 1
		if s[s2[j]] < 0:
			return False
		j += 1
	return True


if __name__ == '__main__':
	s1 = 'rkqodlw'
	s2 = 'world'
	print(scramble(s1, s2))
	
