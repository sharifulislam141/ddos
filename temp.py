import socket,terminal_banner
print(socket.gethostbyname('sherpurgovtcollege.edu.bd'))

TARGET = input("enter a word : ") or ("hello word")
port = input("Enter port or just click enter for default : ") or  80
 
print(type (port))
banner_text = "This is my banner text.\n\nThis is a second line of text."
my_banner = terminal_banner.Banner(banner_text)
print(my_banner)