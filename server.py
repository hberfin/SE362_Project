#!/usr/bin/env python

# WS server example

import asyncio
import websockets

async def hello(websocket, path):
    name = await websocket.recv()
    print(f"< {name}")
    if ("ali" in name):
        greeting = f"Ali: {name}!"
    elif ("veli" in name):
        greeting = f"Veli: {name}!"
    else:
        greeting = f"Diger: {name}!"
    

    await websocket.send(greeting)
    print(f"> {greeting}")

start_server = websockets.serve(hello, "localhost", 8765)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
