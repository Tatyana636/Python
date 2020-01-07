import re
n=int(input())
if n>=1 and n<=100:
    m=int(input())
    if m>=1 and m<=10000:
        lst=[[int(j) for j in input().split()] for i in range(m)]
        arr=[]
        obj={}
        for i in range(m):
           if lst[i] not in arr:
                arr.append(a[i])
        arr=re.findall('\d+', str(b))
        for i in arr:
            if arr.count(i)!=n-1:
                obj[i]=arr.count(i)
        if len(obj)!=0:
            print("No")
        else:
            print("Yes")
    else:
        print("Ошибка")
else:
    print("Ошибка")
