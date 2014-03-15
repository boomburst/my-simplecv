#crude program to recognize digit without ml 

from SimpleCV import *
from sys import *

def findDigit(blobs, corners, lines):
    
    if(len(blobs) == 3):
        return 8
#--------------------------------------
    elif(len(blobs) == 2):
        if(len(lines) >= 10):
            return 4

        for i in range(0, len(blobs)-1):
            if(i != len(blobs)-1):
                center = blobs[i].centroid()
                center1 = blobs[i+1].centroid()
                
                if(center[1] < center1[1]):
                    return 9
                elif(center[1] > center1[1]):
                    return 6
#------------------------------------
    elif(len(blobs) == 1):
        if(len(corners) >= 7 and len(lines) == 2):
            return 1
        elif(len(lines) == 3 and len(corners) == 7):
            return -1
        elif(len(corners) == 6):
            return 2
        elif(len(corners) == 9 and len(lines) == 7):
            return 5

        return 0
#------------------------------------
script, digit = argv

display = Display()
image = Image(digit)

digit = 0
while display.isNotDone():
   
    blobs = image.findBlobs()
    corners = image.findCorners()
    lines = image.findLines()
        
    if blobs is not None:
        blobs.draw(Color.GREEN, width=4)
    if corners is not None:
        corners.draw(Color.RED, width=4)
    if lines is not None:
        lines.draw(Color.BLUE, width=4)
        
    digit = findDigit(blobs, corners, lines)

    image.show()        
                        
print "No of blobs: ", len(blobs)
print "No of corners: ", len(corners)
print "No of lines: ", len(lines)
if(digit == -1):
    print "Possible digit: 7 or 3 "
else:
    print "Possible digit: ",digit
                
