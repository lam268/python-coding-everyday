

def productFib(prod):
	a, b = 0, 1
	while prod > a * b:
		a, b = b, a + b

	return [a, b, prod == a * b]
	
if __name__ == '__main__':
