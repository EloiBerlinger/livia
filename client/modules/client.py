#!/usr/bin/python
#-*-coding:utf-8-*-
# Livia client class file
import socket
import pickle
import time

class Client:

    def __init__(self):
        self.clientConfig = {"colorSupporting": False, "username": "", "password": ""}
        self.clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
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

    def serverConnect(self, host, port, serverName=""):
        print("Asked connection to: "+host+":"+str(port))
        try:
            self.clientSocket.connect((host, port))
            state = True
            return state
        except:
            state = False
            return state

        if(state):
            if(serverName == ""):
                self.site += "/"+host
            else:
                self.site += "/"+serverName

            print("Sending client configuration...")
            clientConfig = "002,"+self.clientConfig["username"]+","+self.clientConfig["password"]
            self.clientSocket.send(clientConfig.encode(clientConfig))

    def sendCommand():
        pass

    def sendChat():
        pass
