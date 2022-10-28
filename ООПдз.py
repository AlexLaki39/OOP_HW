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


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) a![](../../../0737~1/AppData/Local/Temp/10вопрос.jpg)nd course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'



best_student = Student('Roy', 'Eman', 'your_gender')
best_student.finished_courses += ['Git']
best_student.courses_in_progress += ['Python']


print(best_student.finished_courses)
print(best_student.courses_in_progress)
print(best_student.grades)

cool_mentor = Mentor('Olga', 'Petrova')
cool_mentor.courses_attached += ['Python']
print(cool_mentor.courses_attached)


cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)

print(best_student.grades)