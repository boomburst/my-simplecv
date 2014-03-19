from SimpleCV import *
cam = Camera(1)
previous = cam.getImage()

disp = Display()

while not disp.isDone():
    current = cam.getImage()
    motion = current.findMotion(previous)
    for m in motion:
        m.draw(Color.GREEN, normalize = False)
    
    current.show()
    previous = current
