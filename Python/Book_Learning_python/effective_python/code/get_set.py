# This program demonstrates the usage of __get__() and __set__() or descriptor protocol.

# Yes, we can use @property, @property.setter, @property.deleter to add functionalities onto attribute.
# However, when we have too many attributes (e.g. 10), we need to define more than 20 methods.

# Instead, we could use ```__get__(), __set__()``` to handle attributes with similar behavior: which means we could put same behavior into ```__get__(), __set__()```. 

class Grade(object):
    def __init__(self):
        self._value = 0

    def __get__(self, instance, instance_type):
        return self._value

    def __set__(self, instance, value):
        if not (value >=0 and value <= 100):
            raise ValueError('Grade must be between 0,100')
        self._value = value

class Exam(object):
    def __init__(self):
        math_grade = Grade()
        writing_grade = Grade()
        science_grade = Grade()

if __name__ == '__main__':
    exam = Exam()
    exam.writing_grade = 40
    exam.math_grade = 50
    # Will be interpreted as Exam.__dict__['writting_grade'].__set__(exam, 40)

    print(exam.writing_grade)
    # Will be interpreted as print(Exam.__dict__['writting_grade'].__get__(exam, Exam))
    
    second_exam = Exam()
    second_exam.writing_grade = 70
    second_exam.math_grade = 80

    print('First writing grade' , exam.writing_grade)
    print('First math grade' , exam.math_grade)

    print('Second writing grade', second_exam.writing_grade)
    print('Second math grade', second_exam.math_grade)
