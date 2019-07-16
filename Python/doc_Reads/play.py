def f(ham: str, eggs: str = 'eggs') -> str:
    print("annotations:", f.__annotations__)
    print("arguments:", ham, eggs)
    return ham + ' and' + eggs

