import time
import adafruit_dht
import board

dht_device = adafruit_dht.DHT11(board.D4)
temperature_c = dht_device.temperature
    
if temperature_c >25 :
    lcd.putstr('Prenez un verre d eau')

    if temperature_c <25 :
    lcd.putstr('Couvrez-vous')


