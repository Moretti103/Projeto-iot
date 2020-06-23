# Projeto-iot
Esse projeto tem como objetivo, possibilitar realizar uma monitoração de temperatura e umidade do ar utilizando um raspberry pi e o DHT11


Para iniciar o projeto, com o raspberry desligado, conecte o DHT11 no Raspberry da seguinte forma:

Pino 1 do DHT11 ao pino de 3.3v da GPIO

Pino 2 do DHT11 ao pino 7 na GPIO 4.

Pino 3 do DHT11 ao pino 9.


Acesse o Raspberry e execute os próximos passos:

# Atualize os pacotes do sistema do seu Raspberry

sudo apt-get update 

# Instale os pacotes essenciais do Python:

sudo apt-get install build-essential python3-dev

# Instale a biblioteca da Adafruit_DHT, para que seja possivel estabelecer a conexão com o dispositivo DHT11

sudo pip3 install Adafruit_DHT

# Após instalar, verifique se está conseguindo obter os dados com o seguinte comando:

import Adafruit_DHT as adht 
humidity,temperature = adht.read_retry(adht.DHT11, 4) 
print( “humidity: {1:0.1f} and temperature: {1:0.1f} C”.format(humidity, temperature))


# Instale o InfluxDb e o para tratar os dados dos logs de temperatura e umidade

wget -qO- https://repos.influxdata.com/influxdb.key | sudo tee /etc/apt/sources.list.d/influxdb.list test $VERSION_ID = "8" && echo "deb https://repos.influxdata.com/debian jessie stable" | sudo tee /etc/apt/sources.list.d/influxdb.list test $VERSION_ID = "9" && echo "deb https://repos.influxdata.com/debian stretch stable" | sudo tee /etc/apt/sources.list.d/influxdb.list 

sudo apt-get update && sudo apt-get install influxdb 
sudo service influxdb start 

# Verifique o status do Influxdb
 
sudo service influxdb status

# Instale o Telegraf

sudo dpkg -i telegraf_1.9.4-1_armhf.deb 

# Utilize o script temperatureLog.conf para tratar os dados obtidos pelos logs de execução do script Get-Metrics.py

Para obter os dados da forma correta, execute o comando

telegraf --config temperatureLog.conf

# Instale o Grafana

echo "deb https://packages.grafana.com/oss/deb stable main" | sudo tee -a /etc/apt/sources.list.d/grafana.list curl https://packages.grafana.com/gpg.key | sudo apt-key add - 

sudo apt-get update 
sudo apt-get install grafana 
sudo service grafana-server start 

http://localhost:3000/

user: admin 
pass: admin

# Configure a integração do Influxdb com o Grafana

No Grafana, http://localhost:3000/datasources, adicione uma fornte de dados do Influxdb, colocando no campo URL o seguinte: 
http://localhost:8086

No campo database, coloque "temperature" e salve.

# Crie o dashboard de monitoração

Para criar, utilize o arquivo json presente no repositório.


