#!/usr/bin/python
#-*-coding:utf-8-*-
def connect(command, client):
     # Check client configuration password and name
     # /connect <serverName/serverHost:port>
     # Get command serverHost

    errorMessage = "Error while usine /connect, use /help"

    if(len(command) == 1):
        host = input("Server host > ")
        port = input("Server port (Keep empty for use default port) > ")

        client.serverConnect(host, port)

    elif(len(command) == "2"):
        serverAddress = command[2]

        if(":" in serverAddress):
            host, port = serverAddress.split(":")
        else:
            host = serverAddress
            port = 14785

        client.serverConnect(host, port)

    else:
        print(errorMessage)
