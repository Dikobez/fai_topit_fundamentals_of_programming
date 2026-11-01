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
    used=set()
    for tag in tags:
        t = tag.strip()
        if lowercase: t = t.lower()

        if t and t not in used:
            res.append(t)
            used.add(t)
    return tuple(res)


assert collect_tags('one', 'Two', 'one', 'three')==('one', 'two', 'three'), 'collect_tags: not unique'
assert collect_tags('one ', ' ', 'two', '  three')==('one', 'two', 'three'), 'collect_tags: empty tags & spaces'
assert collect_tags('oNe', 'twO', 'THree', lowercase=False)==('oNe', 'twO', 'THree')

assert arithmetic_mean([1,2,3])==2
assert arithmetic_mean([1,2])==1.5
assert arithmetic_mean([float('inf'), 2])==float('inf')

assert normalize_name('NAme SuRname')=='Name Surname'
assert normalize_name(' NAme ')=='Name'
assert normalize_name('  s ')=='S'

assert build_report('IvaN   ivanOv ', [87, 84, 76])==f'Ivan Ivanov. Результат: 82.33'
assert build_report('Ivan Ivanov', [87, 84, 76], precision=3)==f'Ivan Ivanov. Результат: 82.333'
assert build_report('IvaN   ivanOv ', [87, 84, 76], prefix='Result')==f'Ivan Ivanov. Result: 82.33'


print('\ncollect_tags:')
print(collect_tags('one', 'Two', 'one', 'three'))
print(collect_tags('one ', ' ', 'two', '  three'))
print(collect_tags('oNe', 'twO', 'THree', lowercase=False))

print('\narithmetic_mean:')
print(arithmetic_mean([1,2,3]))
print(arithmetic_mean([1,2]))
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
