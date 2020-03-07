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
# perform sorting firstly on attr 'grade', then on 'age'.
print(sorted(student_obj, key=attrgetter('grade', 'age')))

# Stable Sorting
# Stability in sorting: https://www.geeksforgeeks.org/stability-in-sorting-algorithms/

data = [('red', 1), ('blue', 1), ('red', 2), ('blue', 2)]
print(sorted(data, key = itemgetter(0)))

# With stable sorting, we could perform DESC first on 'grade' then ASC on 'age'

# sort on secondary key, ASC
s = sorted(student_obj, key=attrgetter('age'))
# sort on primary key, DESC
print(sorted(s, key = attrgetter('grade'), reverse=True))

# reverse parameter and reversed() could reserve stability.
standard_way = sorted(data, key=itemgetter(0), reverse=True)
double_reversed = list(reversed(sorted(reversed(data), key=itemgetter(0))))
assert standard_way == double_reversed