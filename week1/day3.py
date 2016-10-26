# def is_number_balanced(m):
# 	left_side = 0
# 	right_side = 0
# 	n = str(m)
# 	left_side_arr = []
# 	right_side_arr = []
# 	left_sum = 0
# 	right_sum = 0

# 	if len(n) % 2 == 0:
# 		for left_side_iterator in range(0, len(n) // 2):
# 			left_side_arr.append(n[left_side_iterator])
# 		for right_side_iterator in range(len(n) // 2, len(n)):
# 			right_side_arr.append(n[right_side_iterator])
# 		for iterator in range(0, len(left_side_arr)):
# 			left_sum = left_sum + int(left_side_arr[iterator])
# 			right_sum = right_sum + int(right_side_arr[iterator])
# 		if right_sum == left_sum:
# 			return True
# 		else:
# 			return False
# 	if len(n) % 2 != 0:
# 		for i in range(0, len(n)):
# 			if i == len(n) // 2:
# 				for j in range(0, i + 1):
# 					left_side = left_side + int(n[j])
# 			if i == len(n) - 1:
# 				for k in range(len(n) // 2, len(n)):
# 					right_side = right_side + int(n[k])
# 		if right_side == left_side:
# 			return True
# 		else:
# 			return False


# print is_number_balanced(451812)

# def increasing_or_decreasing(seq):
# 	for i in range(0, len(seq)):
# 		if i != len(seq) - 1:
# 			if seq[i] > seq[i + 1]:
# 				for down_iterator in range(0, len(seq)):
# 					if seq[down_iterator] <= seq[down_iterator + 1]:
# 						return False
# 					else:
# 						if seq[len(seq) - 1] > seq[len(seq) - 2]:
# 							return True
# 						else:
# 							return False
# 			if seq[i] < seq[i + 1]:
# 				for up_iterator in range(0, len(seq)):
# 					if seq[up_iterator] >= seq[up_iterator + 1]:
# 						return False
# 					else:
# 						if seq[len(seq) - 1] < seq[len(seq) - 2]:
# 							return True
# 						else:
# 							return False


# print increasing_or_decreasing([1, 2, 3, 4, 5, 1])

# def largest_palindrome(m):
#     n = str(m)
#     result = 0

#     for char_number in range(0, len(n)):
#         if n[(len(n) - char_number) - 1] == n[char_number]:
#             result = n
#         else:
#             for i in range(m, 0):
#                 for char_number in range(0, len(i)):
#                     if i[(len(i) - char_number) - 1] == i[char_number]:
#                         result = i
#                         break
#     return result


# print largest_palindrome(5676)

# def sum_of_numbers(st):
#     for i in range(0, len(st)): # isDigit method?

def birthday_ranges(numbers, tuples):
    dct = dict(tuples)
    