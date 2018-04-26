#!/usr/bin/python
#-*-coding:utf-8-*-
def serverCmd(command, client):
    commandErrorMessage = "Error while using this command, for help use /help server"
    if(len(command) == 1):
        print(commandErrorMessage)
    else:
        if(command[1] == "add"):
            if(len(command) == 4):
                host = command[2]
                serverName = command[3]
                client.servers[serverName] = host
            else:
                print(commandErrorMessage)
                print("If your placed spaces in the server name you can't !")

        elif(command[1] == "del"):
            if(len(command) == 3):
                del client.servers[command[2]]
            else:
                print(commandErrorMessage)

        elif(command[1] == "list"):
            print("\n", end="")
            print("serverName | serverHost | (fav)\n")
            for s in client.servers.keys():
                if(s in client.bestServers):
                    if(client.clientConfig["colorSupporting"]):
                        print("\x1b[1;32m"+s+"\x1b[0m | "+client.servers[s]+" | \x1b[1;33mFav\x1b[0m")
                    else:
                        print(s+" | "+client.servers[s]+" | Fav")
                else:
                    if(client.clientConfig["colorSupporting"]):
                        print("\x1b[1;32m"+s+"\x1b[0m | "+client.servers[s])
                    else:
                        print(s+" | "+client.servers[s])

            print("\n", end="")

        elif(command[1] == "fav"):
            if(command[2] == "add"):
                serverName = command[3]
                serverExist = False

                for key in client.servers.keys():
                    if(key == serverName):
                        serverExist = True

                if(not serverExist):
                    print("Error > The server "+serverName+" is not existing !")
                else:
                    client.bestServers.append(serverName)

            elif(command[2] == "del"):
                serverName = command[3]
                serverExist = False
                for server in client.bestServers:
                    if(server == serverName):
                        serverExist = True

                if(not serverExist):
                    print("Error > The server "+serverName+" is not in your favorite servers list !")
                else:
                    del client.bestServers[client.bestServers.index(serverName)]

            elif(command[2] == "list"):
                print("serverName | serverHost\n")
                for server in client.bestServers:
                    if(client.clientConfig["colorSupporting"]):
                        print("\x1b[1;32m"+server+"\x1b[0m | "+client.servers[server]+"")
                    else:
                        print(server+" | "+client.servers[server]+"")

                print("\n", end="")

            else:
                print(commandErrorMessage)
        else:
            print(commandErrorMessage)
