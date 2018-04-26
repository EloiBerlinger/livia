#!/usr/bin/python
#-*-coding:utf-8-*-
from modules.client import Client
import os

print("""\x1b[0;32m
           :::        ::::::::::: :::     ::: :::::::::::     :::
          :+:            :+:     :+:     :+:     :+:       :+: :+:
         +:+            +:+     +:+     +:+     +:+      +:+   +:+
        +#+            +#+     +#+     +:+     +#+     +#++:++#++:
       +#+            +#+      +#+   +#+      +#+     +#+     +#+
      #+#            #+#       #+#+#+#       #+#     #+#     #+#
     ########## ###########     ###     ########### ###     ###\x1b[0m     Chat system
""")

if(os.path.getsize("database/client.livia") == 0):
    # If it is the first launching (Check if database/client.livia is empty)
     print("    \x1b[1;36mWELCOME\x1b[0m to your first \x1b[0;32mLivia\x1b[0m launch !")
     print("    Type \x1b[1;31m/help\x1b[0m to know all the commands !", end="\n\n")



# Creating Livia client:
client = Client()

while(not client.exit):
    print("----> "+client.site)
    command = input("$ ").lower().replace("/", "").split(" ")

    if(command[0] == "exit"):
        client.exit = True

    elif(command[0] == "help"):
        if(len(command) == 1):
            print("""
\x1b[1;31mList of little commands:\x1b[0m
    \x1b[0;32mClear console\x1b[0m ->  /clear
    \x1b[0;32mLeave app\x1b[0m     ->  /exit

\x1b[1;31mList of Domains:\x1b[0m
    \x1b[0;32mServers management\x1b[0m -> /help servers
    \x1b[0;32mClient configuration\x1b[0m -> /help config

""")
        else:
            if(command[1] == "servers"):
                print("""
\x1b[1;31mServers help:\x1b[0m

    \x1b[0;32mAdd new server\x1b[0m ->  /server add <host> <name>
    \x1b[0;32mRemove server\x1b[0m  ->  /server del <name>

    \x1b[0;32mFavorite server add\x1b[0m -> /server fav add <serverName>
    \x1b[0;32mFavorite server del\x1b[0m -> /server fav del <serverName>

""")
            elif(command[1] == "config"):
                print("""
\x1b[1;31mClient configuration help:\x1b[0m

Required:
    \x1b[0;32mYour name\x1b[0m     ->  /config name <YourUsername>
    \x1b[0;32mYour Password\x1b[0m ->  /config password <YourPassword>

Facultative:
    \x1b[0;32mYour Email\x1b[0m ->  /config email <yourMail> (Facultative)
    \x1b[0;32mIf you accept Private Messages\x1b[0m ->  /config privatemessages <on/off>

""")
            else:
                print("This domain dosen't exist, for know all domains, type /help !")

# Active commands (Not displaying a lot of text)

    elif(command[0] == "config"):
        commandErrorMessage = "Please specify configuration domain, for help use /help config"
        if(len(command) == 1):
            print(commandErrorMessage)
        else:
            pass

    elif(command[0] == "clear"):
        print(100*"\n")

    else:
        print("\nUnknow command, type /help\n")

# Closing client:
print("\nSaving your changes...")
print("Goodbye !")
