class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id


class School:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        for s in self.students:
            if s.student_id == student.student_id:
                return False
        self.students.append(student)
        return True

    def remove_student(self, name):
        for i in range(len(self.students)):
            if self.students[i].name == name:
                self.students.pop(i)
                return True
        return False

    def list_students(self):
        for s in self.students:
            print(s.name, s.student_id)


school = School()
school.add_student(Student("Alex", "S001"))
school.add_student(Student("Bill", "S002"))
school.add_student(Student("Eva", "S001"))

school.list_students()
school.remove_student("Bob")
school.list_students()