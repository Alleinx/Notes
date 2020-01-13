class Screen:
    def __init__(self):
        self._resolution = 1080
        self._width = -1
        self._height = -1

    @property
    # getter
    def width(self):
        return self._width
    
    @property
    # getter
    def height(self):
        return self._height
    
    @property
    # getter, no setter; 
    # Read-only property.
    def resolution(self):
        return self._resolution
    
    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise ValueError('Width must be an integer.')
        if value <= 0:
            raise ValueError('Width must greater than 0.')
        self._height = value

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise ValueError('Width must be an integer.')
        if value <= 0:
            raise ValueError('Width must greater than 0.')
        
        self._height = value

s = Screen()
s.width = 1024
s.height = 768
print('resolution =', s.resolution)
print('width =', s.width, 'height =', s.height)