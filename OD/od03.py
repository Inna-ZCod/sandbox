start = [-3, 5, 0, -8, 1, 10, 54, 18, -9, 7, 12, 6, 6, -5, 0, 2]
print("Стартовый массив: ", start)


# Пузырьковая сортировка
def bubble(mas):
    for run in range(len(mas) - 1):
        for i in range(len(mas) - 1 - run):
            if mas[i] > mas[i + 1]:
                mas[i], mas[i + 1] = mas[i + 1], mas[i]
    return mas

bbl = bubble(start)
print("Сортировка пузырьковым способом: ", bbl)


# Быстрая сортировка
def quick_sort(s):
    if len(s) <= 1:
        return s

    element = s[0]
    left = list(filter(lambda i: i < element, s))
    center = [i for i in s if i == element]
    right = list(filter(lambda i: i > element, s))

    return quick_sort(left) + center + quick_sort(right)

qs = quick_sort(start)
print("Быстрая сортировка: ", qs)


# Сортировка выбором
def selection_sort(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

sel = selection_sort(start)
print("Сортировка выбором: ", sel)


# Сортировка вставками
def insert_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr

ins = insert_sort(start)
print("Сортировка вставками: ", ins)