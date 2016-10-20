# def count_substrings(haystack, needle): #try to implement .count method
#     counter = 0
#     occurences_counter = 0

#     for i in range(0, len(haystack)):
#     	if haystack[i] == needle[0]:
#     		j = i
#     		for j in range(i, len(haystack)):
#     			if haystack[j] == needle[counter] and counter != len(needle) - 1:
#     				counter = counter + 1
#     			else:
#     				if j == needle[len(needle) - 1]:
#     					occurences_counter = occurences_counter + 1
#     				else:
#     					i = j
#     					break

#     return occurences_counter

# print count_substrings("This is a test string", "is")

# def sum_numbers(matrix):
# 	total_sum = 0;

# 	for i in matrix:
# 		total_sum = total_sum + sum(i)

# 	return total_sum

# print(sum_numbers([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))

# def nan_expand(times):
# 	string = "NaN"
# 	newstr = string[:0] + "Not a " + string[0:]
# 	while times > 0:
# 		times = times - 1
# 		newstr = newstr[:0] + "Not a " + newstr[0:]
# 		print times
# 	return newstr

# print nan_expand(5)


def prime_factorization(n):
    box = n
    arr = [0] * (n + 1)
    counter = 0
    arr2 = [0] * (n + 1)

    for i in range(2, n):
        if box % i > 0:
            i = i + 1
        while box % i == 0:
            box = box / i
            arr[i] = arr[i] + 1
    for j in range(0, len(arr)):
        if arr[j] != 0:
            result = (str(j), str(arr[j])


prime_factorization(1000)