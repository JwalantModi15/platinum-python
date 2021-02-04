import pygame
import random
pygame.init()

# Colors
silver = (192,192,192)
grey = (211,211,211)
green = (144,238,144)
white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)
brown = (165,42,42)
ch = (silver,grey,green)
# Creating window
screen_width = 1000
screen_height = 700
gameWindow = pygame.display.set_mode((screen_width, screen_height))

# Game Title
pygame.display.set_caption("Snakes Eats")
pygame.display.update()
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 35)

def text_screen(text, color, x, y):
    screen_text = font.render(text, True, color)
    gameWindow.blit(screen_text, [x,y])


def plot_snake(gameWindow, color, snk_list, snake_size):
    for x,y in snk_list:
        pygame.draw.rect(gameWindow, color, [x, y, snake_size, snake_size])

# Game Loop
def gameloop(init_velocity):
    # Game specific variables
    exit_game = False
    game_over = False
    snake_x = 45
    snake_y = 55
    velocity_x = 0
    velocity_y = 0
    snk_list = []
    snk_length = 1
    init_score = 100
    c = 0
    count=1
    stone_x = random.randint(10, screen_width - 100)
    stone_y = random.randint(10, screen_height - 100)

    food_x = random.randint(10, screen_width - 100)
    food_y = random.randint(10, screen_height - 100)
    score = 0
    snake_size = 15
    fps = 35
    while not exit_game:
        if game_over:
            gameWindow.fill(white)
            text_screen("Game Over! Press Enter To Continue", red, 300, 300)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        gameloop(5)

        else:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        velocity_x = init_velocity
                        velocity_y = 0

                    if event.key == pygame.K_LEFT:
                        velocity_x = - init_velocity
                        velocity_y = 0

                    if event.key == pygame.K_UP:
                        velocity_y = - init_velocity
                        velocity_x = 0

                    if event.key == pygame.K_DOWN:
                        velocity_y = init_velocity
                        velocity_x = 0

            snake_x = snake_x + velocity_x
            snake_y = snake_y + velocity_y

            if abs(snake_x - food_x)<10 and abs(snake_y - food_y)<10:
                score +=1
                food_x = random.randint(20, screen_width - 100)
                food_y = random.randint(20, screen_height - 100)
                stone_x = random.randint(20, screen_width - 100)
                stone_y = random.randint(20, screen_height - 100)
                snk_length +=4
            if abs(snake_x - stone_x)<10 and abs(snake_y - stone_y)<10:
                game_over = True

            if score*10 == init_score:
                c=1
                count+=1
                init_score+=100
                init_velocity = init_velocity+1

            if score*10 == init_score-100 and c==1:
                r = random.choice(ch)
                c=0    
            if score>=0 and score<=9:   
                gameWindow.fill(white)
                text_screen(f"{count} Round", red, 415,1)     
            if score >= 10:
                gameWindow.fill(r)
                text_screen(f"{count} Round", red, 415,1)    
    
            text_screen("Score: " + str(score * 10), red, 1, 1)
            pygame.draw.rect(gameWindow, red, [food_x, food_y, snake_size, snake_size])
            pygame.draw.rect(gameWindow, brown, [stone_x, stone_y, snake_size, snake_size])
            


            head = []
            head.append(snake_x)
            head.append(snake_y)
            snk_list.append(head)

            if len(snk_list)>snk_length:
                del snk_list[0]

            if head in snk_list[:-1]:
                game_over = True
            if snake_x<0:
                snake_x = screen_width
            if snake_x>screen_width:
                snake_x = 0
            if snake_y<0:
                snake_y = screen_height
            if snake_y>screen_height:
                snake_y = 0        

            plot_snake(gameWindow, black, snk_list, snake_size)
        pygame.display.update()
        clock.tick(fps)

    pygame.quit()
    quit()
gameloop(5)