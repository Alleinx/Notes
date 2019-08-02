#Dict play
users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
        'fav_language': ['python', 'C++']
    },

    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
        'fav_language': ['Swift', 'Java']
    }
}

for username, user_info in users.items():
    print('\nUsername:', username)
    full_name = user_info['first'] + " " + user_info['last']
    location = user_info['location']

    print('  Full name:', full_name.title())
    print('  Location:', location.title())

    print('  Favorite Language:', end='  ')
    for language in user_info['fav_language']:
        print(language, end='  ')

print()
# Func play

def test_var_dict(**args):
    print(type(args))

    test_dict = {}
    for k, v in args.items():
        print('Key:', k + ', Value:', v)
        test_dict[k] = v

    return test_dict

# Format 1
result = test_var_dict(location = 'princeton', field = 'physics')
print(result)

# Format 2
result = test_var_dict(**users)
print(result)

# ------------------------------
def test_var_args(*args):
    res_list = []

    for arg in args:
        res_list.append(arg)
    
    return res_list

test = [1,2,3,4]

# Format 1
print(test_var_args(*test))

# Format 2
# test_var_args(var1, var2, ...)

# Note: Different from Format 1!
print(test_var_args(test))

# Class Inheritance:

class Car():
    
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    
    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        print('This car has ' + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print('You can\'t roll back an odometer!')

    def increment_odometer(self, miles):
        self.odometer_reading += miles


class ElectricCar(Car):
    
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        # Or: Car.__init__(self, make, model, year)

my_tesla = ElectricCar('Tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())