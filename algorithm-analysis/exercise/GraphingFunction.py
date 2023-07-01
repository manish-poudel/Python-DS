# Graph the functions 8n, 4nlogn, 2n2, n3, and 2n using a logarithmic scale
# for the x- and y-axes; that is, if the function value f(n) is y, plot this as a
# point with x-coordinate at logn and y-coordinate at logy.
import math

import matplotlib.pyplot as plt


def graph(x, y):
    # plotting the points
    plt.plot(x, y)

    # naming the x-axis
    plt.xlabel('x - axis')
    # naming the y-axis
    plt.ylabel('y - axis')

    # giving a title to my graph
    plt.title('My first graph!')

    # function to show the plot
    plt.show()


if __name__ == '__main__':
    xaxis = [1, 2, 3, 4, 5, 6]
    yaxis = list(map(lambda x: x*8, xaxis))
    graph(list(map(lambda x: math.log(x), xaxis)), list(map(lambda y: math.log(y), yaxis)))
