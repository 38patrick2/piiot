import RPi.GPIO as GPIO
from time import sleep
import sys
import Adafruit_DHT
from connection import mqtt_connect


def on_message(client, userdata, msg):
   print("Topic: "+msg.topic+" | Message: "+str(msg.payload.decode()))
   if msg.topic == "temp/get":
       temp()
      
client = mqtt_connect()

client.on_message = on_message
client.loop_start()

client.subscribe("temp/get")

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)

a=19
b=26
c=20
d=16
e=12
f=13
g=6

pwm=GPIO.PWM(17, 50)
GPIO.setup(a,GPIO.OUT)
GPIO.setup(b,GPIO.OUT)
GPIO.setup(c,GPIO.OUT)
GPIO.setup(d,GPIO.OUT)
GPIO.setup(e,GPIO.OUT)
GPIO.setup(f,GPIO.OUT)
GPIO.setup(g,GPIO.OUT)

def temp():
    humidity, temperature = Adafruit_DHT.read_retry(11,4)
    print ('Temp: {0:0.1f}C '.format(temperature))
    client.publish("temp/result", temperature)
def off():
    GPIO.output(a,0)
    GPIO.output(b,0)   
    GPIO.output(c,0)
    GPIO.output(d,0)
    GPIO.output(e,0)
    GPIO.output(f,0)
    GPIO.output(g,0)
    sleep(.5)
    
def write0():
    GPIO.output(a,1)
    GPIO.output(b,0)   
    GPIO.output(c,1)
    GPIO.output(d,1)
    GPIO.output(e,1)
    GPIO.output(f,1)
    GPIO.output(g,1)
    sleep(.5)
    
def write1():
    GPIO.output(a,0)
    GPIO.output(b,0)   
    GPIO.output(c,1)
    GPIO.output(d,0)
    GPIO.output(e,0)
    GPIO.output(f,0)
    GPIO.output(g,1)
    sleep(.5)

def write2():
    GPIO.output(a,0)
    GPIO.output(b,1)   
    GPIO.output(c,0)
    GPIO.output(d,1)
    GPIO.output(e,1)
    GPIO.output(f,1)
    GPIO.output(g,1)
    sleep(.5)

def write3():
    GPIO.output(a,0)
    GPIO.output(b,1)   
    GPIO.output(c,1)
    GPIO.output(d,1)
    GPIO.output(e,0)
    GPIO.output(f,1)
    GPIO.output(g,1)
    sleep(.5)

def write4():
    GPIO.output(a,1)
    GPIO.output(b,1)   
    GPIO.output(c,1)
    GPIO.output(d,0)
    GPIO.output(e,0)
    GPIO.output(f,0)
    GPIO.output(g,1)
    sleep(.5)

def write5():
    GPIO.output(a,1)
    GPIO.output(b,1)   
    GPIO.output(c,1)
    GPIO.output(d,1)
    GPIO.output(e,0)
    GPIO.output(f,1)
    GPIO.output(g,0)
    sleep(.5)

def write6():
    GPIO.output(a,1)
    GPIO.output(b,1)   
    GPIO.output(c,1)
    GPIO.output(d,1)
    GPIO.output(e,1)
    GPIO.output(f,1)
    GPIO.output(g,0)
    sleep(.5)

def write7():
    GPIO.output(a,0)
    GPIO.output(b,0)   
    GPIO.output(c,1)
    GPIO.output(d,0)
    GPIO.output(e,0)
    GPIO.output(f,1)
    GPIO.output(g,1)
    sleep(.5)

def write8():
    GPIO.output(a,1)
    GPIO.output(b,1)   
    GPIO.output(c,1)
    GPIO.output(d,1)
    GPIO.output(e,1)
    GPIO.output(f,1)
    GPIO.output(g,1)
    sleep(.5)

def write9():
    GPIO.output(a,1)
    GPIO.output(b,1)   
    GPIO.output(c,1)
    GPIO.output(d,0)
    GPIO.output(e,0)
    GPIO.output(f,1)
    GPIO.output(g,1)
    sleep(.5)
    
def motor(x):  
    pwm.start(0)
    pwm.ChangeDutyCycle(x) 
    sleep(1)
    pwm.stop()

write1()
off()
write2()
off()
write3()
off()
write4()
off()
write5()
off()
write6()
off()
write7()
off()
write8()
off()
write9()
off()
write0()
off()
motor(5)
GPIO.cleanup()

client.loop_stop()