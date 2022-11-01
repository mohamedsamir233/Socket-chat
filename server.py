import socket 
s = socket.socket ()
host = socket.gethostname ()
s.bind ((host,80))
s.listen (5)
c , addr = s.accept ()
print ("Get Connection from",addr)
c.send (b"Welcome to my Server .")
while True :
    data = c.recv (1024)
    print (data.decode ("UTF-8"))
    msg = input ("\nReply : ")
    c.send (msg.encode())