#!/usr/bin/python
#-*-coding:utf-8-*-
# Livia server class file
import socket
import select
import cPickle, shelve

class Server:
    def __init__(self):
        # Initialise server variables:
        self.users = list()
        self.host = str()
        self.state = False
        self.serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Getting server configuration:


    def start():
        pass
