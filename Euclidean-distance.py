#1. Find an Euclidean distance between (2,3) and (10,8)
"""the formula is a=((x1-y1)^2 + (x2-y2)^2);
answer = a**(1./2)"""

first_coordinate = (2 - 10)**2
second_coordinate = (3 - 8)**2
a = first_coordinate + second_coordinate
answer = a * (1. / 2)
print("The distance is :", answer)
