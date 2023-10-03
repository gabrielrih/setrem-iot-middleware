import logging
import asyncio
import aiocoap.resource as resource
import aiocoap

import src.env as envs

from src.coap import WhoAmI


logging.basicConfig(level=logging.INFO)
logging.getLogger("coap-server").setLevel(logging.DEBUG)


async def main():
   # Resource tree creation
   
   root = resource.Site()
   root.add_resource(['.well-known', 'core'], resource.WKCResource(root.get_resources_as_linkheader))
   root.add_resource(['whoami'], WhoAmI())

   # Create tuple for bind
   #    The create_server_context receives a tuple
   bind = (envs.BIND_IP, envs.PORT) 
   await aiocoap.Context.create_server_context(site = root, bind = bind)
   
   # Run forever
   await asyncio.get_running_loop().create_future()


if __name__ == "__main__":
   asyncio.run(main())
