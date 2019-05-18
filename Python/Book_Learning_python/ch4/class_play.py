class worker:
    def __init__(self, name, pay):
        self.name = name
        self.salary = pay

    def last_name(self):
        return self.name.split()[-1]

    def giveRaise(self, percent):
        self.salary *= (1.0 + percent)


if __name__ == "__main__":
    christopher = worker('John Smith', 10000)
    
    print(christopher.last_name())
    print(christopher.salary)
    christopher.giveRaise(0.5)
    print(christopher.salary)
