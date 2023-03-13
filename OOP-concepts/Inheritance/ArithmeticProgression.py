# Arithmetic Progress is about incrementing previous value by constant such that a(n) = a(n-1) + c,
# where n is the current position and c is the constant value
# for example, incrementing by constant 4 will be 0, 4, 8, .....

from Progression import Progression


# Progression as a base class
class ArithmeticProgression(Progression):

    def __init__(self, increment=1, start=0):
        super().__init__(start)  # pass current value to the super class
        self._increment = increment

    # Overriding advance with our implementation
    def _advance(self):
        self.current += self._increment
