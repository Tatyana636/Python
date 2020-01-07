from random import randrange
lines = int(input())
columns = int(input())
arr = [[randrange(10, 99) for i in range(columns)] for j in range(lines)]
first =int(input())
second =int(input())
def SwapColumns (a, i, j):
    print(' ')
    for i in a:
        print(' '.join(([str(j) for j in i])))
    for i in range(len(a)):
        for k in range(len(a[i])):
            if k==i and k+1==j:
                i=a[k]
                j=a[k+1]
                a[k]=j
                a[k+1]=i
                print(' ')
                for i in a:
                    print(' '.join(([str(j) for j in i])))
SwapColumns (arr, first, second)
