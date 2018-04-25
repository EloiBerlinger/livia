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
        self.serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Getting server configuration:
        with open("serverConfig.conf", "r") as configFile:

            extractedValues = {}

            for l in configFile:
                if(l[0] != "#"):
                    # If the first caracter of the line is not #:
                    def extractValue(key, line):
                        final = ""
                        keyLength = len(key+" = ")
                        lineLength = len(l)
                        for c in line:
                            charIndex = line.index(c)
                            if(charIndex in range(keyLength, lineLength)):
                                final += c

                        return final

                    if("serverName" in l):
                        extractedValues["serverName"] = extractValue(l, "serverName")
                    elif("serverPort" in l):
                        extractedValues["serverPort"] = extractValue(l, "serverPort")

        print(extractedValues)

    def start():
        pass
