def polynom(input_string):
    input_string = input_string.replace(' ', '')
    input_list = list(input_string)

    i = 0
    while(i < len(input_list)):
        if input_list[i] == '*':
            for j in range(i, -1, -1):
                if input_list[j] == '+' or input_list[j] == '-':
                    input_list[j:i] = [''.join(input_list[j:i])]
                    i = j + 3
        if input_list[i] == '^':
            for j in range(i, len(input_list)):
                if input_list[j] == '+' or input_list[j] == '-':
                    input_list[i + 1:j] = [''.join(input_list[i + 1:j])]
                    print(input_list)
                if j == len(input_list) - 1:
                    input_list[i + 1:j + 1] = \
                        [''.join(input_list[i + 1:j + 1])]
                    print(input_list)
        i += 1


polynom("+7854552343*x^5545765865")
