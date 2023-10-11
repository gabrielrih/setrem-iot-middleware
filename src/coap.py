import src.env as envs

from aiocoap import Context, Message, Code
from src.util.logger import Logger


logger = Logger.get_logger(__name__)


ENDPOINT = f'coap://{envs.COAP_SERVER_IP}/humidity'


''' Função assíncrona para enviar dados via COAP '''
async def send_data(payload):
    logger.info(f'Sending payload: {str(payload)}')
    protocol = await Context.create_client_context()
    request = Message(code=Code.PUT, uri=ENDPOINT, payload=payload)
    try:
        response = await protocol.request(request).response
    except Exception as e:
        logger.error(f'Failed to send data: {e}')
    else:
        logger.info(f'Result - Code {response.code} : {response.payload}')
