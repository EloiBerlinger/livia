#!/usr/bin/python
#-*-coding:utf-8-*-
def infoCmd(client):
    # text coloration state
    print("Text coloration: ", end="")
    if(client.clientConfig["colorSupporting"]):
        print("\x1b[0;32menabled\x1b[0m")
    else:
        print("disabled")

    # username
    print("Username: ", end="")
    if(client.clientConfig["username"] != ""):
        print(client.clientConfig["username"])
    else:
        print("NOT CONFIGURED")


    print("\n", end="")
