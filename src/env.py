import os


SECONDS_TO_WAIT = os.getenv('SECONDS_TO_WAIT', 10)
SENSOR_PIN = os.getenv('SENSOR_PIN', 4)

LOG_LEVEL = os.getenv('LOG_LEVEL', 'DEBUG')
