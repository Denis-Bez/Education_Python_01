
# Task analysis: https://www.youtube.com/watch?v=GhiRlhPlJ9Q

# We have area size m, n. Robot can stepping only right and up. How mach ways has robot to door?
"""
            m
  ____ ____ ____ ____ ____
 |    |    |    |    |door|
 |____|____|____|____|____|
 |    |    |    |    |    |
 |____|____|____|____|____|
n|    |    |    |    |    |
 |____|____|____|____|____|
 |robo|    |    |    |    |
 |____|____|____|____|____|

"""
# Example: if m = 3, n = 2, then number of ways = 3


# Recursion method
# contition: paths(n, m) = paths(m-1, n) + paths(m, n-1)
# base of recursion (a simple case for wich we know answer): 
    # 1) paths(x, 0) = paths(0, x) = 0, where 'x' - is robot's coordinate
    # 2) path(1, 1) = 1
# but working time = O(2^(n+m))

def rec(m, n):
    
    if m == 0 or n == 0:
        return 0
    if m == 1 and n == 1:
        return 1

    return rec(m-1, n) + rec(m, n-1)


def dynamic(m, n, lst):
    if m == 0 or n == 0:
        return 0
    if m == 1 and n == 1:
        return 1
    
    if (lst[n][m] != 0 ):
        return lst[n][m]
    lst[n][m] = dynamic(m-1, n, lst) + dynamic(m, n-1, lst)
    return lst[n][m]


def main():
    n = 4
    m = 5
    lst =  [[0]*(m+1) for i in range(n+1)] # Only for 'dynamic'
    
    path = dynamic(m, n, lst)
    print(path)

if __name__ == '__main__':
    main()