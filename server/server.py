#!/usr/bin/env python
# coding: utf-8

from aiohttp import web
import logging
from lang_model import handletext
# for production uncomment logging and change headers to empty

logging.basicConfig(filename='server.log', level=logging.INFO, format='%(asctime)s %(levelname)-2s %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

# CORS policy headers
# headers = {
#     "Access-Control-Allow-Origin": "*",
#     "Access-Control-Allow-Methods": "*",
#     "Access-Control-Allow-Headers": "*",
# }
headers = {}
async def handleoptions(request):
    return web.Response(headers=headers)


async def resolve_words_request(request):
    req = await request.json()
    if req.get("input"):
        edited_sentence = handletext(req.get("input"))
        data = {
            "editedInput": edited_sentence
        }
        return web.json_response(data, headers=headers)
    else:
        return web.HTTPBadRequest(text="input key is empty or doesn't exist")


app = web.Application()
app.add_routes([web.options(r"/{xyz:.*}", handleoptions),
                web.post("/api/words", resolve_words_request)])
web.run_app(app, host="127.0.0.1", port=7009, access_log=None)
