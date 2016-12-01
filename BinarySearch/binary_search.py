def binary_search(array, element):
    start = 0
    end = len(array) - 1
    mid = end // 2
    return binary_search_recursive(array, element, start, end, mid)


def binary_search_recursive(array, element, start, end, mid):
    if array[mid] != element:
        if element < array[mid]:
            end = mid
        else:
            start = mid
        mid = (start + end) // 2
        return binary_search_recursive(array, element, start, end, mid)
    else:
        return mid


def main():
    array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    element = 12
    print(binary_search(array, element))


if __name__ == '__main__':
    main()
