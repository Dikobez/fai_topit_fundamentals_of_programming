from collections import defaultdict

submissions = [
    ("anna", "lab_01", 5),
    ("boris", "lab_01", 4),
    ("anna", "lab_02", 5),
    ("daria", "lab_01", 3),
    ("boris", "lab_02", 5),
    ("anna", "lab_01", 4),
]

students = set()
labs = set()
labs_stud = {
    'lab_01': set(),
    'lab_02': set()
}
attempts = defaultdict(lambda: [])
best_results = defaultdict(lambda: 0)
labs_attempts = defaultdict(lambda: 0)
last = 0

for name, lab, res in submissions:
    students.add(name)
    labs.add(lab)
    if lab == 'lab_01': labs_stud['lab_01'].add(name)
    if lab == 'lab_02': labs_stud['lab_02'].add(name)
    attempts[name].append((lab,res))
    best_results[(name, lab)] = max(best_results[(name, lab)], res)
    labs_attempts[(name, lab)] += 1
    last += 1

print(f'Множество всех студентов: {students}')
print(f'Множество всех сданных лабораторных работ: {labs}')
print(f'Попытки студентов по лабораторным работам:\n{'\n'.join([f'{k}: {v}' for k, v in attempts.items()])}')
print(
    f'Словарь лучших результатов по ключу `(student, laboratory)`:\n{'\n'.join([f'{k}: {v}' for k, v in best_results.items()])}')
print(
    f'Словарь количества попыток для каждой пары `(student, laboratory)`:\n{'\n'.join([f'{k}: {v}' for k, v in labs_attempts.items()])}')
print('Студенты, которые сдавали обе работы:', labs_stud['lab_01'] & labs_stud['lab_02'])

print('\nПосле добавления новой записи:')
submissions.append(('victor', 'lab_03', 5))

for name, lab, res in submissions[last:]:
    students.add(name)
    labs.add(lab)
    if lab == 'lab_01': labs_stud['lab_01'].add(name)
    if lab == 'lab_02': labs_stud['lab_02'].add(name)
    attempts[name].append((lab,res))
    best_results[(name, lab)] = max(best_results[(name, lab)], res)
    labs_attempts[(name, lab)] += 1

print(f'Множество всех студентов: {students}')
print(f'Множество всех сданных лабораторных работ: {labs}')
print(f'Попытки студентов по лабораторным работам:\n{'\n'.join([f'{k}: {v}' for k, v in attempts.items()])}')
print(
    f'Словарь лучших результатов по ключу `(student, laboratory)`:\n{'\n'.join([f'{k}: {v}' for k, v in best_results.items()])}')
print(
    f'Словарь количества попыток для каждой пары `(student, laboratory)`:\n{'\n'.join([f'{k}: {v}' for k, v in labs_attempts.items()])}')
print('Студенты, которые сдавали обе работы:', labs_stud['lab_01'] & labs_stud['lab_02'])

print('\nПрактическое расширение:')
requests = 'student anna\nbest anna lab_01\nattempts boris lab_02\ncompleted lab_01'
for i in requests.split('\n'):
    request = i.strip().split()
    match request[0]:
        case 'student':
            name = request[1]
            print(f'{i}:', end=' ')
            print(*attempts[name], sep=', ')
        case 'best':
            name, lab = request[1:]
            print(f'{i}:', best_results[(name, lab)])
        case 'attempts':
            name, lab = request[1:]
            print(f'{i}:', labs_attempts[(name, lab)])
        case 'completed':
            lab = request[1]
            print(f'{i}:', labs_stud[lab])
        case _:
            print(f'{i}:', 'Ошибка. Такой запрос не поддерживается')
