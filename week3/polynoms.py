class Parser():
    def convert_to_dict(input_string):
        input_list = ""

        input_string = input_string.replace(" ", "")
        input_list = list(input_string)
        for main_index in range(0, len(input_list)):
            if input_list[main_index] == 'x':
                for constant_index in range(main_index, 0):
                    if input_list[constant_index] == '+' or \
                        input_list[constant_index] == '-' or \
                            constant_index == 0:
                        constant_index += 1
                        input_list[constant_index:main_index] = \
                            [''.join(input_list[constant_index:main_index])]
                        main_index = constant_index + 1
                        break
                for times_index in range(main_index, len(input_list)):
                    if input_list[times_index] == '+' or \
                        input_list[times_index] == '-' or \
                            times_index == 0:
                        input_list[main_index:times_index] = \
                            [''.join(input_list[constant_index:main_index])]
