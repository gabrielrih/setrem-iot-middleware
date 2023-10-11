import os

''' Ler e enviar dados do sensor a cada X segundos'''
SECONDS_TO_WAIT = os.getenv('SECONDS_TO_WAIT', 300)

''' Pino físico do Raspberry onde o sensor está conectado '''
SENSOR_PIN = os.getenv('SENSOR_PIN', 4)

''' IP onde a aplicação está executando. Ela estará "escutando" na porta do Coap esperando por dados '''
COAP_SERVER_IP = os.getenv('COAP_SERVER_IP', '192.168.1.115')

''' Nível de logs a serem exibidos '''
LOG_LEVEL = os.getenv('LOG_LEVEL', 'DEBUG')
