def f(ham: str, eggs: str = 'eggs') -> str:
    print("annotations:", f.__annotations__)
    print("arguments:", ham, eggs)
    return ham + ' and' + eggs

def test(x: int, y: int) -> int:
    x.append(10)
    y.append(10)

    return 'test'

if __name__ == "__main__":

    t1 = []
    t2 = []
    y = test(t1, t2)
    
    print(t1, t2)
    print(type(y))