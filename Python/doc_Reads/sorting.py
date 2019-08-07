student_tuples = [
    ('john', 'A', 15),
    ('jane', 'C', 12),
    ('dave', 'B', 10)
]

# sort by name
print(sorted(student_tuples, key = lambda student: student[0]))

# sort by grade
print(sorted(student_tuples, key = lambda student: student[1]))

# sort by age
print(sorted(student_tuples, key = lambda student: student[2]))

# Also works
class Student:
    def __init__(self, name, grade, age):
        self.name = name
        self.grade = grade
        self.age = age

    def __repr__(self):
        return repr((self.name, self.grade, self.age))

student_obj = [
    Student('john', 'A', 15),
    Student('jane', 'C', 12),
    Student('dave', 'B', 10)
]

print(sorted(student_obj, key = lambda student : student.age))

# --------
# Or could use lib

from operator import itemgetter, attrgetter

print(sorted(student_tuples, key=itemgetter(1,2)))
print(sorted(student_obj, key=attrgetter('grade', 'age')))