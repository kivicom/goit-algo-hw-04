import heapq

def merge_k_lists(sorted_lists):
    '''Цей метод ефективно об'єднує кілька відсортованих списків
    у один великий відсортований список,
    використовуючи властивості мінімальної купи для забезпечення мінімального часу виконання'''

    min_heap = []
    # Ініціалізація купи з першими елементами кожного списку
    for idx, sublist in enumerate(sorted_lists):
        if sublist:
            heapq.heappush(min_heap, (sublist[0], idx, 0))

    list_merged = []
    # Витягування найменших елементів і добавлення наступних із того ж списку
    while min_heap:
        val, list_idx, element_idx = heapq.heappop(min_heap)
        merged_list.append(val)
        if element_idx + 1 < len(sorted_lists[list_idx]):
            next_element = sorted_lists[list_idx][element_idx + 1]
            heapq.heappush(min_heap, (next_element, list_idx, element_idx + 1))

    return list_merged

# Приклад виклику функції
example_lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
merged_list = merge_k_lists(example_lists)
print("Sorted list:", merged_list)
