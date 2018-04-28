#!/usr/bin/python
#-*-coding:utf-8-*-
# Livia server user class file
class User:
    def __init__(self, socket, socketData, pseudo, password, otherInformations):
        self.socket = socket
        self.socketData = socketData
        self.pseudo = pseudo
        self.password = password
        self.otherInformations = otherInformations
