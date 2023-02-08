import pygame
from sys import exit

pygame.init()
pygame.display.set_caption('shot')

clock = pygame.time.Clock()
resolution=(1500,800)
clock = pygame.time.Clock()
screen = pygame.display.set_mode(resolution)

player_surf = pygame.image.load('grap/player/player.png').convert_alpha()
player_rect = player_surf.get_rect(center=(resolution[0]/2,resolution[1]/2))

def walkingAnimation(frame, player):
    if frame%2==1:
        player = pygame.image.load('grap/player/player1.png').convert_alpha()
    else:
        player = pygame.image.load('grap/player/player2.png').convert_alpha()
    return player

def  walking(playerRect, playerSurf, speed, frame):
    userInput = pygame.key.get_pressed()
    maxSpeed=11
    acceleration = 1
    braking = 1
    if userInput[pygame.K_LEFT]: #LEFT
        if speed[0] <= maxSpeed:
            speed[0] += acceleration
        playerSurf = walkingAnimation(frame, playerSurf)
        playerRect.x -= playerSpeed[0]
    else:
        if speed[0] >= 1:
            speed[0] -= braking
    if userInput[pygame.K_RIGHT]: #RIGHT
        if speed[1] <= maxSpeed:
            speed[1] += acceleration
        playerSurf = walkingAnimation(frame, playerSurf)
        playerRect.x += playerSpeed[1]
    else:
        if speed[1] >= 1:
            speed[1] -= braking
    if userInput[pygame.K_UP]: #UP
        if speed[2] <= maxSpeed:
            speed[2] += acceleration
        playerSurf = walkingAnimation(frame, playerSurf)
        playerRect.y -= playerSpeed[2]
    else:
        if speed[2] >= 1:
            speed[2] -= braking
    if userInput[pygame.K_DOWN]: #DOWN
        if speed[3] <= maxSpeed:
            speed[3] += acceleration
        playerSurf = walkingAnimation(frame, playerSurf)
        playerRect.y += playerSpeed[3]
    else:
        if speed[3] >= 1:
            speed[3] -= braking

    return playerRect,playerSurf


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

    
    player_rect, player_surf = walking(player_rect,player_surf,playerSpeed,frames)
        
    screen.blit(player_surf,player_rect)
    if frames>=60:
        frames=0
    else:
        frames+=1
    pygame.display.update()
    clock.tick(60)
