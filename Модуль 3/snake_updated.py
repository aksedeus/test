#coding: utf8

import pygame, time, random

pygame.init()

def snake(headname, bodyname, snakeList, snakeHead, lead_x, lead_y):
    for XnY in snakeList:
        gameDisplay.blit(pygame.image.load(bodyname),(XnY[0],XnY[1]))
        gameDisplay.blit(pygame.image.load(headname),(lead_x,lead_y))

def message_to_screen(msg,color,x,y):
    screen_text = font.render(msg, True, color)
    gameDisplay.blit(screen_text, [x,y])

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)

display_width = 600
display_height = 600
block_size = 40

font = pygame.font.SysFont(None, 32)
gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption("Snake GAME")

gameExit = False

lead_x = (display_width-40)/2
lead_y = (display_height-40)/2
lead_x_change = 0
lead_y_change = 0

snakeList = []
snakeLength = 1
score = 0

appleX = round(random.randrange(block_size, display_width-block_size)/block_size)*block_size
appleY = round(random.randrange(block_size, display_height-block_size)/block_size)*block_size

pygame.mixer.init()

pygame.mixer.music.load("2.wav")
pygame.mixer.music.play(-1)

sound1 = pygame.mixer.Sound('3.wav')
sound2 = pygame.mixer.Sound('3.wav')

while not gameExit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameExit = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                lead_x_change = -block_size
                lead_y_change = 0
            elif event.key == pygame.K_RIGHT:
                lead_x_change = block_size
                lead_y_change = 0
            elif event.key == pygame.K_DOWN:
                lead_y_change = block_size
                lead_x_change = 0
            elif event.key == pygame.K_UP:
                lead_y_change = -block_size
                lead_x_change = 0
            if event.key == pygame.K_q or event.key == pygame.K_ESCAPE:
                gameExit = True

    if lead_x >= display_width-block_size or lead_x <0 or lead_y >= display_height-block_size or lead_y <0:
        gameDisplay.fill(white)
        message_to_screen(''.join(["Game over! Score: ",str(score)]), black, 200,260)
        pygame.display.update()
        time.sleep(2)
        gameExit = True

    # движение змейки
    lead_x += lead_x_change
    lead_y += lead_y_change
    snakeHead = [lead_x, lead_y]
    snakeList.append(snakeHead)
    if len(snakeList) > snakeLength:
        del snakeList[0]

    # столкновение змейки с самой собой
    for eachSegment in snakeList[:-1]:
        if eachSegment == snakeHead:
            gameDisplay.blit(pygame.image.load('back.png'), (0, 0))
            message_to_screen(''.join(["Game over! Score: ",str(score)]), black, 200,260)
            pygame.display.update()
            time.sleep(2)
            gameExit = True

    # столкновение с яблоком
    if lead_x == appleX and lead_y == appleY:
        appleX = round(random.randrange(block_size, display_width-block_size)/block_size)*block_size
        appleY = round(random.randrange(block_size, display_height-block_size)/block_size)*block_size
        snakeLength += 1
        score += 1
        sound1.play()

    gameDisplay.blit(pygame.image.load('back.png'), (0, 0))
    # отображение количества очков
    message_to_screen(''.join(["Score: ",str(score)]), black, 10,10)
    # отображение яблока
    gameDisplay.blit(pygame.image.load('grib.png'),(appleX, appleY))
    # отображение змейки
    snake('test.png', 'test.png', snakeList, snakeHead, lead_x, lead_y)
    pygame.display.update()
    pygame.time.delay(150)

pygame.mixer.music.stop()
pygame.quit()