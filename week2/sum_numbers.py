import sys

def main():
	lines_arr = [0]
	total_sum = 0

	with open(sys.argv[1], "r") as f:
		lines_arr = f.read()
		lines_arr = lines_arr.split(" ")

	for i in lines_arr:
		if i != '':
		    total_sum += int(i)

	print(total_sum)


if __name__ == '__main__':
	main()