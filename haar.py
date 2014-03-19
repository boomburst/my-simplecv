from SimpleCV import *

cam = Camera(1)
disp = Display()

while not disp.isDone():
    img = cam.getImage()
    faces = img.findHaarFeatures('face.xml')
    for f in faces:
        f.draw(Color.RED, width=3)
    img.show()
