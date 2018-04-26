#!/usr/bin/python
#-*-coding:utf-8-*-

def helpCmd(command, client):
    if(len(command) == 1):
        if(client.clientConfig["colorSupporting"]):
            print("""
    \x1b[1;31mList of little commands:\x1b[0m
        \x1b[0;32mClear console\x1b[0m  ->  /clear
        \x1b[0;32mLeave app\x1b[0m      ->  /exit
        \x1b[0;32mGet your info\x1b[0m  ->  /info
        \x1b[0;32mConnect to server\x1b[0m -> /connect <serverName>

    \x1b[1;31mList of Domains:\x1b[0m
        \x1b[0;32mServers management\x1b[0m -> /help servers
        \x1b[0;32mClient configuration\x1b[0m -> /help config

""")
        else:
            print("""
    List of little commands:
        Clear console  ->  /clear
        Leave app      ->  /exit
        Get your info  ->  /info
        Connect to server -> /connect <serverName>

    List of Domains:
        Servers management -> /help server
        Client configuration -> /help config

""")
    else:
        if(command[1] == "server"):
            if(client.clientConfig["colorSupporting"]):
                print("""
    \x1b[1;31mServers help:\x1b[0m
        For precise the server port just add :port after server address !

        \x1b[0;32mGet saved servers\x1b[0m -> /server list
        \x1b[0;32mAdd new server\x1b[0m ->  /server add <host> <name>
        \x1b[0;32mRemove server\x1b[0m  ->  /server del <name>

        \x1b[0;32mGet favorite servers\x1b[0m -> /server fav list
        \x1b[0;32mFavorite server add\x1b[0m -> /server fav add <name>
        \x1b[0;32mFavorite server del\x1b[0m -> /server fav del <name>

""")
            else:
                print("""
    Servers help:
        For precise the server port just add :port after server address !

        Get saved servers -> /server list
        Add new server ->  /server add <host> <name>
        Remove server  ->  /server del <name>

        Get favorite servers -> /server fav list
        Favorite server add -> /server fav add <name>
        Favorite server del -> /server fav del <name>

""")
        elif(command[1] == "config"):
            if(client.clientConfig["colorSupporting"]):
                print("""
    \x1b[1;31mClient configuration help:\x1b[0m

    Required:
        \x1b[0;32mYour name\x1b[0m     ->  /config name <YourUsername>
        \x1b[0;32mYour Password\x1b[0m ->  /config password <YourPassword>
        \x1b[0;32mColor support\x1b[0m ->  /config color <On/Off>

    Facultative:
        \x1b[0;32mYour Email\x1b[0m ->  /config email <yourMail>
        \x1b[0;32mIf you accept Private Messages\x1b[0m ->  /config privatemessages <on/off>

""")
            else:
                print("""
    Client configuration help:

    Required:
        Your name     ->  /config name <YourUsername>
        Your Password ->  /config password
        Color support ->  /config color <On/Off>

    Facultative:
        Your Email ->  /config email <yourMail> (Facultative)
        If you accept Private Messages ->  /config privatemessages <on/off>

""")
        else:
            print("This domain dosen't exist, for know all domains, type /help !")
