# Geometric Progress is about multiplying preceding value by constant called base


from Progression import Progression


# Progression as a base class
class GeometricProgression(Progression):

    def __init__(self, base=2, start=1):
        super().__init__(start)  # pass current value to the super class
        self._base = base

    # Overriding advance with our implementation
    def _advance(self):
        self.current *= self._base
