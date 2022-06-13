def find_smallest(arr: list):
    smallest = arr[0]
    smallest_index = 0
    for i in range(len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index


def choice_sort(arr: list):
    sorted_arr = []
    for i in range(len(arr)):
        smallest = find_smallest(arr)
        sorted_arr.append(arr.pop(smallest))
    return sorted_arr


def choice_sort1(arr):
    for pos in range(0, len(arr)-1):
        for j in range(pos+1, len(arr)):
            if arr[j] < arr[pos]:
                arr[pos], arr[j] = arr[j], arr[pos]
    return arr


arr = [1, 4, 3, 2, 5, -1, -1, 0, 100, -1000, -1000]
print(choice_sort1(arr))

sorted = choice_sort(arr)
print(sorted)


