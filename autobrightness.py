import numpy as np
from SimpleCV import Camera, Display, Image
import os

def menu():
    os.system('clear')
    user = os.popen('echo $USER').read()
    date = os.popen('date').read()
    string = '''\n\t This program uses your default webcam to detect changes in lighting and changes your laptop brightness accordingly
                 \n\t Press ESC to terminate the script'''
    print "\tWelcome "+user
    print string
    print "Started at: ", date
               
def light(current):
    gray=current.grayscale()
    matrix=current.getNumpy()
    mean=matrix.mean()
    return mean

def changeBrightness(mean):
    if(mean <= 69.0):
        os.system('echo 5 > /sys/class/backlight/acpi_video0/brightness')
    if(mean >= 70.0 and mean <= 89.0 ):
        os.system('echo 7 > /sys/class/backlight/acpi_video0/brightness')
    if(mean >= 90.0 and mean <= 124.0):
        os.system('echo 9 > /sys/class/backlight/acpi_video0/brightness')
    if(mean >= 125.0 and mean<= 159.0):
        os.system('echo 11 > /sys/class/backlight/acpi_video0/brightness')
    if(mean >= 160.0):
        os.system('echo 13 > /sys/class/backlight/acpi_video0/brightness')
    
os.system('sudo chmod 777 /sys/class/backlight/acpi_video0/brightness')
cam = Camera()
display = Display()

menu() 
mean=0
while not display.isDone():
    current=cam.getImage()    
    mean = light(current)
    changeBrightness(mean)
    current.show()

date = os.popen('date').read()
os.system('clear')
print "Ended at ",date

    
