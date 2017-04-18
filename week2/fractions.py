def recursive(a, b):
    if a == b:
        return a
    else:
        if a > b:
            return recursive(a - b, b)
        else:
            return recursive(a, b - a)


def inner(a, b):
    if b == 0:
        return a
    else:
        return recursive(b, a % b)


def simplify_fraction(fraction):
    a = fraction[0] // inner(fraction[0], fraction[1])
    b = fraction[1] // inner(fraction[0], fraction[1])
    return (a, b)


def sort_fractions(fractions):
    arr = [(i[0] / i[1], i) for i in fractions]
    sorted_arr = sorted(arr)
    res = [i[1] for i in sorted_arr]
    return res
