# This program demonstrate the usage of classmethod
class InputData:

    def read(self):
        raise NotImplementedError('read method is not supported by current cls')

class PathInputData(InputData):

    def __init__(self, path):
        super().__init__()
        self.path = path
    
    def read(self):
        return open(self.path).read()

# worker = InputData()
# worker.read()

# ---------------------------------------------------------
class Date(object):

    def __init__(self, day=0, month=0, year=0):
        self.day = day
        self.month = month
        self.year = year

    @classmethod
    def build_from_string(cls, date_as_string):
        '''
        Use classmethod to overload the constructor
        '''
        day, month, year = map(int, date_as_string.split('-'))
        date = cls(day, month, year)
        return date

date = Date.build_from_string('11-09-2012')
print(date.year, date.month, date.day)
