print('# 4.1 main task')


def arithmetic_mean(values: list[float]) -> float:
    """Возвращает среднее арифметическое непустого списка."""
    if not values:
        raise ValueError("Empty list")
    return sum(values) / len(values)


def normalize_name(name: str) -> str:
    """Удаляет лишние пробелы и приводит каждую часть имени к нужному регистру."""
    if not name.split():
        raise ValueError("Empty name")
    res = name.strip()
    res = list(map(lambda x: x.capitalize(), res.split()))
    res = ' '.join(res)
    return res


def build_report(
        student: str,
        results: list[int],
        *,
        precision: int = 2,
        prefix: str = "Результат") -> str:
    """Формирует строковый отчет о результатах студента."""
    res_mean = round(arithmetic_mean(results), precision)
    name_stud = normalize_name(student)
    return f'{name_stud}. {prefix}: {res_mean}'


def collect_tags(*tags: str, lowercase: bool = True) -> tuple[str, ...]:
    """Возвращает очищенные теги без пустых значений и повторов."""
    res = []
    used = set()
    for tag in tags:
        t = tag.strip()
        if lowercase: t = t.lower()

        if t and t not in used:
            res.append(t)
            used.add(t)
    return tuple(res)


assert collect_tags('one', 'Two', 'one', 'three') == ('one', 'two', 'three'), 'collect_tags: not unique'
assert collect_tags('one ', ' ', 'two', '  three') == ('one', 'two', 'three'), 'collect_tags: empty tags & spaces'
assert collect_tags('oNe', 'twO', 'THree', lowercase=False) == ('oNe', 'twO', 'THree')

assert arithmetic_mean([1, 2, 3]) == 2
assert arithmetic_mean([-2, 4]) == 1
assert arithmetic_mean([float('inf'), 2]) == float('inf')
try:
    arithmetic_mean([])
except ValueError:
    pass
else:
    assert False, 'expected ValueError'

assert normalize_name('NAme SuRname') == 'Name Surname'
assert normalize_name(' NAme ') == 'Name'
assert normalize_name('  s ') == 'S'

assert build_report('IvaN   ivanOv ', [87, 84, 76]) == f'Ivan Ivanov. Результат: 82.33'
assert build_report('Ivan Ivanov', [87, 84, 76], precision=3) == f'Ivan Ivanov. Результат: 82.333'
assert build_report('IvaN   ivanOv ', [87, 84, 76], prefix='Result') == f'Ivan Ivanov. Result: 82.33'

print('\ncollect_tags:')
print(collect_tags('one', 'Two', 'one', 'three'))
print(collect_tags('one ', ' ', 'two', '  three'))
print(collect_tags('oNe', 'twO', 'THree', lowercase=False))

print('\narithmetic_mean:')
print(arithmetic_mean([1, 2, 3]))
print(arithmetic_mean([-2, 4]))
print(arithmetic_mean([float('inf'), 2]))

print('\nnormalize_name:')
print(normalize_name('NAme SuRname'))
print(normalize_name(' NAme '))
print(normalize_name('  s '))

print('\nbuild_report:')
print(build_report('IvaN   ivanOv ', [87, 84, 76]))
print(build_report('Ivan Ivanov', [87, 84, 76], precision=3))
print(build_report('IvaN   ivanOv ', [87, 84, 76], prefix='Result'))

arguments = ["Ivan", [80, 90, 100]]
print('arguments:', build_report(*arguments))

report_options = {
    "student": "Ivan",
    "results": [80, 90, 100],
    "precision": 1,
    "prefix": "Средний балл",
}
print('report_options:', build_report(**report_options))

print('\n# Исследование LEGB')
course = '1'


def outer_func():
    course = '2'

    def inner_func():
        nonlocal course
        course = '3'
        print(f'Внутренняя, course: {course}')

    print(f'Внешняя, до вызова inner_func(), course: {course}')
    inner_func()
    print(f'Внешняя, после вызова inner_func(), course: {course}')


outer_func()
print('course:', course)

print('\n# Ошибка изменяемого значения по умолчанию')


def add_result(value, results=[]):
    results.append(value)
    return results


print(add_result(5))
print(add_result(10))
print(add_result(15))

print('\nкорректный вариант:')


def add_result(value, results=None):
    if results is None:
        results = []
    results.append(value)
    return results


print(add_result(5))
print(add_result(10))
print(add_result(15))

print('\n# Практическое расширение')


def apply_to_results(operation, values):
    result = []
    for value in values:
        result.append(operation(value))
    return result


results = [50, 60, 70, 80, 90]


def double(value):
    return value * 2


assert apply_to_results(double, results) == [100, 120, 140, 160, 180]
assert apply_to_results(lambda x: x ** 2, results) == [2500, 3600, 4900, 6400, 8100]

print('double:', apply_to_results(double, results))
print('lambda:', apply_to_results(lambda x: x ** 2, results))
print('results:', results)


def make_threshold_checker(threshold):
    def check(result):
        return result >= threshold

    return check


check_60 = make_threshold_checker(60)
check_80 = make_threshold_checker(80)

assert check_60(70) == True
assert check_80(60) == False
assert check_80(80) == True

print('\ncheck_60(70):', check_60(70))
print('check_80(70):', check_80(70))
print('check_80(80):', check_80(80))
