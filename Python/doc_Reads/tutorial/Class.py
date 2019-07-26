class Complex:
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart
    def notify(self):
        print('Notify from Complex class.')

class DerivedFromComplex(Complex):
    def notify(self):
        print('Notify from DerivedFromComplex class.')


x = Complex(realpart=3.0, imagpart=4.5)
print(x.r, x.i)

y = DerivedFromComplex(10, 20)
print(y.r, y.i)


y.notify()
x.notify()
Complex.notify(y) #BaseClassName.methodname(self, arguments)