"""
Exercise 7.1.
Copy the loop from Section 7.5 and encapsulate it in a function called mysqrt
that takes a as a parameter, chooses a reasonable value of x, and returns an
estimate of the square root of a.
To test it, write a function named test_square_root that prints a table like this:
a   mysqrt(a)      math.sqrt(a)   diff
-   ---------      ------------   ----
1.0 1.0            1.0            0.0
2.0 1.41421356237  1.41421356237  2.22044604925e-16
3.0 1.73205080757  1.73205080757  0.0
4.0 2.0            2.0            0.0
5.0 2.2360679775   2.2360679775   0.0
6.0 2.44948974278  2.44948974278  0.0
7.0 2.64575131106  2.64575131106  0.0
8.0 2.82842712475  2.82842712475  4.4408920985e-16
9.0 3.0            3.0            0.0
The first column is a number, a;
the second column is the square root of a computed with mysqrt;
the third column is the square root computed by math.sqrt;
the fourth column is the absolute value of the difference between the two estimates.

This example the table is formated identical.
"""

import math
epsilon = 0.0000000001

def mysqrt(a):
    x = a
    while True:
        y = (x + a/x) / 2
        if abs(y-x) < epsilon:
            return y
            break
        x = y

def right_digit(n):
    trunc = f'{n:.11f}'
    dig = trunc [len(trunc)-1]
    return dig

def test_square_root(n):
    print('a', ' '*1, 'mysqrt(a)', ' '*3, 'math.sqrt(a)', ' diff')
    print('-', ' '*1, '-'*9, ' '*3, '-'*12, ' ' + '-'*4)

    for i in range(9):
        x=i+1

        print(f'{x:0.1f}', end=' ')

        if mysqrt(x) - int(mysqrt(x)) < 0.001:
            y=1
        elif right_digit(mysqrt(x)) == '0':
            y=10
        else:
            y=11

        print(f'{mysqrt(x):<13.{y}f}', end=' ')
        print(f'{mysqrt(x):<13.{y}f}', end=' ')

        diff= math.sqrt(x) - mysqrt(x)
        print(f'{diff:.12g}')

test_square_root(9)

