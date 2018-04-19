## Requirements:
* Programming in Python 3
* GIT usage [GitHUB Tutorial](http://try.github.io/), [Openclassrooms French Tutorial](https://openclassrooms.com/courses/gerer-son-code-avec-git-et-github)

## Steps for making a contribution:
1. Fork the Livia project to your Github account
2. Clone your fork in your local machine
3. Create a new branch in your local clone for your changes
4. Push your changed branch on your Github fork
5. Create an pull request and explain your changes, raisons etc...
6. Wait for one of the Livia developers either to include your change in the Livia Project


# Livia Functionning
## Messages types:
Livia uses an special code for define message types, there is the list of message types:  
*Message Format:* `CODE,USERNAME,CONTENT`  
The message code type **need to be on 3 digits** !  

| Type Name     |    Code     |    Example     |
| :------------- | :------------- | :------------- |
| Chat Message | 000 | `000,userName,"This is an simple chat Message"` |
| Private message | 001 | `001,fromUser,toUser,"This is an simple chat Message"` |
| Client data connection/register | 002 | `002,clientUserName,clientHashedPassword` |
| Server connection (confirmation/informations) | 003 | `003,fromUser,toUser,"This is an simple chat Message"` |
