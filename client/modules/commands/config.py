#!/usr/bin/python
#-*-coding:utf-8-*-
from getpass import getpass
from hashlib import sha1

def configCmd(command, client):
    commandErrorMessage = "Error while using this command, for help use /help config"
    if(len(command) == 1):
        print(commandErrorMessage)
    else:
        if(command[1] == "name"):
            if(len(command) == 3):
                # Checking username
                userPseudo = command[2]
                authorizedChars = list("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890_")
                validity = True

                for c in userPseudo:
                    if(not c in authorizedChars):
                        validity = False
                        print("Error > Your username need to contains letters and digits !")
                if(len(userPseudo) > 15):
                    validity = False
                    print("Error > Your pseudo need to contains under 15 characters !")
                if(len(userPseudo) < 5):
                    validity = False
                    print("Error > Your pseudo need to contains above 5 characters !")

                if(validity):
                    client.clientConfig["username"] = userPseudo

            else:
                print(commandErrorMessage)
                print("If you placed spaces on your username, you can't !")

        elif(command[1] == "color"):
            if(len(command) == 3):
                if(command[2].lower() == "on"):
                    client.clientConfig["colorSupporting"] = True
                    print("\x1b[0;32mEnabled text coloration\x1b[0m")
                elif(command[2].lower() == "off"):
                    client.clientConfig["colorSupporting"] = False
                    print("Disabled text coloration")
                else:
                    print("Error > You need to choose : ON or OFF !")
            else:
                print(commandErrorMessage)

        elif(command[1] == "password"):
            if(len(command) >= 2):
                print("Please enter your password, it is recommended to use a strong password !")
                client.clientConfig["password"] = sha1(getpass().encode()).hexdigest()
        else:
            print(commandErrorMessage)
