def mean(values: list) -> float:
    if not values:
        raise ValueError("Empty list")
    return sum(values) / len(values)


def minimum(values):
    if not values:
        raise ValueError("Empty list")
    mn = float('inf')
    for i in values:
        if i < mn:
            mn = i
    return mn


def maximum(values):
    if not values:
        raise ValueError("Empty list")
    mx = -float('inf')
    for i in values:
        if i > mx:
            mx = i
    return mx


def classify(score):
    if score > 100 or score < 0:
        raise ValueError("Wrong value")
    levels = ['недостаточный', 'удовлетворительный', 'хороший', 'отличный', 'No data']
    if 0 <= score < 60:
        level_id = 0
    elif 60 <= score < 75:
        level_id = 1
    elif 75 <= score < 90:
        level_id = 2
    else:
        level_id = 3
    return levels[level_id]


def student_summary(name, results):
    if not name:
        raise ValueError("Empty name")
    if not results:
        sumup = {
            'name': name,
            'mean': -1,
            'minimum': None,
            'maximum': None,
            'category': 'No data'
        }
        return sumup
    mean_val = mean(results)
    min_val = minimum(results)
    max_val = maximum(results)
    cat = classify(mean_val)
    sumup = {
        'name': name,
        'mean': mean_val,
        'minimum': min_val,
        'maximum': max_val,
        'category': cat
    }
    return sumup


def find_top_students(students):
    means = []
    for name, result in students.items():
        stud_data = student_summary(name, result)
        means.append((stud_data['mean'], name))

    means.sort(reverse=True)
    highest_score = means[0][0]
    leads = []

    for score, name in means:
        if score == highest_score:
            leads.append(name)
    return leads


def group_summary(students):
    means = []
    cats = {
        'недостаточный': 0,
        'удовлетворительный': 0,
        'хороший': 0,
        'отличный': 0,
        'No data': 0
    }
    students_rating = students.copy()
    if not students:
        return None, [], cats, -1, {}
    means_for = []
    for name, result in students.items():
        stud_data = student_summary(name, result)
        means.append((stud_data['mean'], name))
        cats[stud_data['category']] += 1
        means_for += students[name]

    means.sort(reverse=True)
    highest_score = means[0][0]

    gen_mean = mean(means_for)
    leads = find_top_students(students)

    for i, (score, name) in enumerate(means):
        students_rating[name] = i + 1

    return highest_score, leads, cats, gen_mean, students_rating


def format_report(student_data, group_data):
    highest_score, leads, cats, gen_mean, students_rating = group_summary(group_data)

    output_group = f'''leaders with score {highest_score}: {', '.join(leads)}
\nstudents in categories:
    недостаточный: {cats['недостаточный']}
    удовлетворительный: {cats['удовлетворительный']}
    хороший: {cats['хороший']}
    отличный: {cats['отличный']}               
\nmean score of whole group: {gen_mean:.2f}
\nstudents rating:
{'\n'.join([f"{nm}: {val}" for nm, val in students_rating.items()])}\n                             
'''

    output_students = ''
    for out in student_data:
        output_students += '\n'.join(
            [f'{info}: {data}' if info != 'mean' else f'{info}: {data:.2f}' for info, data in out.items()]) + '\n\n'

    return output_group + output_students


students = {
    "Анна": [78, 91, 84, 88],
    "Борис": [60, 72, 68],
    "Дарья": [95, 93, 97, 90],
    "Илья": [55, 61],
}

students1 = {
    "Анна": [78, 91, 84, 88],
}

students2 = {
    "Анна": [78, 91, 84, 88],
    "Борис": [66, 95, 86, 94],
    "Дарья": [85.25],
    "Илья": [89.5],
}

students3 = {

}

students4 = {
    "Анна": [78, 91, 84, 88],
    "Борис": [],
    "Дарья": [95, 93, 97, 90],
    "Илья": [55, 61],
}

students5 = {
    "Анна": [60, 60, 60],
    "Борис": [74, 74],
    "Дарья": [95, 85, 90],
    "Илья": [55, 61],
}

for i, group in enumerate([students, students1, students2, students3, students4, students5]):
    students_summary = [student_summary(n, r) for n, r in group.items()]
    print(f'================ students{i} ================')
    print(format_report(students_summary, group))
