def number(bus_stops):
	i_count = 0
	o_count = 0
	for item in bus_stops:
		i_count = i_count + item[0]
		o_count = o_count + item[1]
	return i_count

if __name__ == '__main__':
	print(number([[10,0],[3,5],[5,8]]))