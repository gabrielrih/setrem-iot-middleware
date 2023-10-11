
import Adafruit_DHT
import math

from src.util.logger import Logger


logger = Logger.get_logger(__name__)


SENSOR = Adafruit_DHT.DHT11


def __truncate(input: int) -> int:
    return math.trunc(input)


def read_data_from_sensor(pin: int) -> (str, str):
    logger.debug(f'pin: {pin}')
    try:
        humidity, temperature = Adafruit_DHT.read_retry(SENSOR, pin)
        return __truncate(temperature), __truncate(humidity)
    except Exception as exc:
        logger.error(f'Error on reading sensor: {exc}')
