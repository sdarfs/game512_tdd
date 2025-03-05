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


def empty_list(mas):
    list = []
    for i in range(4):
        for j in range(4):
            if mas[i][j] == 0:
                num = get_number_from_index(i, j)
                list.append(num)
    return list

def to_the_left(mas):
    for row in mas:
        while 0 in row:
            row.remove(0)
        while (len(row)) != 4:
            row.append(0)
        for i in range(4):
            for j in range(3):
                if mas[i][j] == mas[i][j + 1] and mas[i][j] != 0:
                    mas[i][j] *= 2
                    mas[i].pop(j + 1)
                    mas[i].append(0)
    return mas