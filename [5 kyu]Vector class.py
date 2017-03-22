#! /usr/local/bin python3
# -*- coding: utf-8 -*-
"""
	Description:
		Create a Vector object that supports addition, subtraction, 
		dot products, and norms. So, for example:

		a = Vector([1,2,3])
		b = Vector([3,4,5])
		c = Vector([5,6,7,8])
		a.add(b) # should return Vector([4,6,8])
		a.subtract(b) # should return Vector([-2,-2,-2])
		a.dot(b) # should return 1*3+2*4+3*5 = 26
		a.norm() # should return sqrt(1^2+2^2+3^2)=sqrt(14)
		a.add(c) # raises an exception
		If you try to add, subtract, or dot two vectors with different lengths, 
		you must throw an error!

	Also provide:

		a toString function, so that using the vectors from above, 
		a.toString() === '(1,2,3)' (in Python, this is a __str__ method, 
		so that str(a) == '(1,2,3)')
		an equals function, so that two vectors who have the same components 
		are equal
		The test cases will utilize the user-provided equals method.

    Args:
        class
    Author:

    	yangxw163@gmail.com

    Created:

    	13 March 2017
"""
from functools import reduce

class Vector:
	"""docstring for Vector"""
	def __init__(self, data):
		self._valueList = data
	
	@property
	def valueList(self):
		return self._valueList

	@valueList.setter
	def valueList(self, lst):
		if not isinstance(lst, list):
			return ValueError()
		self._valueList = lst

	def check_parameter(f):
		def wrapper(self, vector):
			if not isinstance(vector, Vector):
				return ValueError()
			if len(self._valueList) != len(vector._valueList):
				return ValueError()
			return f(self, vector)
		return wrapper

	@check_parameter
	def add(self, vector):
		return Vector(map(lambda x, y: x + y, self._valueList, vector._valueList))

	@check_parameter
	def subtract(self, vector):
		return Vector(map(lambda x, y: x - y, self._valueList, vector._valueList))
	
	@check_parameter
	def dot(self, vector):
		return reduce(lambda x, y: x + y ,map(lambda x, y: x * y, self._valueList, vector._valueList))
	
	def norm(self):
		return (sum(i**2 for i in self._valueList))**0.5

	@check_parameter
	def equals(self, vector):
		for i in range(len(self._valueList)):
			if self._valueList[i] != vector._valueList[i]:
				return ValueError()
		return True

	def __str__(self):
		return ''.join(str(tuple(self._valueList)).split())


if __name__ == '__main__':
	a = Vector([1,2,3])
	b = Vector([3,4,5])
	print(a.add(b))
	print(a.subtract(b))
	print(a.dot(b))