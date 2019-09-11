import abc

class Tombola(abc.ABC):

    @abc.abstractmethod
    # this rerepresent that the following function is a abstract function
    def load(self, iterable):
        """Add element from iterable object"""
    
    @abc.abstractmethod
    def pick(self):
        """
        randomly choose a element, remove it and return to the caller.
        If there is no available element, should raise LookupError.
        """
    
    def loaded(self):
        """
        return True if there is at least one element in the container,
        otherwise, return False
        """
        return bool(self.inspect())

    def inspect(self):
        """
        return a ordered tuple of currently existed elements.
        """
        items = []
        while True:
            try:
                items.append(self.pick())
            except LookupError:
                break
        self.load(items)
        # Because we don't know how the subclass will store their elements, we could
        # clear Tombola by calling pick() and store all the elements back.
        # Also, subclasses of Tombola could override this method.
        return tuple(sorted(items))

