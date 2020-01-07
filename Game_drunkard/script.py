first, second=[int(input("First: ")) for i in range(5)], [int(input("Second: ")) for i in range(5)]
counter=0
def push():
    first.append(first.pop(0))
    first.append(second.pop(0))
def push1():
    second.append(first.pop(0))
    second.append(second.pop(0))
while len(first)!=0 or len(second)!=0:
    if len(first)==0 or len(second)==0:
        break
    elif first[0]==0 and second[0]==9:
        push()
    elif first[0]==9 and second[0]==0:
        push1()
    elif first[0]<second[0]:
        push1()
    elif first[0]>second[0]:
        push()
    counter+=1
    if counter==10**2:
        print('botva')
        break
print('second' if len(first)==0 else 'first', c)

        
    
