#Simple script to detect digits using basic geometry (8, 6, 9)
#Use an image file as argument 

from SimpleCV import *
from sys import *

script, digit = argv

display = Display()
img = Image(digit)

while display.isNotDone():
    blobs = img.findBlobs().sortArea()
    if blobs is not None:
        for i in range(0, len(blobs)-1):
            blobs[i].draw(Color.GREEN, width =-1)
            if(len(blobs) == 3):
                print "The number might be a 8"
                exit()
            
            if(len(blobs) == 2):
                if(i != len(blobs)-1):
                    center = blobs[i].centroid()
                    center1 = blobs[i+1].centroid()

                    if(center[1] < center1[1]):
                        print "The number might be a 9"
                        exit()

                    if(center[1] > center1[1]):
                        print "The number might be a 6"            
                        exit()
                            
print len(blobs)
                
