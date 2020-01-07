file=open('text.txt', 'r')
line=file.read().split('\n')
leng=0
for i in range(len(line)):
    if len(line[i])>leng:
        leng=len(line[i])
for i in range(len(line)):
    if len(line[i])==leng:
        print(line[i])

