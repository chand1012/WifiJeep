import socket
import sys
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = sys.argv[1]
port = None
try:
    port = int(sys.argv[2])
except IndexError:
    port = 1166

print("Starting client to {} on port {}...".format(host, port))
s.connect((host, port))
print("Connected!")

while True:
    msg = input(":")
    snd = msg.strip().encode('ascii')
    s.send(snd)
    if msg.strip()=='exit' or msg.strip()=='stop':
        break
s.close()


