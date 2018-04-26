#!/usr/bin/python
#-*-coding:utf-8-*-
from modules.commands.help import *
from modules.commands.config import *
from modules.commands.server import *
from modules.commands.clear import *

def commandProcess(command, client):

    if(command[0] == "exit"):
        client.exit = True

    elif(command[0] == "help"):
        helpCmd(command, client)

    elif(command[0] == "config"):
        configCmd(command, client)

    elif(command[0] == "server"):
        serverCmd(command, client)

    elif(command[0] == "clear"):
        clearCmd()

    else:
        print("\nUnknow command, type /help\n")
