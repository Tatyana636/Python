import math
x=float(input('Координата точки по оси Оx '))
y=float(input('Кордината точки по оси Оy '))
xc=float(input('Центр круга по оси Ox '))
yc=float(input('Центр круга по оси Оy '))
r=float(input('Радиус круга '))
def distance(x, y, xc, yc):
    return math.sqrt((x-xc)**2+(y-yc)**2<r**2)
def IsPointInCircle(x, y, xc, yc, r):
    return (x-xc)**2+(y-yc)**2<r**2
if distance(x, y, xc, yc):
    print('Yes')
else:
    print('No')
