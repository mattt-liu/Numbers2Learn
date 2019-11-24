## Matthew Liu

########## MODULES ##########
from pygame import *
import math as Math
import random
import os
import pprint

def degrade(points):
    if len(points) <= 28:
        return points
    newPoints = []
    for x in range(0, len(points), 2):
        p = []
        for y in range(0, len(points[x]), 2):

            ## check 4x4 area
            x1y1 = float(points[x][y])
            x1y2 = float(points[x][y+1])
            x2y1 = float(points[x+1][y])
            x2y2 = float(points[x+1][y+1])

            ## set to average
            avg = float((x1y1+x1y2+x2y1+x2y2)/4)
##            if avg!=0: 
##                avg = (x1y1+x1y2+x2y1+x2y2+1)/5
##            if (avg>=1): avg = 1
##            p.append(avg)
                
        newPoints.append(p)
##    print(newPoints[int(len(newPoints)/2)])
    return degrade(newPoints)
        
def main():
    points = []
    file = open("points.txt", "r")
    lines = file.readlines()
    for line in lines:
        line = line.replace("[", "")
        line = line.replace("]", "")
        points.append("".join((line.strip().split(", "))))

    points = degrade(points)

    ## write new points
    file = open("degradedPoints.txt", "w")
    for line in points:
        for p in line:
            file.write(str(p)+" ")
        file.write("\n")
    file.close()

    ## write as array

if __name__ == "__main__":
    main()
