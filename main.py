import time
import adafruit_dht
import board

dht_device = adafruit_dht.DHT11(board.D4)
temperature_c = dht_device.temperature
if capteur de mouvement.value==1:


def écran () : 
 if temperature_c >25 :
    lcd.putstr('Prenez un verre d eau')


 if 15<temperature_c <25 :
    lcd.putstr ('Température normale') 
    

 if temperature_c <15 :
lcd.putstr('Couvrez-vous')


