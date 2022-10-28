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


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}


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


# best_student = Student('Roy', 'Eman', 'your_gender')
# best_student.finished_courses += ['Git']
# best_student.courses_in_progress += ['Python',]
#
# print(best_student.finished_courses)
# print(best_student.courses_in_progress)
# print(best_student.grades)
# print('1' * 10)
#
# cool_lecturer = Lecturer('Olga', 'Petrova')
# cool_lecturer.courses_attached += ['Python']
# cool_lecturer.courses_attached += ['Git']
# print(cool_lecturer.courses_attached)
# print('2' * 10)
#
# cool_reviewer = Reviewer('Vova', 'Topov')
# cool_reviewer.courses_attached += ['Python']
# cool_reviewer.rate_hw(best_student, 'Python', 10)
# cool_reviewer.rate_hw(best_student, 'Python', 10)
# cool_reviewer.rate_hw(best_student, 'Python', 10)
#
# print(best_student.grades)
# print(cool_reviewer.__dict__)
# print('3' * 10)
#
# print(best_student.grades)
# print('4' * 10)
#
# best_student.rate_lc(cool_lecturer, 'Python', 5)
# print(cool_lecturer.grades)
# best_student.rate_lc(cool_lecturer, 'Git', 8)
#
# print(cool_lecturer.grades)
# print(cool_lecturer.__dict__)
