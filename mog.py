from SimpleCV import *

mog = MOGSegmentation(history = 200, nMixtures = 5, backgroundRatio = 0.3, noiseSigma = 16, learningRate = 0.3)
  
cam = Camera(1)  
  
disp = Display()
  
while (disp.isNotDone()):  
    frame = cam.getImage()
    
    mog.addImage(frame)
    
    segmentedImage = mog.getSegmentedImage()
    blobs = segmentedImage.findBlobs()
    if blobs is not None:
        blobs.sortArea()
        blobs[-1].draw(Color.RED, width=3)
        
    
    segmentedImage.show()
