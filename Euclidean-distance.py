#1. Find an Euclidean distance between (2,3) and (10,8)
"""the formula is a=((x1-y1)^2 + (x2-y2)^2);
answer = a**(1./2)"""
import numpy as np
arr = [2,3,10,8]
exponent = 2

distx = [[arr[0]-arr[2]]]
disty = [[arr[1]-arr[3]]]
dist = (np.power (distx,exponent)) + (np.power (disty,exponent))
answer = dist*(1./2)
print(answer)
