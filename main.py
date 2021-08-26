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


def writeText(_coin, _score, _stage):
    global screen
    if _coin <= 0:
        gameOverFont = pygame.font.Font('font/bm.ttf', 50)
        stageFont = pygame.font.Font('font/bm.ttf', 30)
        gameOver = gameOverFont.render('GAME OVER', True, (255, 0, 0))
        stage = stageFont.render('STAGE ' + str(_stage), True, (255, 0, 0))
        textpos = gameOver.get_rect()
        textpos.center = (screenWidth / 2, screenHeight / 2)
        screen.blit(gameOver, textpos)
        screen.blit(stage, (130, 278))
        pygame.display.update()
        sleep(3)
        sys.exit()
    else:
        font = pygame.font.Font('font/bm.ttf', 15)
        coin = font.render('COIN: ' + str(_coin), True, (255, 0, 0))
        score = font.render('SCORE: ' + str(_score), True, (0, 0, 255))
        stage = font.render('STAGE: ' + str(_stage), True, (255, 0, 0))
        screen.blit(coin, (0, 0))
        screen.blit(score, (0, 15))
        screen.blit(stage, (295 , 0))

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

def runGame():
    global clock, background, rocket, missile, enemySpeed, coin, score, stage, stageCount

    moveX, moveY, shotCount = 0, 0, 0

    rocketSize, rocketWidth, rocketHeight = getSize(rocket)
    missileSize, missileWidth, missileHeight = getSize(missile)

    xpos, ypos = (screenWidth / 2) - (rocketWidth / 2), screenHeight * 0.9

    missileList = []

    enemy, enemySize, enemyWidth, enemyHeight, enemyPosx, enemyPosy = createEnemy()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type in [pygame.KEYDOWN]:
                if event.key == pygame.K_LEFT:
                    moveX -= 5

                elif event.key == pygame.K_RIGHT:
                    moveX += 5

                elif event.key == pygame.K_UP:
                    moveY -= 5

                elif event.key == pygame.K_DOWN:
                    moveY += 5

                elif event.key == pygame.K_SPACE:
                    missileX = xpos + rocketWidth / 2 - (missileWidth / 2)
                    missileY = ypos - (missileHeight / 2)
                    missileList.append([missileX, missileY])

            if event.type in [pygame.KEYUP]:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    moveX, moveY = 0, 0





def main():
    global screen, clock, background, rocket, missile
    pygame.init()
    screen = pygame.display.set_mode((screenWidth, screenHeight))
    pygame.display.set_caption('ShooterGame')
    background = pygame.image.load('images/background.png')
    rocket = pygame.image.load('images/rocket.png')
    missile = pygame.image.load('images/missile.png')
    clock = pygame.time.Clock()
    runGame()

main()