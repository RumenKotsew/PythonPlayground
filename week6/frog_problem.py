class FrogTree():
    class Node():
        def __init__(self, frog_map):
            self.frog_map = frog_map
            self.priority = 10
            self.next = ()

    def __init__(self, root_data):
        self.root = self.Node(root_data)

    def dfs(self):
        pass

    def generate(self, main_frog_map):
        for char_index in range(0, len(main_frog_map)):
            if main_frog_map[char_index] == '_':
                result = self.apply_rules(main_frog_map, char_index)
        return result

    def apply_rules(self, main_frog_map, char_index):
        result = []
        result = self.apply_rule_1(main_frog_map, char_index, result)
        return result

    def apply_rule_1(self, main_frog_map, char_index, result):
        current_frog_map = main_frog_map
        if char_index > 1:
            if current_frog_map[char_index - 2] == '>':
                current_frog_map[char_index] = '>'
                current_frog_map[char_index - 2] = '_'
                swapped_1 = current_frog_map

                result.append(swapped_1)
                return self.apply_rule_2(main_frog_map, char_index, result)
            else:
                return self.apply_rule_2(main_frog_map, char_index, result)
        else:
            return self.apply_rule_2(main_frog_map, char_index, result)

    def apply_rule_2(self, main_frog_map, char_index, result):
        current_frog_map = main_frog_map
        if char_index < (len(current_frog_map) - 3):
            if current_frog_map[char_index + 2] == '<':
                current_frog_map[char_index] = '<'
                current_frog_map[char_index + 2] = '_'
                swapped_2 = current_frog_map

                result.append(swapped_2)
                return self.apply_rule_3(main_frog_map, char_index, result)
            else:
                return self.apply_rule_3(main_frog_map, char_index, result)
        else:
            return self.apply_rule_3(main_frog_map, char_index, result)

    def apply_rule_3(self, main_frog_map, char_index, result):
        current_frog_map = main_frog_map
        if char_index > 0:
            if current_frog_map[char_index - 1] == '>':
                current_frog_map[char_index] = '>'
                current_frog_map[char_index - 1] = '_'
                swapped_3 = current_frog_map

                result.append(swapped_3)
                return self.apply_rule_4(main_frog_map, char_index, result)
            else:
                return self.apply_rule_4(main_frog_map, char_index, result)
        else:
            return self.apply_rule_4(main_frog_map, char_index, result)

    def apply_rule_4(self, main_frog_map, char_index, result):
        current_frog_map = main_frog_map
        if char_index < (len(current_frog_map) - 2):
            if current_frog_map[char_index + 1] == '<':
                current_frog_map[char_index] = '<'
                current_frog_map[char_index + 1] = '_'
                swapped_4 = current_frog_map

                result.append(swapped_4)
                return result
            else:
                return result
        else:
            return result
