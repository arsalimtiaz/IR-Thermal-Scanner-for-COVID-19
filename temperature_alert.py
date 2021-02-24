from smbus2 import SMBus
from mlx90614 import MLX90614
import smtplib
import time

server = smtplib.SMTP_SSL('smtp.gmail.com', 465)

server.login("arsalimtiazgcp", "CCES2021")
USN = 'ENG17CT0025'
message = "Subject: COVID-19 Potential Paitent \n\nPotential Paitent : " + USN
while 1:
    bus = SMBus(1)
    sensor = MLX90614(bus, address=0x5A)
#print "Ambient Temperature :", sensor.get_ambient()
    print ("Object Temperature :", sensor.get_object_1())
    object=sensor.get_object_1()
    print("Object Temperature:",object)
    bus.close()
    if object>38.0:
        server.sendmail(
  "arsalimtiazgcp@gmail.com",
  ["nishanthkv2000@gmail.com","arsalimtiaz@gmail.com"],
  message)
        time.sleep(3)
   
server.quit()
