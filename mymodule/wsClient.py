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
        self.close = 0

    async def receiveCB(self):
        try:
            # always listen to incoming message to keep the ws connection live
            msg = await self.ws.recv()
            self.loop.call_soon_threadsafe(
                asyncio.create_task, self.receiveCB())  # register this function for loop's next iteration to keep connection alive and keep receiving
            await self.received(msg)  # call the received subroutine
        except:     # most like this block will run if the socket is closed
            print('Error while receiving from socket. Disconnecting ...')
            # if socket is not closed the close it as there was something wrong in receiving also puts the class to a stanble state
            await self.disconnect()

    async def connect(self):
        try:
            # if there is a runnning loop then use it
            self.loop = asyncio.get_running_loop()
            self.which_loop = 0  # 0 signifies a already running loop
        except:  # if here is no running loop
            # create a new running loop if there is no running loop
            self.loop = asyncio.new_event_loop()
            self.thread = threading.Thread(
                target=self.loop.run_forever, daemon=True)  # run that loop on a new thread and daemon=True signifies it is a background task means it exits if program closes
            self.thread.start()
            self.which_loop = 1  # 1 signifies a loop created my this module
        self.ws = await websockets.connect(self.uri)
        self.loop.call_soon_threadsafe(asyncio.create_task, self.receiveCB())

    async def send(self, data):  # subroutine to send data over socket
        if (self.close == 1):
            return
        if (self.ws == None):
            self.loop.call_soon_threadsafe(
                self.loop.call_later, 2, self.loop.create_task, self.send(data))
            return
        await self.ws.send(data)

    # subroutine to proporly disconnect the socket and put the class object to a stable state
    async def disconnect(self):
        if (self.which_loop):  # if loop is created by this module then close the loop
            self.loop.call_soon_threadsafe(self.loop.stop)
        try:
            await self.ws.close()
        except:
            pass
        self.ws = None
        self.loop = None
        self.close = 1
        print('Websocket: Disconnected')

    # abstract function which needs to be overeiden in the child call to do something with the received data
    async def received(self, data):
        pass


class JsonAsyncClient(AsyncBaseClient):

    async def send_json(self, raw_data):  # process and send data over websocket
        data = None
        try:
            data = json.dumps(raw_data)  # stringify data to json strinig
        except:
            # if there is any error in json.dumps()
            print('ERROR: Error converting data to json string')
        if (data):
            await self.send(data)  # send processed data

    # to process the received string
    async def json_received_preprocessor(self, raw_data):
        data = None
        try:
            data = json.load(raw_data)  # load the received json string
        except:
            print('ERROR: Error loading received data as json')
        if (data):
            # call the method where user can do somethingwith data
            await self.received_json(data)

    # needs to be override by user where he/she can use the received data
    async def received_json(self, data):
        pass

    async def received(self, data):
        await self.json_received_preprocessor(data)
