def get_number_from_index(i, j):
    return i * 4 + j + 1


def get_index_from_number(num):
    num -= 1
    x, y = num // 4, num % 4
    return x, y


def zero_in_mas(mas):
    for row in mas:
        if 0 in row:
            return True
    return False
