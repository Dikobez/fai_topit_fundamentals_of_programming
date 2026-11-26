import tracemalloc
from collections import deque
from typing import Iterable, Iterator, Generator, List, Any


def read_measurements(lines: Iterable[str]) -> Generator[float, None, None]:
    """Преобразует непустые строки в вещественные числа."""
    for num in lines:
        if num.strip():
            yield float(num)


def filter_range(values: Iterable[float], minimum: float, maximum: float) -> Generator[float, None, None]:
    """Пропускает только значения из закрытого диапазона."""
    for num in values:
        if minimum <= num <= maximum:
            yield num


def moving_average(values: Iterable[float], window_size: int) -> Generator[float, None, None]:
    """Выдает скользящее среднее для заданного размера окна."""
    if window_size <= 0:
        raise ValueError('размер окна должен быть положительным числом')
    current_win = deque(maxlen=window_size)
    current_sum = 0.0

    for num in values:
        if len(current_win) == window_size:
            current_sum -= current_win[0]

        current_win.append(num)
        current_sum += num

        if len(current_win) == window_size:
            yield current_sum / window_size


# ------ practise ------


def take(n: int, iterable: Iterable[Any]) -> Generator[Any, None, None]:
    """Возвращает первые n элементов итерируемого объекта."""
    if n < 0:
        raise ValueError("длина не может быть отрицательной")
    if n == 0:
        return

    it = iter(iterable)
    for _ in range(n):
        try:
            yield next(it)
        except StopIteration:
            return


def drop(n: int, iterable: Iterable[Any]) -> Generator[Any, None, None]:
    """Пропускает первые n элементов, затем выдает остальные."""
    if n < 0:
        raise ValueError("длина не может быть отрицательной")

    it = iter(iterable)
    for _ in range(n):
        try:
            next(it)
        except StopIteration:
            return

    for item in it:
        yield item


def batch(iterable: Iterable[Any], size: int) -> Generator[List[Any], None, None]:
    """Группирует элементы в списки заданного размера."""
    if size <= 0:
        raise ValueError('размер окна должен быть положительным числом')

    chunk = []
    for item in iterable:
        chunk.append(item)
        if len(chunk) == size:
            yield chunk
            chunk = []
    # оставшееся
    if chunk:
        yield chunk


if __name__ == '__main__':
    """Демонстрационный сценарий"""
    raw_lines = ["10.0", "", "12.5", "100.0", "11.5", "13.0", "9.5"]
    nums = read_measurements(raw_lines)
    valid = filter_range(nums, 0.0, 20.0)
    averages = moving_average(valid, 3)

    # print(list(nums)) # [10.0, 12.5, 100.0, 11.5, 13.0, 9.5]
    # print(list(valid)) # [10.0, 12.5, 11.5, 13.0, 9.5]
    # print(f'Список средних значений в движущемся окне: {list(averages)}')  # [11.333333333333334, 12.333333333333334, 11.333333333333334]

    print(f'Первое среднее: {next(averages)}')
    print(f'Второе среднее: {next(averages)}')
    print(f'Оставшиеся: {list(averages)}')
    print(f'Попытка обойти второй раз: {list(averages)}')

    print('\nСоздаем новый конвейер:')
    nums2 = read_measurements(raw_lines)
    valid2 = filter_range(nums2, 0.0, 20.0)
    averages2 = moving_average(valid2, 3)
    print(f'Обход нового конвейера: {list(averages2)}')

    print("\nВключения и генераторные выражения")
    evens_square = [i ** 2 for i in range(2, 21, 2)]
    lens_tuple = {len(s.strip()) for s in raw_lines if s.strip()}
    num_sq = {i: i ** 2 for i in range(1, 11)}
    sum_big = sum(i ** 2 for i in range(1, 10_000_000))
    print(f'список квадратов четных чисел от 1 до 20: {evens_square}')
    print(f'множество длин непустых строк: {lens_tuple}')
    print(f'словарь `число: квадрат` для чисел от 1 до 10: {num_sq}')
    print(f'генераторное выражение для суммы квадратов большого диапазона: {sum_big}')

    print('\n------------ practise ------------')
    nums3 = read_measurements(raw_lines)
    valid3 = filter_range(nums3, 0.0, 20.0)
    averages3 = moving_average(valid3, 2)

    skipped = drop(1, averages3)
    taken = take(5, skipped)
    batches = batch(taken, 2)

    # print(list(skipped)) # [12.0, 12.25, 11.25]
    # print(list(taken)) # [12.0, 12.25, 11.25]
    print('Результат batches:', list(batches))  # [[11.25, 12.0], [12.25, 11.25]]

    print('\nСравнение памяти:')
    # ленивый вариант
    input_data = (str(i % 20) for i in range(100_000))
    tracemalloc.start()
    lazy_nums = read_measurements(input_data)
    lazy_valid = filter_range(lazy_nums, 0.0, 20.0)
    lazy_averages = moving_average(lazy_valid, 3)
    lazy_skipped = drop(1, lazy_averages)
    lazy_taken = take(50, lazy_skipped)
    lasy_result = list(batch(lazy_taken, 2))

    current_lazy, peak_lazy = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    print(f"Пиковая память ленивого конвейера: {peak_lazy / 1024:.2f} KB")

    # Списочный вариант
    input_data_2 = [str(i % 20) for i in range(100_000)]
    tracemalloc.start()
    list_num = list(read_measurements(input_data_2))
    list_valid = list(filter_range(list_num, 0.0, 20.0))
    list_averages = list(moving_average(list_valid, 3))
    list_skipped = list(drop(1, list_averages))
    list_taken = list(take(50, list_skipped))
    list_result = list(batch(list_taken, 2))

    current_list, peak_list = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    print(f"Пиковая память списочного конвейера: {peak_list / 1024:.2f} KB")

    print(f'\nЭкономия памяти: в {peak_list / max(1, peak_lazy):.2f} раз')
