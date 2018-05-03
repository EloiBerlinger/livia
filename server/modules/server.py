#!/usr/bin/python
#-*-coding:utf-8-*-
# Livia server class file
from modules.utils.clientConfig import *
from modules.utils.clientProcess import *
from modules.user import *
import socket
import select
import time

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
                        self.serverConfig["serverPort"] = int(extractValue("serverPort", l))
                    if("maxClients" in l):
                        self.serverConfig["maxClients"] = extractValue("maxClients", l)
                    if("welcomeMessage" in l):
                        self.serverConfig["welcomeMessage"] = extractValue("welcomeMessage", l)

    def start(self):
        print("Starting server...")
        self.log("serverStarting", "Starting server")

        self.serverSocket.bind(("", self.serverConfig["serverPort"]))
        self.serverSocket.listen(5)
        print("Server listening on "+str(self.serverConfig["serverPort"]))
        self.log("ServerStarting", "Server listening on "+str(self.serverConfig["serverPort"]))

        self.state = True
        while(self.state):
            askedConnections, wlist, xlist = select.select([self.serverSocket], [], [], 0.05)

            for connection in askedConnections:
                clientConnection, connectionData = connection.accept()
                print("New connection from "+str(connectionData))

                # Client configuration:
                recevedConfiguration = False
                try:
                    clientConfig = clientConnection.recv(1024)
                    recevedConfiguration = True
                except:
                    print("Client configuration error for "+connectionData)
                    clientConnection.close()

                if(recevedConfiguration):
                    # Extract client informations
                    clientConfig = clientConfig.decode()
                    clientConfig = clientConfig.split(",")
                    if(clientConfig[0] == "002"):
                        # Check message type
                        try:
                            userPseudo = clientConfig[1]
                            userPassword = clientConfig[2]

                            self.users.append(User(clientConfig(clientConnection, connectionData, userPseudo, userPassword)))
                        except:
                            print("Error while getting user pseudo and user password !")

                    else:
                        print("Client configuration error, message type error !")


            """
            toReadClient = []
            try:
                toReadClient, wlist, xlist = select.select(self.users.socket, [], [], 0.05)
            except select.error:
                pass
            else:
                for client in self.users:
                    clientProcess(client)
            """

    def stop(self):
        print("Stopping server...")
        self.log("StoppingServer", "Stopping server...")

        for c in self.users:
            c.socket.close()
            print("Closed connection with ...")
            self.log("ClosedConnection", "Closed connection with...")

        self.serverSocket.close()

    def log(self, type, content):
        timePrefix = "{"+time.strftime("%d/%b/%Y:%H-%M-%S")+"}"
        with open("database/serverLogs.txt", "a") as logsFile:
            logsFile.write(timePrefix+" ["+type+"] "+content+"\n")
