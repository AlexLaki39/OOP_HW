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
        list = []
        for value in self.grades.values():
            for item in value:
               list.append(item)
        avrg = sum(list) / len(list)
        return avrg

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}' \
              f'\nСредняя оценка за домашние задания: {self._average_grade_hw()}' \
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
        list = []
        for value in self.grades.values():
            for item in value:
               list.append(item)
        avrg = sum(list) / len(list)
        return avrg

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}' \
              f'\nСредняя оценка за лекции: {self._average_grade_lc()} '
        return res


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

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Такого преподавателя нет!')
            return
        return self._average_grade_lc() < other._average_grade_lc()

