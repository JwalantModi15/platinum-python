import pygame
from random import randrange
pygame.init()
screen_width = 800
screen_height = 500

win = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Snake")
pygame.display.update()
white = (255,255,255)
red = (255,0,0)
black = (0,0,0)
green = (34,139,34)
game_close = False
start_x = 100
start_y=100
update_x = 0
update_y = 0
size_x = 21
size_y = 21
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 35)

def text_on_screen(text,color, x, y):
    screen_text = font.render(text,True, color)
    win.blit(screen_text, [x, y])

def snake(sn_list):
    for x,y in sn_list:
        pygame.draw.rect(win, black, [x, y, size_x,size_y])

def main_gameloop():
    global game_close
    start_x = 100
    start_y=100
    update_x = 0
    update_y = 0
    size_x = 21
    size_y = 21
    food_x = randrange(50, 750)
    food_y = randrange(50, 500)
    game_over = False
    s_length = 1
    snake_list = []
    while not game_close:
        pygame.display.update()
        if game_over==True:
            win.fill(white)
            text_on_screen("You Lose!, Press Enter to Play Again", red, 155, 230) #155,230

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_close = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        main_gameloop() 

        else:    
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_close = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        update_x=-21
                        update_y=0
                    elif event.key == pygame.K_RIGHT:
                        update_x=21
                        update_y=0 
                    elif event.key == pygame.K_UP:
                        update_y=-21
                        update_x=0 
                    elif event.key == pygame.K_DOWN:
                        update_y =+21
                        update_x=0
                                 

            start_x += update_x
            start_y += update_y
            clock.tick(8)
            win.fill(green)
            pygame.draw.circle(win, red, (food_x, food_y), 12)
            head = []
            head.append(start_x)
            head.append(start_y)
            snake_list.append(head)

            if abs(start_x-food_x)<21 and abs(start_y-food_y)<21:
                s_length+=1
                food_x = randrange(50, 700)
                food_y = randrange(50, 475)
                pygame.draw.circle(win, red, (food_x, food_y), 12)
            
            if len(snake_list)>s_length:
                del(snake_list[0])      

            if head in snake_list[:-1]:
                game_over = True      

            if start_y > screen_height:
                start_y=0

            if start_x > screen_width:
                start_x=0

            if start_x < 0:
                start_x=screen_width

            if start_y < 0:
                start_y = screen_height        

            snake(snake_list)    

main_gameloop()