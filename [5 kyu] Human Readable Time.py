def make_readable(seconds):
	return '%02d:%02d:%02d' %(seconds / 3600, (seconds % 3600) / 60, ((seconds % 3600) % 60) % 60)

if __name__ == '__main__':
	print(make_readable(59))