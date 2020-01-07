file=open('text.txt', 'r').readlines()
for i in range(len(file)):
    file[i]=file[i].strip()
    for j in range(len(file[i])):
       print(chr(ord(file[i][j])+i+1), end='')
    print()
