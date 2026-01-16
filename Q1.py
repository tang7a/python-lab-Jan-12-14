class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def introduce(self):
        print(f"Hi, my name is {self.name} and I am in grade {self.grade}")


s1 = Student("Alex", 10)
s2 = Student("Bill", 15)

s1.introduce()
s2.introduce()