import pygame, sys, random
from time import sleep


screenWidth = 360
screenHeight = 480
enemySpeed = 3
coin = 3
score = 0
stage = 1
stageCount = 0

enemyList = [ 'images/alien0.png', 'images/alien1.png', 'images/alien2.png', 'images/rocket1.png', 'images/rocket2.png', ]


def drawImage(_img, _x , _y):
    global screen
    screen.blit(_img, (_x, _y))

def getSize(obj):
    size = obj.get_rect().size
    width = size[0]
    height = size[1]
    return size, width, height

def createEnemy():
    enemy = pygame.image.load(random.choice(enemyList))
    size, width, height = getSize(enemy)
    xpos = random.randrange(0, screenWidth - width)
    ypos = -42
    return enemy, size, width, height, xpos, ypos
