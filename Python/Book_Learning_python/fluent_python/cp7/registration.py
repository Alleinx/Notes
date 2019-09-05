registry = []

def register(func):
    print('running register(%s)' % func)
    registry.append(func)
    return func

@register
def f1():
    print('running f1()')

@register
def f2():
    print('running f2()')

def f3():
    print('running f3()')

def main():
    # f1 = register(f1)
    # f2 = register(f2)
    # decorator is executed when the module is loaded.
    print('running main()')
    print('registry ->', registry)
    f1()
    f2()
    f3()

if __name__ == "__main__":
    main()