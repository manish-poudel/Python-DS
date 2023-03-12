# We will be demonstrating the power of inheritance using the progression class example which will produce sequence
# of number. By default, the subsequent number will be 1 added to the previous number. For example, 1, 2, (1+2),
# ...... However, other base class can override non-public methods called "_advance" to provide their own
# implementation.

# For more information, I have also included notes. => ./notes/
# Don't hesitate to email me at mspoudel92@gmail.com for any questions.
# Good luck with coding :) !!!

class Progression:

    def __init__(self, start=0):
        self.current = start

    # this method is responsible for producing the next element after called from
    # special named method __next__. Default implementation will add 1 to previous number.
    # Other base class can provide their own implementation
    def _advance(self):
        self.current = self.current + 1

    # Special named method called iterator to return the next element. If you don't
    # know about this method, please see the Python operator overloading concepts from python-primer directory
    def __next__(self):
        # Convention to stop iteration
        if self.current is None:
            return StopIteration()
        else:
            answer = self.current  # Store answer value
            self._advance()  # Advance the number for next iteration
            return answer  # Return value

    # Returning self as an iterator
    def __iter__(self):
        return self

    # Print progress up to n value
    def print_progression(self, n):
        print(' '.join(str(next(self)) for j in range(n)))
