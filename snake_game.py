import pygame
import time
import random
pygame.init()
 
width = 800
length = 600
dis = pygame.display.set_mode((width, length))
pygame.display.set_caption('Snake Game')

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
blue = (0, 0, 225)
li_blue = (155, 209, 255)
 
game_over = False

clock = pygame.time.Clock()

block = 10
speed = 15

font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)

def dis_score(score):
    value = score_font.render("Your Score: " + str(score), True, li_blue)
    dis.blit(value, [0, 0])

def snake(snake_block, snake_list):
    for i in snake_list:
        pygame.draw.rect(dis, white, pygame.Rect(i[0], i[1], block, block))

def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [width/6, length/3])

def gameLoop(): 
    game_over = False
    game_close = False

    x = width/2
    y = length/2

    x_change = 0       
    y_change = 0

    snake_list = []
    snake_length = 1

    foodx = round(random.randrange(0, width - block) / 10.0) * 10.0
    foody = round(random.randrange(0, length - block) / 10.0) * 10.0

    while not game_over:
        while game_close == True:
            dis.fill(black)
            message('You Lost! Press Q-Quit or C-Play Again', li_blue)
            pygame.display.update()

            for event in pygame.event.get():
                ## if you want to exit not using q that this works as well
                if event.type == pygame.QUIT:
                    game_over = True
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN: 
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -block
                    y_change = 0
                elif event.key == pygame.K_RIGHT:
                    x_change = block
                    y_change = 0
                elif event.key == pygame.K_UP:
                    y_change = -block
                    x_change = 0
                elif event.key == pygame.K_DOWN:
                    y_change = block
                    x_change = 0
    
        if x >= width or x < 0 or y >= length or y < 0:
            game_close = True

        x += x_change
        y += y_change
        dis.fill(black)
        pygame.draw.rect(dis, blue, pygame.Rect(foodx, foody, block, block))
        snake_head = []
        snake_head.append(x)
        snake_head.append(y)
        snake_list.append(snake_head)

        if len(snake_list) > snake_length:
            del snake_list[0]

        for i in snake_list[:-1]:
            if i == snake_head:
                game_close = True

        snake(block, snake_list)
        dis_score(snake_length - 1)

        pygame.display.update()

        if x == foodx and y == foody:
            foodx = round(random.randrange(0, width - block) / 10.0) * 10.0
            foody = round(random.randrange(0, length - block) / 10.0) * 10.0
            snake_length += 1

        clock.tick(speed)
 
    pygame.quit()
    quit()

gameLoop()