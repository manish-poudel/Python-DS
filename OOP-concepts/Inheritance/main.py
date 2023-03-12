# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from Progression import Progression


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


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
