import time
import asyncio

import src.env as envs

from src.coap import send_data
from src.dht11 import read_data_from_sensor
from src.util.logger import Logger


logger = Logger.get_logger(__name__)


'''
    Método principal
    Loop infinito que lê os dados do sensor e se houver dados envia via Coap
'''
if __name__ == "__main__":
    logger.info("Starting...")
    logger.info(f'Sending data every {envs.SECONDS_TO_WAIT} seconds!')
    while True:
        logger.info("Reading data from sensor...")
        temperature, humidity = read_data_from_sensor(int(envs.SENSOR_PIN))
        if not temperature or not humidity:
            logger.warning(f'Unable to read sensor. Temperature: {temperature} - Humidity: {humidity}')
            continue
        payload = f'{temperature} {humidity}'
        asyncio.run(send_data(bytes(payload, 'utf-8')))
        time.sleep(int(envs.SECONDS_TO_WAIT))
