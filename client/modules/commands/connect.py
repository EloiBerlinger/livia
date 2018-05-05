#!/usr/bin/python
#-*-coding:utf-8-*-
def connectCmd(command, client):
     # Check client configuration password and name
     # /connect <serverName/serverHost:port>
     # Get command serverHost

    errorMessage = "Error while usine /connect, use /help"

    if(len(command) == 1):
        # If user command is just /connect
        host = input("Server host > ")
        port = input("Server port (Keep empty for use default port) > ")

        if(port == ""):
            port = 14785

        client.serverConnect(host, port)

    elif(len(command) == 2):
        # If user precised server host
        serverAddress = command[1]

        if(":" in serverAddress):
            # If port is precised
            host, port = serverAddress.split(":")
        else:
            # If port not precised
            host = serverAddress
            port = 14785

        client.serverConnect(host, port)

    else:
        print(errorMessage)
