# Each value of a Fibonacci series is the
# sum of the two most recent values. for eg , 0 1 1 2 3 5 8 13 21

from Progression import Progression


class FibonacciProgression(Progression):

    def __init__(self):
        super().__init__(0)
        self._next = 1  # Defne next value

    def _advance(self):
        self.current, self._next = self._next, self.current + self._next  # switch current to next, and add next
        # value to itself with current value to be used by current for later in the future.
