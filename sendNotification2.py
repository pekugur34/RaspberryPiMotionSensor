
import os
import glob
import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

def sendEmail():
    msg = MIMEMultipart()
    msg['Subject'] = 'Someone is in your room!!'
    msg['From'] = 'ugurpek22@gmail.com'
    msg['To'] = 'pekugur34@gmail.com'

    text = MIMEText("We detected a motion in your room!!")
    msg.attach(text)

    path,dirs,files=next(os.walk('/home/pi/Desktop/cookie/images'))
    file_count=len(files)

    i=0
    while i < file_count:
        img_data = open('/home/pi/Desktop/cookie/images/' + os.listdir('/home/pi/Desktop/cookie/images')[i], 'rb').read()
        image = MIMEImage(img_data,name=os.path.basename('/home/pi/Desktop/cookie/images/'+os.listdir('/home/pi/Desktop/cookie/images')[i]))
        msg.attach(image)
        i+=1;

    files = glob.glob('/home/pi/Desktop/cookie/images/*')

    for f in files:
        os.remove(f)

#image = MIMEImage(img_data, name=os.path.basename('2018. 04. 30-185332.jpg'))
#msg.attach(image)
        

    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.ehlo()
    s.starttls()
    s.ehlo()
    s.login('ugurpek22@gmail.com','Ugur.1907')
    s.sendmail(msg['From'], msg['To'], msg.as_string())
    s.quit()
