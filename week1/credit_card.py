def is_credit_card_valid(number):
    input_list = [int(i) for i in list(str(number))]

    for i in range(len(input_list[::-1])):
        if i % 2 == 1:
            input_list[i] *= 2

    input_list = [str(i) for i in input_list]
    input_list = ''.join(input_list)
    input_list = list(input_list)

    return sum(int(i) for i in input_list) % 10 == 0


print(is_credit_card_valid(79927398715))
