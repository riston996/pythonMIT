import math


#### points as lists
##def addPoints(p1,p2):
## r = []
## r.append(p1[0]+p2[0])
## r.append(p1[1]+p2[1])
## return r
##
##p = [1,2]
##q = [3,1]
##r = addPoints(p,q)
##print(r) 

## points as classes
class cartesianPoint:
 pass

cp1 = cartesianPoint()
cp2 = cartesianPoint()
cp1.x = 1.0
cp1.y = 2.0
cp2.x = 1.0
cp2.y = 3.0

def samePoint(p1,p2):
 return (p1.x == p2.x) and (p1.y == p2.y)

def printPoint(p):
 print('(' + str(p.x) + ', ' + str(p.y) + ')')
