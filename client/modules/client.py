#!/usr/bin/python
#-*-coding:utf-8-*-
# Livia client class file
import socket
import pickle

class Client:

    def __init__(self):
        self.exit = False
        self.site = "Livia/Home"
        self.colorSupporting = False
        self.servers = {}
        self.bestServers = []

    def saveClient(self):
        with open("database/client.livia", "wb") as file:
            pickleFile = pickle.Pickler(file)
            pickleFile.dump(self)

    def serverConnect(self, host, port):
        pass
