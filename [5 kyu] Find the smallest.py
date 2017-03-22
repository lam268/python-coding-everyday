def min_value(n):
	i,j,index = str(n)[0], 1, 0
	while j < len(str(n)):
		if int(str(n)[j]) <= int(i):
			i = j
			index = j
		j += 1
	return index

def smallest(n):
	if not n:
		return
	index = min_value(n)
	if index:
		result = str(n)[index-1] + str(n)[0:index-1] + str(n)[index::]
		result1 = str(n)[1:index-1] + str(n)[0] + str(n)[index::]
		print(index,result,result1)
		return [result, index, 0] if result < result1 else [result1, 0, index]
	else:
		return [str(n)[0] + smallest(int(str(n)[1:]))[0], smallest(int(str(n)[1:]))[1] + 1, smallest(int(str(n)[1:]))[2] + 1]


if __name__ == '__main__':
	n = 261235
	# print((min(str(n))))
	print(smallest(261235))
	