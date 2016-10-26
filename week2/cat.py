# cat.py
import sys


def main():
	with open(sys.argv[1], "r") as f:
		print(f.read())

if __name__ == '__main__':
	main()