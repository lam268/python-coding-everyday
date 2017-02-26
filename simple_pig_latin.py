#! /usr/local/bin python3 
# -*- coding: utf-8 -*-
"""
	Description: 
		Move the first letter of each word to the end of it, 
        then add 'ay' to the end of the word.

    Args:
        text (str)

    Author: 

    	yangxw163@gmail.com
        
    Created:

    	24 Ferbary 2017
"""

def pig_it(text):
    if not isinstance(text, str) or len(text) == 0:
        return 'bad args'
    text_split = text.split()
    result = []
    for item in text_split:
        if len(item) == 1 and (ord(item) < 65 or ord(item) > 122):
            result.append(item)
        else:
            item = item[1:len(item)] + item[0] + 'ay'
            result.append(item)

    return ' '.join(result)

#优雅实现
def pig_it(text):
    return ' '.join(item[1:] + item[:1] + 'ay' if item.isalpha() else item for item in text.split())

if __name__ == '__main__':
    print(pig_it('uisQay ustodietcay psosiay ustodescay ?'))
    