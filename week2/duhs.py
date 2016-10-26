import sys
import os


def get_size(start_path = sys.argv[1]):
	total_sum = 0

	for root, dirs, files in os.walk(start_path):
		for f in files:
			fp = os.path.join(root, f)
			total_sum += os.path.getsize(fp)
	return total_sum

print(get_size())


def main():
	pass
