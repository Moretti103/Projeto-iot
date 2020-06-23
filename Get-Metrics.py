import Adafruit_DHT
import time
import logging

DHT_SENSOR = Adafruit_DHT.DHT11
DHT_PIN = 4

print("Iniciando leitura dos dados")

logging.basicConfig(filename='temperature.log', filemode='a', format='%(created)f %(message)s', level=logging.INFO)

while True:
    humidity, temperature = Adafruit_DHT.read(DHT_SENSOR, DHT_PIN)
    if humidity is not None and temperature is not None:
        logging.info("Temp={0:0.1f}C and  Humidity={1:0.1f}%".format(temperature, humidity))
    else:
        print("Sensor failure. Check wiring.");
    time.sleep(5);
