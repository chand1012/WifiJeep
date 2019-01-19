import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = '192.168.1.18'

port = 1166

s.connect((host, port))
print("Starting client")
while True:
    msg = input(":")
    snd = msg.strip().encode('ascii')
    s.send(snd)
    if msg.strip()=='exit':
        break

s.close()


