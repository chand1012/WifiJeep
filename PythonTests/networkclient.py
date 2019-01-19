import socket
import sys
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = sys.argv[1]

port = int(sys.argv[2])

s.connect((host, port))
print("Starting client")
while True:
    msg = input(":")
    snd = msg.strip().encode('ascii')
    s.send(snd)
    if msg.strip()=='exit' or msg.strip()=='stop':
        break

s.close()


