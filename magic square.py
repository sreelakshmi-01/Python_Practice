'''A magic square of order n is an arrangement of n^2
numbers, usually distinct integers, in a square,
such that the n numbers in all rows, all columns, and both diagonals sum to the same constant. A
magic square contains the integers from 1 to n^2. Create a magic square of a given order N.'''

import numpy as np

def odd_magical_square(n):
    mag_sq = np.zeros((n,n), dtype = int)

    i,j = 0,n//2
    for num in range (1, n*n+1):
        mag_sq[i][j] = num
        i = i-1
        j = j+1

        if num % n == 0:
            i = i+2
            j = j-1
        elif i<0:
            i = n-1
        elif j==n:
            j = 0
    print(mag_sq)

def doubly_even_number(n):
    mag_sq = np.arange(1,n*n+1).reshape(n,n)
    for i in range(n):
        for j in range(n):
            if (i%4 == j%4) or ((i%4)+(j%4)==3):
                mag_sq[i][j] = n * n + 1 - mag_sq[i][j]
    print(mag_sq)
