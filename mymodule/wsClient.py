import threading
import websockets
import asyncio
import json


class AsyncBaseClient:

    def __init__(self, *args, **kwargs):
        self.ws = None
        self.uri = None
        self.__dict__.update(kwargs)
        self.loop = None
        self.which_loop = None
        try:
            self.loop = asyncio.get_running_loop()
            self.which_loop = 0
        except:
            self.loop = asyncio.new_event_loop()
            self.thread = threading.Thread(
                target=self.loop.run_forever, daemon=True)
            self.thread.start()
            self.which_loop = 1

    async def receiveCB(self):
        try:
            msg = await self.ws.recv()
            self.loop.call_soon_threadsafe(
                asyncio.create_task, self.receiveCB())
            await self.received(msg)
        except:
            print('Error while receiving from socket. Disconnecting ...')
            await self.disconnect()

    async def connect(self):
        self.ws = await websockets.connect(self.uri)
        self.loop.call_soon_threadsafe(asyncio.create_task, self.receiveCB())

    async def send(self, data):
        await self.ws.send(data)

    async def disconnect(self):
        if (self.which_loop):
            self.loop.call_soon_threadsafe(self.loop.stop)
        try:
            await self.ws.close()
        except:
            pass
        self.ws = None
        print('Websocket: Disconnected')

    async def received(self, data):
        pass


class JsonAsyncClient(AsyncBaseClient):

    async def send_json(self, raw_data):
        data = None
        try:
            data = json.dumps(raw_data)
        except:
            print('ERROR: Error converting data to json string')
        print('json data processed to send :-')
        print(data)
        if (data):
            await self.send(data)

    async def json_received_preprocessor(self, raw_data):
        data = None
        try:
            data = json.load(raw_data)
        except:
            print('ERROR: Error loading received data as json')
        if (data):
            await self.received_json(data)

    async def received_json(self, data):
        pass

    async def received(self, data):
        self.json_received_preprocessor(data)
