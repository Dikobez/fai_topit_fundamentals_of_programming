'''Задание 2. Собственный итератор. Реализует класс StepRange - последовательность целых чисел
с произвольным ненулевым шагом, и отдельный класс StepRangeIterator,
который хранит текущее состояние обхода'''


class StepRangeIterator:
    """Итератор для последовательного обхода StepRange. Хранит текущее состояние обхода
    и возвращает следующий элемент при каждом вызове __next__()"""

    def __init__(self, start: int, stop: int, step: int) -> None:
        """Инициализирует итератор с начальным значением, границей и шагом"""
        self.current = start  # Текущее значение последовательности.
        self.stop = stop  # Граница (не включительно) последовательности.
        self.step = step  # Шаг между элементами.

    def __next__(self) -> int:
        """Возвращает следующий элемент последовательности"""
        if self.step > 0 and self.current >= self.stop or self.step < 0 and self.current <= self.stop:
            raise StopIteration
        value = self.current
        self.current += self.step
        return value

    def __iter__(self) -> 'StepRangeIterator':
        """Возвращает сам итератор"""
        return self


class StepRange:
    """Итерируемый объект, представляющий последовательность целых чисел
    с произвольным ненулевым шагом. Не хранит список всех значений, а вычисляет их сразу, занимая
    константную память O(1) независимо от размера диапазона"""

    def __init__(self, start: int, stop: int, step: int) -> None:
        """Инициализирует StepRange с заданными параметрами"""
        self.start = start
        self.stop = stop
        self.step = step
        if self.step == 0:
            raise ValueError("шаг не может быть нулевым")

    def __iter__(self) -> StepRangeIterator:
        """Создает и возвращает новый итератор для обхода последовательности"""
        result = StepRangeIterator(self.start, self.stop, self.step)
        return result

    def __len__(self) -> int:
        """Вычисляет количество элементов в последовательности за O(1)"""
        if self.step > 0 and self.start >= self.stop or self.step < 0 and self.start <= self.stop:
            return 0
        return (abs(self.stop - self.start) + abs(self.step) - 1) // abs(self.step)

    def __contains__(self, item: int) -> bool:
        """Проверяет принадлежность элемента последовательности за O(1)"""
        if self.step > 0:
            if self.start <= item < self.stop and (item - self.start) % self.step == 0:
                return True
        else:
            if self.stop < item <= self.start and (item - self.start) % abs(self.step) == 0:
                return True
        return False

    def __repr__(self) -> str:
        """Возвращает однозначное строковое представление объекта"""
        return f'StepRange({self.start}, {self.stop}, {self.step})'


if __name__ == "__main__":
    """Демонстрационный сценарий"""

    numbers = StepRange(2, 11, 3)
    print(list(numbers))  # [2, 5, 8]
    print(f'повторный вызов list(numbers){list(numbers)}\n')

    it1 = iter(numbers)
    it2 = iter(numbers)
    print(f'next(it1): {next(it1)}')
    print(f'next(it1): {next(it1)}')
    print(f'next(it2): {next(it2)}')

    print(f'Отрицательный шаг: {list(StepRange(10, 1, -3))}')
    print(f'Недостижимая граница: {list(StepRange(10, 2, 1))}')
    # print(f'Нулевой шаг: {list(StepRange(10, 2, 0))}') # ValueError: шаг не может быть нулевым

    print('\nпроверка случаев:')
    print(list(StepRange(0, 5, 1)))
    print(list(StepRange(5, 0, -1)))
    print(list(StepRange(0, 0, 1)))
    print(list(StepRange(0, 5, -1)))

    print('\nпоочередный вызов двух итераторов:')
    it1 = iter(numbers)
    it2 = iter(numbers)
    print(f'старт -> it1.current-{it1.current}, it2.current-{it2.current})')
    print(f"next(it1)={next(it1)} -> it1.current={it1.current}, it2.current={it2.current}")
    print(f"next(it2)={next(it2)} -> it1.current={it1.current}, it2.current={it2.current}")
    print(f"next(it1)={next(it1)} -> it1.current={it1.current}, it2.current={it2.current}")
    print(f"next(it2)={next(it2)} -> it1.current={it1.current}, it2.current={it2.current}")
    print(f"next(it1)={next(it1)} -> it1.current={it1.current}, it2.current={it2.current}")
    print(f"next(it2)={next(it2)} -> it1.current={it1.current}, it2.current={it2.current}")

    print('\n------------ practise -------------')
    big = StepRange(0, 10_000_000, 3)
    print(f'9_999_999 in big: {9_999_999 in big}')
    print(f'9_999_998 in big: {9_999_998 in big}')
    print(f'шагов через __contains__: {1}')

    steps = 0
    found = False
    for x in big:
        steps += 1
        if x == 9_999_999:
            found = True
            break
    print(f'шагов в последовательном обходе: {steps}')

    rev = StepRange(10, 1, -3)
    print('\nпроверка: ', rev)
    print("len:", len(rev))
    print("7 in rev:", 7 in rev)
    print("8 in rev:", 8 in rev)
