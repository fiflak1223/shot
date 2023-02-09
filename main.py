import pygame
import math
from sys import exit

pygame.init()
pygame.display.set_caption('shot')

clock = pygame.time.Clock()
resolution=(1500,800)
clock = pygame.time.Clock()
screen = pygame.display.set_mode(resolution)

player_surf = pygame.image.load('grap/player/player.png').convert_alpha()
player_rect = player_surf.get_rect(center=(resolution[0]/2,resolution[1]/2))
armGun_surf = pygame.image.load('grap/armGun.png').convert_alpha()
armGun_rect = armGun_surf.get_rect(center=(resolution[0]/2+2,resolution[1]/2+2))

def walkingAnimation(frame, player):
    if frame%20>10:
        player = pygame.image.load('grap/player/player1.png').convert_alpha()
    else:
        player = pygame.image.load('grap/player/player2.png').convert_alpha()
    return player

def  walking(playerRect, playerSurf, armGunRect, speed, frame):
    userInput = pygame.key.get_pressed()
    maxSpeed=3
    acceleration = 0.2
    braking = 0.2
    if userInput[pygame.K_LEFT]: #LEFT
        if speed[0] <= maxSpeed:
            speed[0] += acceleration
        playerSurf = walkingAnimation(frame, playerSurf)
        playerRect.x -= playerSpeed[0]
        armGunRect.x -= playerSpeed[0]
    else:
        if speed[0] >= 1:
            speed[0] -= braking
    if userInput[pygame.K_RIGHT]: #RIGHT
        if speed[1] <= maxSpeed:
            speed[1] += acceleration
        playerSurf = walkingAnimation(frame, playerSurf)
        playerRect.x += playerSpeed[1]
        armGunRect.x += playerSpeed[1]
    else:
        if speed[1] >= 1:
            speed[1] -= braking
    if userInput[pygame.K_UP]: #UP
        if speed[2] <= maxSpeed:
            speed[2] += acceleration
        playerSurf = walkingAnimation(frame, playerSurf)
        playerRect.y -= playerSpeed[2]
        armGunRect.y -= playerSpeed[2]
    else:
        if speed[2] >= 1:
            speed[2] -= braking
    if userInput[pygame.K_DOWN]: #DOWN
        if speed[3] <= maxSpeed:
            speed[3] += acceleration
        playerSurf = walkingAnimation(frame, playerSurf)
        playerRect.y += playerSpeed[3]
        armGunRect.y += playerSpeed[3]
    else:
        if speed[3] >= 1:
            speed[3] -= braking

    return playerRect,playerSurf,armGunRect

def rotateGun(armGunSurf,armGunRect):
    mX, mY = pygame.mouse.get_pos()
    rX, rY = abs(mX - armGunRect.x), abs(mY-armGunRect.y)
    angle = int(math.degrees(math.atan(rY/rX)))
    #print(angle)
    #armGunSurf = pygame.transform.rotate(armGunSurf,angle)
    return armGunSurf
frames=0
playerSpeed=[0,0,0,0]
while True:
    screen.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYUP:
            player_surf = pygame.image.load('grap/player/player.png').convert_alpha()

    
    player_rect, player_surf, armGun_rect = walking(player_rect,player_surf,armGun_rect,playerSpeed,frames)
        
    #armGun_surf = pygame.transform.rotate(armGun_surf,90)
    armGun_surf = rotateGun(armGun_surf,armGun_rect)
    screen.blit(player_surf,player_rect)
    screen.blit(armGun_surf,armGun_rect)
    if frames>=60:
        frames=0
    else:
        frames+=1
    pygame.display.update()
    clock.tick(10)
