#!/usr/bin/env python
#coding: utf-8


import json
import os
import pyjsonrpc


SERVER_HOST = 'localhost'
SERVER_PORT = 4040

class RequestHandler(pyjsonrpc.HttpRequestHandler):
    """test"""
    @pyjsonrpc.rpcmethod
    def add(self, a, b):
        print "add"
        return a + b


http_server = pyjsonrpc.ThreadingHttpServer(
    server_address = (SERVER_HOST, SERVER_PORT),
    RequestHandlerClass = RequestHandler
)

print 'Starting HTTP server...'
print 'URL: http://' + str(SERVER_HOST) + " : " + str(SERVER_PORT)

http_server.serve_forever()