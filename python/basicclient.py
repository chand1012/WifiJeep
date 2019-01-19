import pygame, sys
import socket

host = sys.argv[1]
port = None
try:
    port = int(sys.argv[2])
except IndexError:
    port = 1166

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
pygame.init()
screen = pygame.display.set_mode((400, 300))
print("Starting client to {} on port {}...".format(host, port))
s.connect((host, port))
print("Connected!")
n = 0
keydown = False
while True:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit(0)
                    s.close()
                if event.type == pygame.KEYDOWN:
                    keydown = True
        
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_UP]: 
            n = 2
        elif pressed[pygame.K_DOWN]: 
            n = 3
        else:
            n = 1

        if pressed[pygame.K_LEFT]: 
            n = 5
        elif pressed[pygame.K_RIGHT]: 
            n = 4
        else:
            n = 0 

        if pressed[pygame.K_ESCAPE]:
            pygame.quit()

        s.send(str(n).encode('ascii'))
        pygame.display.update()
        