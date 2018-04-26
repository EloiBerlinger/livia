#!/usr/bin/python
#-*-coding:utf-8-*-
def configCmd(command, client):
    commandErrorMessage = "Error while using this command, for help use /help config"
    if(len(command) == 1):
        print(commandErrorMessage)
    else:
        if(command[1] == "name"):
            if(len(command) == 3):
                # Checking username
                userPseudo = command[2]
                authorizedChars = list("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890")
                validity = True

                for c in userPseudo:
                    if(not c in authorizedChars):
                        validity = False
                        print("Error > Your username need to contains letters and digits !")
                if(len(userPseudo) > 15):
                    validity = False
                    print("Error > Your pseudo need to contains under 15 characters !")

                if(validity):
                    client.clientConfig["username"] = userPseudo

            else:
                print(commandErrorMessage)
                print("If you placed spaces on your username, you can't !")
