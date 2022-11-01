import socket
s = socket.socket ()
host = socket.gethostname ()
s.connect ((host,80))

while True :
    print((s.recv(1024)).decode ("UTF-8"))
    msg = input ("\nReply : ")
    s.send (msg.encode())