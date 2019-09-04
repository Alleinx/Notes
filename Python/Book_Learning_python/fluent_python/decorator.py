def decorate(func):
    # will print out 'running target()'
    func()
    def inner():
        print('Running Inner')
    # will print out 'running Inner'
    inner()

@decorate
def target():
    print('Running target()')

# Equivlant to:
# target = decorate(target)

if __name__ == "__main__":
    target
