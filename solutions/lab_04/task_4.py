from dataclasses import dataclass


@dataclass()
class Submission:
    student_id: str
    laboratory_id: str
    attempt: int
    score: float
    comment: str = ""

    def __post_init__(self):
        if self.student_id == "":
            raise ValueError("Идентификатор студента не может быть пустым")
        if self.laboratory_id == "":
            raise ValueError("Идентификатор работы не может быть пустым")
        if self.attempt <= 0:
            raise ValueError("Номер попытки должен быть положительным")
        if not (0 <= self.score <= 100):
            raise ValueError("Результат должен находится в диапазоне от 0 до 100")


class Student:
    def __init__(self, student_id: str, name: str):
        if student_id == "":
            raise ValueError("Идентификатор студента не может быть пустым")
        self.student_id = student_id
        self._submissions = []
        self.name = name

    @property
    def submissions(self):
        return tuple(self._submissions)

    @property
    def average_score(self) -> float:
        if not self._submissions:
            return 0.0
        scores = [sub.score for sub in self._submissions]
        return sum(scores) / len(scores)

    @classmethod
    def from_full_name(cls, student_id: str, full_name: str) -> "Student":
        if student_id.strip() == "":
            raise ValueError("Идентификатор студента не может быть пустым")
        cleaned_name = " ".join(full_name.split())
        return cls(student_id=student_id, name=cleaned_name)

    @staticmethod
    def is_valid_id(student_id: str) -> bool:
        return isinstance(student_id, str) and bool(student_id.strip())

    def sorted_submissions(self, by_attempt: bool = True) -> list["Submission"]:
        if by_attempt:
            return sorted(self._submissions, key=lambda x: (x.attempt, x.score))
        else:
            return sorted(self._submissions, key=lambda x: (x.score, x.attempt))

    def add_submission(self, submission: "Submission"):
        if submission.student_id != self.student_id:
            raise ValueError(f'Работа принадлежит студенту {submission.student_id} а не {self.student_id}')
        self._submissions.append(submission)

    def best_score(self, laboratory_id: str) -> float:
        scores = [sub.score for sub in self._submissions if sub.laboratory_id == laboratory_id]
        return max(scores) if scores else 0.0

    def __len__(self) -> int:
        return len(self._submissions)

    def __iter__(self):
        return iter(self._submissions)

    def __str__(self) -> str:
        return f"{self.name} ({self.student_id}) - попыток: {len(self)}, средний балл: {self.average_score:.1f}"

    def __repr__(self) -> str:
        return f"Student(student_id={self.student_id!r}, name={self.name!r})"


class Course:
    def __init__(self):
        self._students = {}  # student_id: Student

    def add_student(self, student):
        if student.student_id in self._students:
            raise ValueError("Студенты не могут повторяться")
        self._students[student.student_id] = student

    def get_student(self, student_id):
        if student_id not in self._students:
            raise ValueError("Студент не найден")
        return self._students[student_id]

    def submit(self, submission):
        student = self.get_student(submission.student_id)
        student.add_submission(submission)

    def top_students(self, limit: int = 3):
        sort_stud = sorted(self._students.values(), key=lambda x: x.average_score,
                           reverse=True)  # sorted создает новый список, не меняя исходный словарь
        return sort_stud[:limit]

    def __contains__(self, student_id):
        return student_id in self._students

    def __len__(self):
        return len(self._students)

    def __iter__(self):
        return iter(self._students.values())


