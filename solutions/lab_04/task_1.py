def func():
    values = [10, 20, 30]
    iterator = iter(values)

    print(iterator is values)
    print(iter(iterator) is iterator)
    print(next(iterator))
    print(next(iterator))
    # print(next(iterator))
    # print(next(iterator))
    '''    print(next(iterator))
              ~~~~^^^^^^^^^^
    StopIteration
    '''
    return iterator


def gen():
    yield 1
    yield 2
    yield 3


def consume(iterable) -> list:
    """Собирает элементы iterable, вручную используя iter() и next()."""
    result = []
    iterator = iter(iterable)
    while True:
        try:
            result.append(next(iterator))
        except StopIteration:
            break
    return result


def my_enumerate(iterable, start=0):
    iterator = iter(iterable)
    index = start

    while True:
        try:
            value = next(iterator)
            yield (index, value)
            index += 1
        except StopIteration:
            break


def my_zip(first, second):
    first_iterator = iter(first)
    second_iterator = iter(second)

    while True:
        try:
            first_value = next(first_iterator)
        except StopIteration:
            return

        try:
            second_value = next(second_iterator)
        except StopIteration:
            return

        yield (first_value, second_value)


if __name__ == "__main__":
    print('итератор проверка:')
    func()

    print('\nconsume():')
    print(f'list: {consume([1, 2, 3])}')
    print(f'tuple: {consume((1, 2, 3))}')
    print(f'string: {consume("123")}')
    print(f'range: {consume(range(1, 4))}')
    print(f'generator: {consume(gen())}')

    used_iterator = func()
    print(f'used iterator: {consume(used_iterator)}')

    arr = [1, 2, 3]
    print(f'list обход 1: {consume(arr)}')
    print(f'list обход 2: {consume(arr)}')

    arr_iter = iter(arr)
    print(f'iterator обход 1: {consume(arr_iter)}')
    print(f'iterator обход 2: {consume(arr_iter)}')

    print('\n----------- practise -------------')
    print(f'my_enumerate(list): {list(my_enumerate([1, 2, 3], 2))}')
    print(f'my_enumerate(string): {list(my_enumerate("123", 2))}')
    print(f'my_enumerate(range): {list(my_enumerate(range(1, 4), 2))}')
    print(f'my_enumerate(generator): {list(my_enumerate(gen(), 2))}')
    # print(f'my_enumerate(StepRange): {list(my_enumerate(, 2))}')

    print(f'my_zip(list): {list(my_zip([1, 2, 3], [5, 4, 6]))}')
    print(f'my_zip(string): {list(my_zip("123", "546"))}')
    print(f'my_zip(range): {list(my_zip(range(1, 4), range(4, 7)))}')
    print(f'my_zip(generator): {list(my_zip(gen(), gen()))}')
    # print(f'my_zip(StepRange): {list(my_zip())}')

    '''
    Ошибка дополнительного вызова next(iterator):
    print(next(iterator))
    StopIteration
    
    ответы на вопросы:
    1. возвращает итератор - объект, реализующий итерацию (т.е. имеющий методы __iter()__, __next()__ или исключение StopIteration)
    2. возбуждать исключение `StopIteration`
    3. потому что итератор уже является итерируемым объектом. Это позволяет сохранять состояние обхода в `for` и `iter()`  
    '''
