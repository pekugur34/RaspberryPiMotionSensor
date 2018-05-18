# RaspberryPiMotionSensor

This is for taking pictures when any movement appears in front of the camera and the camera will send 5 pictures to your e-mail.

# Usage

1-Type the commands on your pi's console
-sudo apt-get install python-imaging-tk 
-sudo apt-get install python3-dev
-sudo apt-get install python3-pip
-sudo pip 3.2 install Pillow 

2-Create this directory /home/pi/Desktop/cookie/images.(Pictures will be saved here and be removed after sending a mail.)

3-)Enter your e-mail credentials in sendNotification2.py file.

4-)You can also change how many pictures you want in a mail by changing if statement in useMotion.py file.(Line 37)

5-)Run useMotion.py file

#Uğur Pek - TTU-2018

