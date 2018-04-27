#!/usr/bin/python
#-*-coding:utf-8-*-


class CmdClass:
    def __init__(self, client):
        self.commandErrorMessage = "Error while using this command, for help use /help server"
        self.client = client

    def addServer(self, name, host):
        self.client.servers[name] = host

    def delServer(self, name):
        try:
            del self.client.servers[name]
        except:
            print(self.commandErrorMessage)

    def serverList(self):
        print("\n", end="")
        print("serverName | serverHost | (fav)\n")
        for s in self.client.servers.keys():
            if(s in self.client.bestServers):
                if(self.client.clientConfig["colorSupporting"]):
                    print("\x1b[1;32m"+s+"\x1b[0m | "+self.client.servers[s]+" | \x1b[1;33mFav\x1b[0m")
                else:
                    print(s+" | "+self.client.servers[s]+" | Fav")
            else:
                if(self.client.clientConfig["colorSupporting"]):
                    print("\x1b[1;32m"+s+"\x1b[0m | "+self.client.servers[s])
                else:
                    print(s+" | "+self.client.servers[s])
        print("\n", end="")


    def addFavServer(self, name):
        serverExist = False
        for key in self.client.servers.keys():
            if(key == name):
                serverExist = True

        if(not serverExist):
            print("Error > The server "+name+" is not existing !")
        else:
            self.client.bestServers.append(name)

    def delFavServer(self, name):
        serverExist = False
        for server in self.client.bestServers:
            if(server == name):
                serverExist = True

        if(not serverExist):
            print("Error > The server "+name+" is not in your favorite servers list !")
        else:
            del self.client.bestServers[self.client.bestServers.index(name)]

    def listFav(self):
        print("serverName | serverHost\n")
        for server in self.client.bestServers:
            if(self.client.clientConfig["colorSupporting"]):
                print("\x1b[1;32m"+server+"\x1b[0m | "+self.client.servers[server]+"")
            else:
                print(server+" | "+self.client.servers[server]+"")

        print("\n", end="")


def serverCmd(command, client):
    cmd = CmdClass(client)

    if(len(command) == 1):
        print(cmd.commandErrorMessage)
    else:
        if(command[1] == "add"):
            if(len(command) == 2):
                print("Adding new Livia server... ")
                serverName = input("Server name > ")
                serverHost = input("Server host > ")
                cmd.addServer(serverName, serverHost)
                print("Added "+serverName+"\n")

            elif(len(command) == 4):
                cmd.addServer(command[3], command[2])

            else:
                print(cmd.commandErrorMessage)
                print("If your placed spaces in the server name you can't !")

        elif(command[1] == "del"):
            if(len(command) == 3):
                cmd.delServer(command[2])
            else:
                print(cmd.commandErrorMessage)

        elif(command[1] == "list"):
            cmd.serverList()

        elif(command[1] == "fav"):
            if(command[2] == "add"):
                if(len(command) == 3):
                    print("For adding new Favorite, your server need to be on the basic server list :")
                    cmd.serverList()
                    cmd.addFavServer(input("Server name (In the basic list) > "))

                elif(len(command) == 4):
                    cmd.addFavServer(command[3])

                else:
                    print(cmd.commandErrorMessage)

            elif(command[2] == "del"):
                cmd.delFavServer(command[3])

            elif(command[2] == "list"):
                cmd.listFav()

            else:
                print(cmd.commandErrorMessage)
        else:
            print(cmd.commandErrorMessage)
