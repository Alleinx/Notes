# @decorate
# def target():
#   pass
# is equal to:
# target = decorate(target)
# target() -> decorate(target)()

def decorate(func):
    # will print out 'running target()'
    func()
    def inner():
        print('Running Inner')
    # will print out 'running Inner'
    inner()
    return inner

@decorate
def outer():
    print('Running target()')

# Equivlant to:
# outer = decorate(outer)

if __name__ == "__main__":
    outer()
