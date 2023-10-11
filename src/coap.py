from aiocoap import Context, Message, Code
from src.util.logger import Logger


logger = Logger.get_logger(__name__)


async def send_data(payload):
    logger.info(f'Sending payload: {str(payload)}')
    protocol = await Context.create_client_context()
    request = Message(code=Code.PUT, uri='coap://192.168.1.115/humidity', payload=payload)
    try:
        response = await protocol.request(request).response
    except Exception as e:
        logger.error(f'Failed to send data: {e}')
    else:
        logger.info(f'Result - Code {response.code} : {response.payload}')
