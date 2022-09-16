#Importa las librerias
import RPi.GPIO as GPIO
import time
from Adafruit_IO import Client, Feed

#Define el puerto en Base a los GPIOS
GPIO.setmode(GPIO.BCM)
SERVO = 17
GPIO.setup(SERVO,GPIO.OUT)

print ("Enciende Servo")
#Incializa la frecuencia del servo y el angulo
p =GPIO.PWM(SERVO,50)
p.start(2.5)
angulo = 2

#Introduce tus datos de cuenta
READ_TIMEOUT = 5
ADAFRUIT_IO_KEY = "aio_SxLr54GsCf9mQ9XTAGt370X5IZN2"
ADAFRUIT_IO_USERNAME = "DR424"
aio = Client(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)

#Obtener feed
feed = aio.feeds('servo')

#Correr
try:
    while True:
        time.sleep(0.5)
        #Recibir del feed
        data = aio.receive(feed.key)
        angulo = int(data.value)
        print("angulo "+ str(round(angulo,2)))
        angulo = (int(angulo)/18) + 2
        p.ChangeDutyCycle(angulo)
        
except KeyboardInterrupt:
    print("The End")
    GPIO.cleanup() 

