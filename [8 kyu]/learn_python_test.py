#! /usr/local/bin python3
# -*- coding: utf-8 -*-

class MyObject(object):
	"""docstring for MyObject"""
	def __init__(self, arg):
		super(MyObject, self).__init__()
		self.__arg = arg
		
class Screen(object):
	"""docstring for Screen"""
	def __init__(self):
		super(Screen, self).__init__()

	@property
	def width(self):
		return self._width

	@width.setter
	def width(self, value):
		self._width = value

	@property
	def height(self):
		return self._height

	@height.setter
	def height(self, value):
		self._height = value

	@property
	def resolution(self):
		return self._height * self._width

		

if __name__ == '__main__':
	foo = []

	from collections import namedtuple

	MyExpense = namedtuple('F', ['type_', 'amount'])

	# test data
	foo.append(MyExpense('food', 4))
	foo.append(MyExpense('food', 3))
	foo.append(MyExpense('car', 3))
	foo.append(MyExpense('dog', 1))


	def summarizeExpenses(min_amount, input):
	    expenses = {}
	    for expense in input:
	        if expense.amount >= min_amount:
	            if not expense.type_ in expenses:
	                expenses[expense.type_] = 0
	            expenses[expense.type_] = expenses[expense.type_] + expense.amount

	    for (expense, amount) in sorted(expenses.items(), key=lambda e: e[1], reverse=False):
	        print(expense, amount)

	summarizeExpenses(2, foo)