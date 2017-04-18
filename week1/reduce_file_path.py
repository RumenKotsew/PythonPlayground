import re


def remove_values_from_list(the_list, val):
    return [value for value in the_list if value != val]


def reduce_file_path(path):
    res = []
    path = path
    path = path.split('/')
    path = remove_values_from_list(path, '')
    temp = ['/']
    for i in path:
        temp.append(i)
    path = temp
    it = iter(path)
    for item in it:
        if item == '.':
            pass
        elif item == '..':
            res.pop(len(res) - 1)
            res.append('/')
        else:
            res.append(item)
    if len(res) == 1:
        res.append('')
    res = list(re.sub(r'(/)\1+', r'\1', '/'.join(res)))

    if res[len(res) - 1] == '/' and len(res) > 1:
        res.pop(len(res) - 1)
    res = ''.join(res)

    return res
