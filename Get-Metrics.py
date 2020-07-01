import Adafruit_DHT as adht
import time
import logging

logging.basicConfig(filename='temperature.log', filemode='a', format='%(created)f %(message)s', level=logging.INFO)
print ("iniciando coleta de dados do sensor")
while True:
    h,t = adht.read_retry(adht.DHT11, 4)
    logging.info('Temp={0:0.1f} C and Humidity={1:0.1f} %'.format(t, h))
