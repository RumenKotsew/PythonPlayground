# A function for counting the digits of a number
# def sum_of_digits(number):
#     result = 0
#     while number > 0:
#         result = result + number % 10
#         number = number // 10
    
#     return result

# print(sum_of_digits(82915))

# Create list with the digits of a number
# def to_digits(number):
#     result = []
#     while number > 0:
#         result.insert(0, number % 10)
#         number = number // 10

#     return result

# print(to_digits(123589999))

# Create number from array
# def to_number(digits):
#     number = 0;
#     for i in range(0, len(digits)):
#         if i != 0:
#             number = (number * 10) + digits[i]
#         else: number = number + digits[i]

#     return number

# print(to_number([1, 2, 3, 5, 6, 9, 9, 9]))


# Count the vowels in a string
# def count_vowels(string):
#     string = string.lower()
#     counter = 0
#     vowels = ["a", "i", "u", "o", "e"]

#     for char in string:
#         if char in vowels:
#             counter = counter + 1

#     return counter

# print(count_vowels("AAAAAAAAAAAAAAAAAA"))

# Count the consonants in a string
# def count_consonants(string):
#     string = string.lower()
#     counter = 0
#     vowels = ["a", "i", "u", "o", "e"]

#     for char in string:
#         if char not in vowels:
#             counter = counter + 1

#     return counter

# print(count_consonants("kkkkkkkkkkaaiaiaoaiaoai"))


# Check if a given number is prime
# def prime_number(number):
#     if (number % 2) > 0:
#         return "true"
#     else: return "false"

# print(prime_number(719))

# Sum of the factorials of the digits in the number
# def fact_digits(n):
#     iterator = 1;
#     total_sum = 1;
#     for iterator in range(1, n + 1):
#         total_sum = total_sum * iterator

#     return total_sum

# print fact_digits(5)

# fibonacci sequence
# def fibonacci(number):
#     arr = []
#     for iterator in range(0, number):
#         if iterator == 0 or iterator == 1:
#             arr.append(1)
#         else:
#             arr.append(arr[iterator - 1] + arr[iterator - 2])

#     return arr

# print fibonacci(15)

# Check if a given string is palindrome
# def palindrome(string):
#     flag = "false"
#     for char_number in range(0, len(string)):
#         if string[(len(string) - char_number) - 1] == string[char_number]:
#             flag = "true"
#         else:
#             flag = "false"
#             break

#     return flag

# print palindrome("10101")    

# Dictionary with all characters from a string
def char_histogram(string):
    dict dictionary = []
    for char in string:
        if char in string:
            dictionary.append(char, 1)
            


