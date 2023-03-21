# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from Progression import Progression
from ArithmeticProgression import ArithmeticProgression
from GeometricProgression import GeometricProgression
from FibonacciProgression import FibonacciProgression


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    progression = Progression(start=0)
    iterObj = iter(progression)
    print(next(iterObj))  # 0
    print(next(iterObj))  # 1
    print(next(iterObj))  # 2

    progression2 = Progression(start=0)
    progression2.print_progression(10)  # 0 1 2 3 4 5 6 7 8 9

    # Test AP
    arithmeticProgression = ArithmeticProgression(4)
    arithmeticProgression.print_progression(10)  # 0 4 8 12 16 20 24 28 32 36

    arithmeticProgression = ArithmeticProgression(10, 1)
    arithmeticProgression.print_progression(5)  # 1 11 21 31 41

    # Test GP
    geometricProgression = GeometricProgression()  # Let's use default param
    geometricProgression.print_progression(10)  # 1 2 4 8 16 32 64 128 256 512

    geometricProgression = GeometricProgression(3, 10)
    geometricProgression.print_progression(5)  # 10 30 90 270 810

    fibonacciProgression = FibonacciProgression()
    fibonacciProgression.print_progression(9)  # 0 1 1 2 3 5 8 13 21

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
