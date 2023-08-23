"""
Ассоциация
"""


class Professor:
    def __init__(self, name) -> None:
        self.name = name
        

class Student:
    def __init__(self, name) -> None:
        self.name = name
        

class Course:
    def __init__(self, name, professor, students) -> None:
        self.name = name
        self.professor = professor
        self.students = students
        

pr1 = Professor("Aleksandr")
st1 = Student("Valysii")
st2 = Student("Anya")

course = Course("Hight Mathematic", pr1, [st1, st2])