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