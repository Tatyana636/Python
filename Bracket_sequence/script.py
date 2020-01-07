import re
file=open('text.txt', 'r').read()
line=re.findall('[()[\\]{}]', file)
counter=0
def pop():
    line.pop(i)
    line.pop(i)
if len(line)%2!=2:
    for i in range(len(line)):
        while counter<len(line):
            if line[i] == '(' and line[i+1] == ')':
                    pop()
                    if line[i] == '[' and line[i+1] == ']':
                        pop()
                        if line[i] == '{' and line[i+1] == '}':
                            pop()
            counter+=1
print('yes' if len(line)==0 else 'no')
