#Montaje 23: Programado en un ESP32 leds con bucle while, for y listas en python y wokwi
#corregir

from machine import Pin
import time

leds = [Pin(i, Pin.OUT) for i in (22, 21, 19 18, 5, 4, 2, 15, )]

while True:
   for led in leds:
       led.value(1)
       time.sleep(0.4)
       led.value(0)
   for led in reverded (leds):
       led.value(1)
       time.sleep(0.2)
       led.value(0)
