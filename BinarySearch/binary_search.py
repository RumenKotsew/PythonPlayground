def binary_search(array, a, b, element):
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


def find_turning_point(array, start, end):
    if array == sorted(array, key=int):
        return "Array is sorted."
    else:
        for i in range(len(array)):
            if array[0:i] != sorted(array[0:i], key=int):
                return "Turning point is " + str(array[i - 1]) + " on index " + str(i - 1) + "."

    return "Turning point is " + str(array[len(array) -1]) + " on index " + str(len(array) - 1) + "."
