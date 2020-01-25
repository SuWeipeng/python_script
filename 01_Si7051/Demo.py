from machine import Pin
from machine import I2C
import Si705x
from time import sleep

i2c = I2C(scl=Pin(12), sda=Pin(14), freq=10000)

si7051 = Si705x.Si705x(i2c=i2c)

while(True):
    sleep(1)
    temp = si7051.temperature
    print(temp)
