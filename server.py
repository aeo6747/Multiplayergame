from socket import *
import pygame
import sys

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

white = (255, 255, 255)
black = (0, 0, 0)

pygame.init()
pygame.display.set_caption("Server")
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pos_x = 200
pos_y = 200

epos_x = 300
epos_y = 200

port = 8080

serverSock = socket(AF_INET, SOCK_STREAM)
serverSock.bind(('', port))
serverSock.listen(1)

print('%d번 포트로 접속 대기중'%port)

connectionSock, addr = serverSock.accept()

print(str(addr), '에서 접속되었습니다.')

sendData = f"{pos_x} {pos_y}"
connectionSock.send(sendData.encode('utf-8'))

while True:
    sendData = f"{pos_x} {pos_y}"

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    key_event = pygame.key.get_pressed()

    if key_event[pygame.K_LEFT]:
        pos_x -= 1
        connectionSock.send(sendData.encode('utf-8'))
    elif key_event[pygame.K_RIGHT]:
        pos_x += 1
        connectionSock.send(sendData.encode('utf-8'))
    elif key_event[pygame.K_UP]:
        pos_y -= 1
        connectionSock.send(sendData.encode('utf-8'))
    elif key_event[pygame.K_DOWN]:
        pos_y += 1
        connectionSock.send(sendData.encode('utf-8'))
    
    connectionSock.send(sendData.encode('utf-8'))

    recvData = connectionSock.recv(1024)
    
    qt = recvData.decode('utf-8').split()

    epos_x = int(qt[0])
    epos_y = int(qt[1])

    screen.fill(black)
    pygame.draw.circle(screen, white, (pos_x, pos_y), 20)
    pygame.draw.circle(screen, white, (epos_x, epos_y), 20)

    pygame.display.update()
