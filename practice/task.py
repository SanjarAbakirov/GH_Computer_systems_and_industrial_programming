# Merge Sort

def merge_sort(arr):
    """Сортировка слиянием - O(N log N)"""
    if len(arr) <= 1:
        return arr

    # Разделение массива - O(log N) раз
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    # Рекурсивная сортировка каждой половины
    left_sorted = merge_sort(left_half)
    right_sorted = merge_sort(right_half)

    # Слияние - O(N)
    return merge(left_sorted, right_sorted)


def merge(left, right):
    """Слияние двух отсортированных массивов - O(N)"""
    result = []
    i = j = 0

    # Слияние элементов в порядке возрастания
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Добавление оставшихся элементов
    result.extend(left[i:])
    result.extend(right[j:])

    return result


# Пример использования
arr = [64, 34, 25, 12, 22, 11, 90]
sorted_arr = merge_sort(arr)
print(f"Отсортированный массив: {sorted_arr}")
print(
    f"Исходный размер: {len(arr)}, операций ~ {len(arr) * (len(arr).bit_length())}")
