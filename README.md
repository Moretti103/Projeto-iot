# Projeto-iot
Esse projeto tem como objetivo, possibilitar realizar uma monitoração de temperatura e umidade do ar utilizando um raspberry pi e o DHT11


Para iniciar o projeto, com o raspberry desligado, conecte o DHT11 no Raspberry da seguinte forma:

Pino 1 do DHT11 ao pino de 3.3v da GPIO

Pino 2 do DHT11 ao pino 7 na GPIO 4.

Pino 3 do DHT11 ao pino 9.


Acesse o Raspberry e execute os próximos passos:

Atualize os pacotes do sistema do seu Raspberry

# sudo apt-get update 

Instale os pacotes essenciais do Python:

# sudo apt-get install build-essential python3-dev

Instale a biblioteca da Adafruit_DHT, para que seja possivel estabelecer a conexão com o dispositivo DHT11

# sudo pip3 install Adafruit_DHT

Após instalar, verifique se está conseguindo obter os dados com o seguinte comando:

import Adafruit_DHT as adht 
humidity,temperature = adht.read_retry(adht.DHT11, 4) 
print( “humidity: {1:0.1f} and temperature: {1:0.1f} C”.format(humidity, temperature))




