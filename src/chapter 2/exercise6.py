#using pythagorean theorem to find the distance between two points.
x1,x2,y1,y2=int(input('value of x1')),int(input('value of x2')),int(input('value of y1')),int(input('value of y2'))
distance=round((((x2-x1)**2+(y2-y1)**2)**0.5),2)
print(distance)