import random
import pygame
import time

pygame.init()

collision_sound = pygame.mixer.Sound("collision2.wav")
pygame.mixer.music.load("lineOfFire.mp3")




screen_width = 600
screen_height = 600

black = (0,0,0)
white = (255,255,255)
red = (200,0,0)
green = (0, 200, 0)

bright_red = (255,0,0)
bright_green = (0, 255, 0)

gameDisplay = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption('Catch the ball')
clock = pygame.time.Clock()

paddleImg = pygame.image.load('paddle3.png')
paddle_width = 100
paddle_height = 40

ballImg = pygame.image.load('ball2.jpg')
ball_width = 50
ball_height = 51

pause = False

def gameIntro():

    intro = True

    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()


        gameDisplay.fill(white)
        largeText = pygame.font.SysFont("freesansbold.ttf", 80)
        TextSurf, TextRect = text_objects("Catch the ball!", largeText)
        TextRect.center = ((screen_width / 2), (screen_height / 2))
        gameDisplay.blit(TextSurf, TextRect)


        button("Catch!", 150,450,100,50, green,bright_green, game_loop)
        button("Exit", 350, 450, 100, 50, red, bright_red, game_quit)


        pygame.display.update()
        clock.tick(15)




def button(msg, x,y,width,height, darkColor, brightColor, action = None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x + width > mouse[0] > x and y + height > mouse[1] > y:
        pygame.draw.rect(gameDisplay, brightColor, (x, y, width, height))

        if click[0] == 1 and action != None:
            action()

    else:
        pygame.draw.rect(gameDisplay, darkColor, (x, y, width, height))

    smallTextCatch = pygame.font.SysFont("freesansbold.ttf", 20)
    textSurfCatch, textRectCatch = text_objects(msg, smallTextCatch)
    textRectCatch.center = ((x + (width / 2)), (y + (height / 2)))
    gameDisplay.blit(textSurfCatch, textRectCatch)


def game_quit():
    pygame.quit()
    quit()

def game_pause():

    pygame.mixer.music.pause()


    while pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()


        largeText = pygame.font.SysFont("freesansbold.ttf", 80)
        TextSurf, TextRect = text_objects("Paused", largeText)
        TextRect.center = ((screen_width / 2), (screen_height / 2))
        gameDisplay.blit(TextSurf, TextRect)


        button("Continue", 150,450,100,50, green,bright_green, game_unpause)
        button("Exit", 350, 450, 100, 50, red, bright_red, game_quit)



        pygame.display.update()
        clock.tick(15)

def game_unpause():
    pygame.mixer.music.set_volume(0.2)
    pygame.mixer.music.play(-1)

    global pause
    pause = False


def gameScore(score):
    font = pygame.font.SysFont(None, 25)
    text = font.render("Score: " + str(score), True, black)
    gameDisplay.blit(text, (500, 0))

def gameEndScore(score):
    largeTextScore = pygame.font.SysFont("freesansbold.ttf", 50)
    TextSurfScore, TextRectScore = text_objects("Score: " + str(score), largeTextScore)
    TextRectScore.center = ((screen_width / 0.5), (screen_height / 0.5))
    gameDisplay.blit(TextSurfScore, TextRectScore)

def gameLivesLeft(count):
    font = pygame.font.SysFont(None, 25)
    text = font.render("Game Lives: " + str(count), True, black)
    gameDisplay.blit(text, (0,0))

def paddle(paddleX, paddleY):
    gameDisplay.blit(paddleImg, (paddleX,paddleY))

def ball(ballX, ballY):
    gameDisplay.blit(ballImg, (ballX, ballY))

def text_objects(text, font):
    textSurface = font.render(text, True, black)

    return textSurface, textSurface.get_rect()



def message_display(text):
    largeText = pygame.font.SysFont("freesansbold.ttf", 100)
    TextSurf, TextRect  = text_objects(text, largeText)
    TextRect.center = ((screen_width/2),(screen_height/2))
    gameDisplay.blit(TextSurf, TextRect)
    pygame.display.update()
    time.sleep(2)
    game_loop()


def gameOver(score):

    pygame.mixer.music.stop()


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()


        gameDisplay.fill(white)
        largeTextGameOver = pygame.font.SysFont("freesansbold.ttf", 80)
        TextSurfGameOver, TextRectGameOver = text_objects("Game over!", largeTextGameOver)
        TextRectGameOver.center = ((screen_width / 2), (screen_height / 2))
        gameDisplay.blit(TextSurfGameOver, TextRectGameOver)

        largeTextScore = pygame.font.SysFont("freesansbold.ttf", 50)
        TextSurfScore, TextRectScore = text_objects("Score: " + str(score), largeTextScore)
        TextRectScore.center = (300, 380)
        gameDisplay.blit(TextSurfScore, TextRectScore)


        button("Play again", 150,450,105,50, green,bright_green, game_loop)
        button("Exit", 350, 450, 100, 50, red, bright_red, game_quit)



        pygame.display.update()
        clock.tick(15)


def game_loop():

    global pause

    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(-1)




    paddleX = (screen_width * 0.45)
    paddleY = (screen_height * 0.93)
    paddleX_change = 0
    paddleSpeed = 9


    ballX = random.randrange(0, screen_width - ball_width)
    ballY = 0
    ballSpeed = 5
    ballMotionX = (-1)**random.randrange(0,10) + random.randrange(0,20) - 5
    ballMotionY = 1 + ballSpeed


    gameLives = 3
    score = 0

    gameExit = False

    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    paddleX_change = -paddleSpeed
                if event.key == pygame.K_RIGHT:
                    paddleX_change = paddleSpeed
                if event.key == pygame.K_p:
                    pause = True
                    game_pause()

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    paddleX_change = 0




        paddleX += paddleX_change
        gameDisplay.fill(white)
        gameLivesLeft(gameLives)
        gameScore(score)

        ball(ballX, ballY)
        ballX += ballMotionX
        ballY += ballMotionY

        #kolizija sa ivicama ekrana
        if ballX > screen_width - ball_width:
           pygame.mixer.Sound.play(collision_sound)
           ballMotionX *= -1
        elif ballX < 0:
            pygame.mixer.Sound.play(collision_sound)
            ballMotionX *= -1


        #momenat kada loptica prodje screen_height
        if ballY > screen_height:
            ballX = random.randrange(0, screen_width - ball_width)
            ballY = 0
            ballMotionX = (-1)**random.randrange(0,10) + random.randrange(0,20) - 5
            ballMotionY = 1 + ballSpeed

            gameLives -= 1

            if gameLives == 0:
                gameOver(score)

        paddle(paddleX,paddleY)

        #pomeranje reketa
        if paddleX < 0:
            paddleX = paddleX_change
        elif paddleX > screen_width - paddle_width:
            paddleX -= paddleX_change

        pointX = ballX + ball_width
        pointY = ballY + ball_height
        paddleX1 = paddleX
        paddleX2 = paddleX + paddle_width
        paddleY1 = paddleY
        paddleY2 = paddleY + paddle_height

        if paddleY1 < pointY and pointY < paddleY2 and pointX > paddleX1 and pointX < paddleX2:
            pygame.mixer.Sound.play(collision_sound)
            score += 1

            if score % 10 == 0:
                ballSpeed += 1
                ballX = random.randrange(0, screen_width - ball_width)
                ballY = 0
                ballMotionX = (-1) ** random.randrange(0, 10) + random.randrange(0, 20) - 5
                ballMotionY = 1 + ballSpeed
            else:
                ballX = random.randrange(0, screen_width - ball_width)
                ballY = 0
                ballMotionX = (-1) ** random.randrange(0, 10) + random.randrange(0, 20) - 5
                ballMotionY = 1 + ballSpeed

        pygame.display.update()
        clock.tick(60)


gameIntro()
game_loop()

pygame.quit()
quit()