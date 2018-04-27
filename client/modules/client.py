#!/usr/bin/python
#-*-coding:utf-8-*-
# Livia client class file
import socket
import pickle
import time

class Client:

    def __init__(self):
        self.clientConfig = {"colorSupporting": False, "username": "", "password": ""}
        self.exit = False
        self.site = "Livia/Home"
        self.servers = {}
        self.bestServers = []

    def saveClient(self):
        self.exit = False
        with open("database/client.livia", "wb") as file:
            pickleFile = pickle.Pickler(file)
            pickleFile.dump(self)

    def log(self, type, content):
        timePrefix = "{"+time.strftime("%d/%b/%Y:%H-%M-%S")+"}"
        with open("database/clientLogs.txt", "a") as logsFile:
            logsFile.write(timePrefix+" ["+type+"] "+content+"\n")

    def serverConnect(self, host, port):
        pass
