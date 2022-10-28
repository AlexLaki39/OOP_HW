class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

    def rate_lc(self, lecturer, course, grade):
        if isinstance(lecturer,
                      Lecturer) and course in lecturer.courses_attached \
                and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def _average_grade_hw(self):
        list_1 = []
        for value in self.grades.values():
            for item in value:
                list_1.append(item)
        avrg = sum(list_1) / len(list_1)
        return avrg

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}' \
              f'\nСредняя оценка за домашние задания: {round(self._average_grade_hw(), 2)}' \
              f'\nКурсы в процессе изучения: {", ".join(self.courses_in_progress)}' \
              f'\nЗавершенные курсы: {", ".join(self.finished_courses)}'
        return res

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Такого студента нет!')
            return
        return self._average_grade_hw() < other._average_grade_hw()


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def _average_grade_lc(self):
        list_1 = []
        for value in self.grades.values():
            for item in value:
                list_1.append(item)
        avrg = sum(list_1) / len(list_1)
        return avrg

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}' \
              f'\nСредняя оценка за лекции: {round(self._average_grade_lc(), 2)}'
        return res

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Такого преподавателя нет!')
            return
        return self._average_grade_lc() < other._average_grade_lc()


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached \
                and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}'
        return res


student_1 = Student('Olga', 'Petrova', 'F')
student_1.finished_courses += ['Git']
student_1.courses_in_progress += ['Python']
student_1.add_courses('Java')

student_2 = Student('Egor', 'Popov', 'M')
student_2.finished_courses += ['SQL']
student_2.courses_in_progress += ['Django']
student_2.add_courses('Go')

lecturer_1 = Lecturer('Anna', 'Sokolova')
lecturer_1.courses_attached += ['Python']

lecturer_2 = Lecturer('Oleg', 'Ivanov')
lecturer_2.courses_attached += ['Django']

reviewer_1 = Reviewer('Anton', 'Rogov')
reviewer_1.courses_attached += ['Python']
reviewer_1.rate_hw(student_1, 'Python', 5)
reviewer_1.rate_hw(student_1, 'Python', 8)
reviewer_1.rate_hw(student_1, 'Python', 10)

reviewer_2 = Reviewer('Ivan', 'Orlov')
reviewer_2.courses_attached += ['Django']
reviewer_2.rate_hw(student_2, 'Django', 3)
reviewer_2.rate_hw(student_2, 'Django', 10)
reviewer_2.rate_hw(student_2, 'Django', 6)

student_1.rate_lc(lecturer_1, 'Python', 10)
student_1.rate_lc(lecturer_1, 'Python', 8)
student_1.rate_lc(lecturer_1, 'Python', 8)

student_2.rate_lc(lecturer_2, 'Django', 4)
student_2.rate_lc(lecturer_2, 'Django', 8)
student_2.rate_lc(lecturer_2, 'Django', 2)

print(reviewer_1, reviewer_2, student_1, student_2, lecturer_1, lecturer_2, sep='\n\n')

print(student_1 > student_2)
print(lecturer_1 == lecturer_2)

list_students = [student_1, student_2]
list_lecturers = [lecturer_1, lecturer_2]


def course_avrg_grade_st(lst_std, course):
    lst = []
    for person in lst_std:
        for key, value in person.grades.items():
            if key == course:
                for item in value:
                    lst.append(item)
    r = sum(lst) / len(lst)
    print(f'Средняя оценка по студентам за дз по курсу {course}: {round(r, 2)}')


def lecture_avrg_grade_lct(lst_lct, course):
    lst = []
    for person in lst_lct:
        for key, value in person.grades.items():
            if key == course:
                for item in value:
                    lst.append(item)
    r = sum(lst) / len(lst)
    print(f'Средняя оценка по лекторам за лекции по курсу {course}: {round(r, 2)}')


course_avrg_grade_st(list_students, 'Python')

lecture_avrg_grade_lct(list_lecturers, 'Django')
