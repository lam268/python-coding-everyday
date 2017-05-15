#! /usr/local/bin python3
# -*- coding: utf-8 -*-
"""
	Description:
		You have to return which player won! In case of a draw return
		draw

    Author:
    	yangxw163@gmail.com

    Created:
    	15 May 2017
"""
def rps(p1, p2):
	if p1 == p1:
		return 'Draw!'
	if p1 == 'scissors':
		if p2 == 'paper':
			return 'Player 1 won!'
		else:
			return 'Player 2 won!'
	if p1 == 'paper':
		if p2 == 'rock':
			return 'Player 1 won!'
		else
			return 'Player 2 won!'
	if p1 == 'rock':
		if p2 == 'scissors':
			return 'Player 1 won!'
		else:
			return 'Player 2 won!'