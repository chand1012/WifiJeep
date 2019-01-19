import socket
import sys
import signal
import serial

arduino = serial.Serial('/dev/ttyACM0', 9600) #this will change if running this on windows but this is for linux
arduino.write(b'0')
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

host = sys.argv[1]
port = None
try:
    port = int(sys.argv[2])
except IndexError:
    port = 1166

server.bind((host, port))

server.listen(5)
print("Starting server")
while True:
    client, addr = server.accept()

    print("Connection from %s" % str(addr))

    while True:
        cmd = client.recv(1024)
        command = cmd.decode('ascii').strip()
        # gets command from client and processes it
        if command=='':
            pass
        else:
            print('Command sent: %s' % command)
            bytecmd = b'%b' % command
            arduino.write(bytecmd)
    client.close()

        