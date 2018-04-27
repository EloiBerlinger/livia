#!/usr/bin/python
#-*-coding:utf-8-*-
from modules.client import Client
from modules.commands.commandProcess import commandProcess
import os
import pickle

# Creating Livia client:

header = """\x1b[0;32m
           :::        ::::::::::: :::     ::: :::::::::::     :::
          :+:            :+:     :+:     :+:     :+:       :+: :+:
         +:+            +:+     +:+     +:+     +:+      +:+   +:+
        +#+            +#+     +#+     +:+     +#+     +#++:++#++:
       +#+            +#+      +#+   +#+      +#+     +#+     +#+
      #+#            #+#       #+#+#+#       #+#     #+#     #+#
     ########## ###########     ###     ########### ###     ###\x1b[0m     Chat system
"""

print(header)

if(os.path.getsize("database/client.livia") == 0):
    client = Client()
    client.log("ClientCreation", "Created new client")

    # If it is the first launching (Check if database/client.livia is empty)
    print("    \x1b[1;36mWELCOME\x1b[0m to your first \x1b[0;32mLivia\x1b[0m launch !")
    print("    Type \x1b[1;31m/help\x1b[0m to know all the commands !", end="\n\n")

    print("Do you have text coloration on your terminal or things like: \x1b[1;36m")
    print("1) Yes, i have text coloration and this text is blue !")
    print("2) No, i have this wierd thing '\x1b[1;36m'")
    choose = input("(1 / 2) > ")

    if(choose == "1"):
        client.clientConfig["colorSupporting"] = True
        client.log("Configuration", "Set text coloration ON")
    elif(choose == "2"):
        client.clientConfig["colorSupporting"] = False
        print("WELCOME to your first Livia launch !")
        print("Type /help to know all the commands !", end="\n\n")
        client.log("Configuration", "Set text coloration OFF")
    else:
        client.clientConfig["colorSupporting"] = False
    print("\x1b[0m", end="")


else:
    # Getting client from class:
    client = object()
    with open("database/client.livia", "rb") as file:
        fileUnpickle = pickle.Unpickler(file)
        client = fileUnpickle.load()
    client.log("Initialisation", "Sucessfull restored last client state")


# Commands:
while(not client.exit):
    print("----> "+client.site)
    command = input("$ ").lower().replace("/", "").split(" ")

    commandProcess(command, client)

# Closing client:
print("\nSaving your changes...")
client.saveClient()
print("Goodbye !")
