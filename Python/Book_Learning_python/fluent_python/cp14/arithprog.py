class ArithmeticProgression:

    def __init__(self, begin, step, end=None):
        self.begin = begin
        self.step = step
        self.end = end
    
    def __iter__(self):
        result_type = type(self.begin + self.step)
        result = result_type(self.begin)
        
        infinite_loop = True if self.end is None else False
        index = 0

        while infinite_loop or result < self.end:
            yield result
            index += 1
            result = self.begin + self.step * index
            # Instead of using result = self.begin + self.step
            # we set a index variable to reduce the error of computing float number.
    
if __name__ == "__main__":
    ap = ArithmeticProgression(0, 1, 3)
    print(list(ap))

    ap = ArithmeticProgression(1, 0.5, 3)
    print(list(ap))

    ap = ArithmeticProgression(0, 1/3, 1)
    print(list(ap))

    from decimal import Decimal
    ap = ArithmeticProgression(0, Decimal('.1'), .3)
    print(list(ap))
    