'''You are given N identical eggs, and you have access to a K-floored building from 1 to K. There
exists a floor f where 0 <= f <= K such that any egg dropped from a floor higher than f will
break, and any egg dropped from or below floor f will not break.
There are few rules which are given below.
a) An egg that survives a fall can be used again.
b) A broken egg must be discarded.
c) The effect of a fall is the same for all eggs.
d) If the egg doesn't break at a certain floor, it will not break at any floor below.
e) If the eggs break at a certain floor, it will break at any floor above.
f) Return the minimum number of moves to determine with certainty what the value of f is.
'''

def eggDrop(n,k):
    table = [[0 for _ in range(k+1)] for _ in range (n+1)]

    #Base cases
    for j in range (n+1):
        table[1][j] = j

    for i in range (k+1):
        table[i][0] = 0
        table[i][1] = 1