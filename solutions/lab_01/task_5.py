"""
Модуль для обработки результатов эксперимента.
Выполняет сбор параметров, расчёт временных и комплексных показателей и выводит итоговую карточку с диагностикой типов данных.
"""
# Входные данные
researcher = input('имя исследователя: ')
experiment = input('название эксперимента: ')
launches_count = int(input('количество выполненных запусков(int): '))
launch_duration = float(input('длительность одного запуска в секундах(float): '))
real_coef = float(input('действительная часть комплексного коэффициента(float): '))
imag_coef = float(input('мнимая часть комплексного коэффициента(float): '))

# Вычисления
gen_duration_sec = launches_count * launch_duration
gen_duration_min = gen_duration_sec / 60
has_runs = bool(launches_count)
coef = complex(real_coef, imag_coef)
modulus_sq = real_coef ** 2 + imag_coef ** 2

# Вывод
print('========================================')
print('ЭКСПЕРИМЕНТ:', experiment)
print('Исследователь:', researcher)
print('Запуски:', launches_count)
print(f'Общее время: {gen_duration_sec:.2f} c ({gen_duration_min:.2f} мин)')
print('Коэффициент:', coef)
print(f'Квадрат модуля: {modulus_sq:.2f}')
print('Есть выполненные запуски:', has_runs)
print('========================================\n')

# Диагностика
print('===============input types==============')
print('имя исследователя:', type(researcher))
print('название эксперимента:', type(experiment))
print('количество выполненных запусков:', type(launches_count))
print('длительность одного запуска в секундах:', type(launch_duration))
print('действительная часть комплексного коэффициента:', type(real_coef))
print('мнимая часть комплексного коэффициента:', type(imag_coef))
print('========================================')
