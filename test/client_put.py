import logging
import asyncio

from aiocoap import Context, Message, Code

logging.basicConfig(level=logging.INFO)

async def main():
    protocol = await Context.create_client_context()

    # PUT
    payload = b'45'
    request = Message(code=Code.PUT, uri='coap://192.168.155.182/humidity', payload=payload)
    try:
        response = await protocol.request(request).response
    except Exception as e:
        print(f'Failed to fetch resource: {e}')
    else:
        print('Result: %s\n%r'%(response.code, response.payload))

    # Then, GET
    request = Message(code=Code.GET, uri='coap://192.168.155.182/humidity')
    try:
        response = await protocol.request(request).response
    except Exception as e:
        print(f'Failed to fetch resource: {e}')
    else:
        print('Result: %s\n%r'%(response.code, response.payload))

if __name__ == "__main__":
    asyncio.run(main())
