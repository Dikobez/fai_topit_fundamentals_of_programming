from random import randint, choice


def describe_work(work_type):
    match work_type:
        case 'exam':
            work = 'экзаменационная работа'
        case 'project':
            work = 'проектная работа'
        case 'practice':
            work = 'практическая работа'
        case _:
            work = 'неизвестная работа'
    return work


def get_level(result):
    if 0 <= result <= 59:
        level_id = 0
    elif 60 <= result <= 74:
        level_id = 1
    elif 75 <= result <= 89:
        level_id = 2
    else:
        level_id = 3

    return level_id


def adjust_level(absences, level_id):
    levels = ['недостаточный', 'удовлетворительный', 'хороший', 'отличный']
    if absences > 3 and level_id > 0:
        level_id -= 1
    return levels[level_id]


def classification(result, work_type, absences):
    if not (type(result) == int and 0 <= result <= 100 and type(absences) == int and 0 <= absences <= 5):
        return None

    level_id = get_level(result)
    level = adjust_level(absences, level_id)
    work = describe_work(work_type)

    return work, level


def sumup():
    data = []
    for i in range(10):
        scr = randint(0, 100)  # list(map(int,['0', '59', '60', '74', '75', '89', '90', '100']))[i]
        absnt = randint(0, 5)
        wrk = choice(['exam', 'project', 'practice', 'another'])
        data.append((scr, wrk, absnt))
    studs = {
        "недостаточный": 0,
        "удовлетворительный": 0,
        "хороший": 0,
        "отличный": 0,
    }
    for sc, wt, ab in data:
        result = classification(sc, wt, ab)
        if result is None:
            print(sc, wt, ab, "| Input error")
            continue
        w, lvl = result
        print(sc, wt, ab, f" | Тип работы: {w}. Уровень: {lvl}" )
        studs[lvl] += 1

    summary = "\n".join(f"{key}: {value}" for key, value in studs.items())

    print(
        f"Всего студентов: {len(data)}\n"
        f"Студентов каждого уровня:\n{summary}"
    )


if __name__ == "__main__":
    sumup()
    # for i in range(8):
    #     scr = randint(0, 100) # list(map(int,['0', '59', '60', '74', '75', '89', '90', '100']))[i]
    #     absnt = randint(0, 5)
    #     wrk = choice(['exam', 'project', 'practice', 'another'])
    #     data.append((scr, wrk, absnt))

    # for sc, wt, ab in data:
    #     w, lvl = classification(sc, wt, ab)
    #     print(sc, wt, ab, '  |  ', f'Тип работы: {w}. Уровень: {lvl}')
