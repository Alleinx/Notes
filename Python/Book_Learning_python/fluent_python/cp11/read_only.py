class Point:
    
    def __init__(self, x, y):
        self.__x = float(x)
        self.__y = float(y)
    
    @property
    def x(self):
        return self.__x
    
    @property
    def y(self):
        return self.__y
    
    def __iter__(self):
        return (i for i in (self.x, self.y))
    
    def __repr__(self):
        return 'point: ({:.2f}, {:.2f})'.format(self.__x, self.__y)
        
if __name__ == "__main__":
    point = Point(10, 20)
    print(point)
    # point.x = 321
    # print.y = 123
    # Will raise AttributeError
    # print(point)
        