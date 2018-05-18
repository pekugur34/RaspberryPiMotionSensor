
import picamOriginal
import picamera
import sendNotification2
import glob
import os
from datetime import datetime

motState = False
path = '/home/pi/Desktop/cookie/images/'

def captureImage(currentTime,picPath):
    picName = currentTime.strftime('%Y. %m. %d-%H%M%S')+'.jpg'
    with picamera.PiCamera() as camera:
        camera.resolution = (1280,720)
        camera.capture(picPath+picName)
    print('Taken pic')

def getTime():
    currentTime=datetime.now()
    return currentTime

picNumber=0

files = glob.glob('/home/pi/Desktop/cookie/images/*')

for f in files:
    os.remove(f)

while True:
    motState = picamOriginal.mtion()
    print(motState)
    if motState:
        currentTime = getTime()
        captureImage(currentTime,path)
        picNumber+=1
        if (picNumber == 5):
            sendNotification2.sendEmail()
            picNumber=0