if __name__ == "__main__":

    # Создаём курс
    course = Course()

    # Создаём студентов
    student1 = Student("S001", "Иван Иванов")
    student2 = Student.from_full_name("S002", "Петр Петров")
    student3 = Student.from_full_name("S003", "Евгений Вахранев")
    student4 = Student("S004", "Джон Сина")
    student5 = Student.from_full_name("S005", "Иван Ведерников")

    # Добавляем в курс
    course.add_student(student1)
    course.add_student(student2)
    course.add_student(student3)
    course.add_student(student4)
    course.add_student(student5)

    # Создаём работы
    work1 = Submission("S001", "lab_01", 1, 85.0)
    work2 = Submission("S005", "lab_02", 1, 90.7)
    work3 = Submission("S003", "lab_03", 1, 75.0)
    work4 = Submission("S003", "lab_04", 1, 89.5)
    work5 = Submission("S004", "lab_04", 1, 65.1)
    work6 = Submission("S002", "lab_02", 1, 81.4)
    work7 = Submission("S001", "lab_03", 1, 65.1)
    work8 = Submission("S003", "lab_01", 1, 81.4, "work smart, not hard")
    work9 = Submission("S005", "lab_02", 2, 92.7)

    # Сдаём работы через курс
    course.submit(work1)
    course.submit(work2)
    course.submit(work3)
    course.submit(work4)
    course.submit(work5)
    course.submit(work6)
    course.submit(work7)
    course.submit(work8)
    course.submit(work9)

    print('----- методы класса Course -----')
    print(f'Количество студентов на курсе: {len(course)}')
    print(f'Топ студентов на курсе: {course.top_students()}')
    print(f'Есть ли студент S005 на курсе: {"S005" in course}')
    print(f'Есть ли студент S010 на курсе: {"S010" in course}')
    print('\nCourse как итерируемый объект (список студентов):')
    for stu in course.__iter__():
        print(stu)

    print('\n----- методы класса Student -----')
    print('Студенты:')
    print(student1.__repr__())
    print(student2.__repr__())
    print(student3.__repr__())
    print(student4.__repr__())
    print(student5.__repr__())

    print(f'\nКоличество работ студента S003: {len(student3)}')
    print(f'Работы студента S003: {student3.submissions}')
    print('\nstudent3 как итерируемый объект (его лабораторные работы):')
    for wrk in student3.__iter__():
        print(wrk)

    print('\nПроверка на некорректные данные:')
    try:
        Student.from_full_name("", "Bz Px")
        assert False, "1 Ожидалась ValueError"
    except ValueError as e:
        assert str(e) == "Идентификатор студента не может быть пустым"
        print('Пустой ID (.from_full_name) - OK')

    try:
        Student("", "Bz Px")
        assert False, "2 Ожидалась ValueError"
    except ValueError as e:
        assert str(e) == "Идентификатор студента не может быть пустым"
        print('Пустой ID (default) - OK')

    try:
        Submission("S001", "lab_01", -1, 85.0)
        assert False, "Ожидалась ValueError"
    except ValueError as e:
        assert str(e) == "Номер попытки должен быть положительным"
        print('Отрицательное количество попыток - OK')
    try:
        Submission("S001", "lab_01", 1, 150.0)
        assert False, "Ожидалась ValueError"
    except ValueError as e:
        assert str(e) == "Результат должен находится в диапазоне от 0 до 100"
        print('Балл за работу вне диапазона - OK')

    print('\n----- методы класса Submission -----')
    work10 = Submission("S001", "lab_01", 2, 84.0)
    work11 = Submission("S001", "lab_01", 3, 84.0)
    work12 = Submission("S001", "lab_01", 4, 90.0)
    work13 = Submission("S001", "lab_01", 4, 90.0)

    course.submit(work10)
    course.submit(work11)
    course.submit(work12)

    print(f'work10 == work12: {work10 == work11}')
    print(f'work14 == work13: {work13 == work12}')

    print('\nПроверка сортировки:')
    print(student1.submissions)
    sorted_by_attempt = student1.sorted_submissions(by_attempt=True)
    for work in sorted_by_attempt:
        print(f"Попытка {work.attempt}, балл {work.score} - лабораторная {work.laboratory_id}")
    print('Исходный список не изменился: ', [w.attempt for w in student1.submissions])
