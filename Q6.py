class Student:
    def __init__(self):
        self.grade = None

    def view_grade(self):
        print(self.grade)


class Teacher:
    def assign_grade(self, student, grade):
        student.grade = grade


student1 = Student()
teacher1 = Teacher()

teacher1.assign_grade(student1, 80)
student1.view_grade()