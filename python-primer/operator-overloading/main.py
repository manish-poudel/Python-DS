# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from Vector import Vector
from SequenceIterator import SequenceIterator


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    vector = Vector(5)
    vector = vector + [2, 3, 4, 5, 6]
    print(vector)

    sq = SequenceIterator([1, 2, 3, 4, 5, 6])
    sq_iter = iter(sq)
    print(next(sq_iter))
    print(next(sq_iter))
    print(next(sq_iter))
    print(next(sq_iter))
    print(next(sq_iter))
    print(next(sq_iter))
    print(next(sq_iter))
    print(next(sq_iter))

    print(len(sq))

    i = 0
    while i < len(sq):
        print(sq_iter[i])
        i = i + 1




# See PyCharm help at https://www.jetbrains.com/help/pycharm/
