def nod(a: int, b: int):
    '''алгоритм Евклида - поиск наибольшего общего делителя. a, b натуральные числа
            функция возвращает наибольший общий делитель'''
    if a > b:
        if a % b == 0:
            return b
        return nod(a % b, b)
    else:
        if b % a == 0:
            return a
        return nod(a, b % a)


c = nod(1234, 2468)
print(c)
