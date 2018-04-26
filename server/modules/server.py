#!/usr/bin/python
#-*-coding:utf-8-*-
# Livia server class file
import socket
import select

class Server:
    def __init__(self):
        # Initialise server variables:
        self.users = list()
        self.host = str()
        self.state = False
        self.serverConfig = {}
        self.serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Getting server configuration:
        with open("serverConfig.conf", "r") as configFile:
            
            for l in configFile:
                if(l[0] != "#"):
                    # If the first caracter of the line is not #:
                    def extractValue(key, line):
                        final = ""
                        count = 0
                        keyLength = len(key+" = ")
                        lineLength = len(line)-1 # -1 for the line return

                        for c in line:
                            if(count in range(keyLength, lineLength)):
                                final += c
                            count += 1

                        return final

                    # There is all the server extraction values
                    if("serverName" in l):
                        self.serverConfig["serverName"] = extractValue("serverName", l)
                    if("serverPort" in l):
                        self.serverConfig["serverPort"] = extractValue("serverPort", l)
                    if("maxClients" in l):
                        self.serverConfig["maxClients"] = extractValue("maxClients", l)

    def start():
        pass
