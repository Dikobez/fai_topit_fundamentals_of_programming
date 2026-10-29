import tracemalloc, time, random


def analysing_measurements(arr):
    sum_arr = 0
    min_arr = arr[0]
    max_arr = arr[0]
    even = 0
    len_arr = 0

    for i in arr:
        sum_arr += i
        if i < min_arr:
            min_arr = i
        if i > max_arr:
            max_arr = i
        if i % 2 == 0:
            even += 1
        len_arr += 1

    mean = sum_arr / len_arr
    # вычисление количества чисел, больших среднего арифметического
    up_mean = 0
    for i in arr:
        if i > mean:
            up_mean += 1

    return sum_arr, min_arr, max_arr, even, up_mean


def linear_search(arr, num):
    ind = -1
    comp = 0  # число сравнений
    for i, v in enumerate(arr):
        comp += 1
        if v == num:
            ind = i
            break
    return ind, comp


def is_prime(num):
    if num <= 1:
        return False
    i = 2
    while i * i <= num:
        if num % i == 0:
            return False
        i += 1
    return True


def binary_search(ar, vl):
    lt = 0
    rt = len(ar) - 1
    comp = 0  # число сравнений
    while lt <= rt:
        mid = (lt + rt) // 2
        if vl < ar[mid]:
            rt = mid - 1
        elif vl > ar[mid]:
            lt = mid + 1
        elif ar[mid] == vl:
            break
        comp += 1
    else:
        return -1, comp
    return mid, comp


def selection_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        min_val = arr[i]
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < min_val:
                min_val = arr[j]
                min_idx = j

        if min_idx != i:
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr


def time_memory_test(func, data, num):
    tracemalloc.start()
    time_start = time.perf_counter()

    result, comp = func(data, num)

    time_end = time.perf_counter()
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    time_sec = time_end - time_start
    mem_kb = peak / 1024

    return time_sec, mem_kb, result, comp


def main():
    measurements = [12, 15, 11, 18, 18, 9, 21, 15, 7, 18]
    measures = analysing_measurements(measurements)
    print('| сумма: ', measures[0], '| O(n) |')
    print('| минимальное значение: ', measures[1], '| O(n) |')
    print('| максимальное значение: ', measures[2], '| O(n) |')
    print('| количество четных чисел: ', measures[3], '| O(n) |')
    print('| количество значений, больших ср. арифм.: ', measures[3], '| O(n) |')
    print('| линеный поиск введенного числа: ', linear_search(measurements, int(input('Введите число: ')))[0],
          '| O(n) |')

    # Дополнительный алгоритмический эксперимент
    for i in measurements:
        print(f'{i} - {['Составное', 'Простое'][is_prime(i)]}')

    # Практическое расширение
    sort_measurements = selection_sort(measurements)
    arr10 = sort_measurements
    arr100 = selection_sort([random.randint(-10 ** 2, 10 ** 2) for _ in range(100)])
    arr1000 = selection_sort([random.randint(-10 ** 2, 10 ** 2) for _ in range(1000)])

    gap = 12
    num = int(input('Введите число для поиска: '))
    print(
        f'\n| {'Тип поиска':<{gap}}| {'Длина':<{gap}} | {'Время':<{gap}} | {'Память':<{gap}} | {'Сравнений':<{gap}} | {'Результат':<{gap}} |')
    print(
        f'|  {':---':<{gap}} | {':---':<{gap}} | {':---':<{gap}} | {':---':<{gap}} | {':---':<{gap}} | {':---':<{gap}} |')

    for ar in [arr10, arr100, arr1000]:
        len_arr = len(ar)
        time_sec, memory, result, comp = time_memory_test(binary_search, ar, num)
        print(
            f' {'| Бинарный поиск':<{gap}} | {len_arr:<{gap}} | {time_sec:<{gap}.6f} sec | {memory:<{gap}.6f} KB | {comp:<{gap}} | {result:<{gap}} |')

        time_sec, memory, result, comp = time_memory_test(linear_search, ar, num)
        print(
            f' {'| Линейный поиск':<{gap}} | {len_arr:<{gap}} | {time_sec:<{gap}.6f} sec | {memory:<{gap}.6f} KB | {comp:<{gap}} | {result:<{gap}} |')


if __name__ == "__main__":
    main()
