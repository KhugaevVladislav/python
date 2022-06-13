def recursive_sum(arr: list):
    '''рекурсивная функция суммирования элементов в массиве'''
    if len(arr) == 0:
        return 0
    if len(arr) == 1:
        return arr[0]
    return arr[0] + recursive_sum(arr[1:])


arr = [1, 2, 3, 4, 5, -1, -2, -3, -4, -5]
arr1 = list(i for i in range(1, 101))

print(recursive_sum(arr))
print(recursive_sum(arr1))
