num=int(input())
arr=[['.']*num for i in range(num)]
for i in range(num):
    for j in range(num):
        if i+j==num-1 or i==num//2 or j==num//2:
            arr[i][j]='*'
        arr[i][i]='*'
for j in arr:
    print(' '.join([str(i) for i in j]))
