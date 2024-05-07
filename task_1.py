import timeit
import random


def merge_sort(arr):
    '''Сортування злиттям'''
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]
        merge_sort(L)
        merge_sort(R)
        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

def insertion_sort(arr):
    '''Сортування вставками'''
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >=0 and key < arr[j] :
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


# Генерація випадкового масиву
array = [random.randint(0, 1000) for _ in range(10000)]

# Тестування часу виконання
print("Merge Sort:", timeit.timeit('merge_sort(array.copy())', globals=globals(), number=10))

print("Insertion Sort:", timeit.timeit('insertion_sort(array.copy())',
                                       globals=globals(), number=10))

print("Timsort:", timeit.timeit('sorted(array.copy())', globals=globals(), number=10))
