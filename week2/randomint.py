import sys
from random import randint

def main():
	with open(sys.argv[1], "w") as f:
		for i in range(0, int(sys.argv[2])):
			f.write(str(randint(0, 1000)))
			f.write(" ")

if __name__ == '__main__':
	main()