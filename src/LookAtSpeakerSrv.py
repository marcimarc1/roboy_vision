from __future__ import print_function

import logging
import asyncio
import websockets
import json as json

# # from config import params_setup
# from lib import data_utils



async def lookatspeaker_service_callback():
    async with websockets.connect('ws://localhost:9090') as websocket:

        # advertise the service
        await websocket.send("{ \"op\": \"advertise_service\",\
                      \"type\": \"roboy_communication_cognition/LookAtSpeaker\",\
                      \"service\": \"/roboy/cognition/vision/LookAtSpeaker\"\
                    }")

        i = 1  # counter for the service request IDs

        # wait for the service request, generate the answer, and send it back
        while True:
            try:
                # pdb.set_trace()
                request = await websocket.recv()

                srv_response = {}
                answer = {}
                # Look at speaker function must be called here
                answer["turned"] = False

                srv_response["values"] = answer
                srv_response["op"] = "service_response"
                srv_response["id"] = "service_request:/roboy/cognition/vision/LookAtSpeaker:" + str(i)
                srv_response["result"] = True
                srv_response["service"] = "/roboy/cognition/vision/Loo  kAtSpeaker"
                i += 1

                await websocket.send(json.dumps(srv_response))


            except Exception as e:
                logging.exception("Oopsie! Got an exception in LookAtSpeakerSrv")

logging.basicConfig(level=logging.INFO)
asyncio.get_event_loop().run_until_complete(lookatspeaker_service_callback())