import pygame
import random
import time
import os
os.chdir(r"C:\Users\Jwalant Modi")
pygame.init()
red = (255,0,0)
gray = (119,118,119)
width = 800
height = 700
fps = 35
root = pygame.display.set_mode((width,height))
pygame.display.set_caption("Racing Game")
black = (0,0,0)
clock = pygame.time.Clock()
car_img = pygame.image.load("1/car5.jpg")
backgroundpic = pygame.image.load("1/grass.jpg")
yellow_strip = pygame.image.load("1/yellow strip.jpg")
strip = pygame.image.load("1/strip.jpg")
car_width = 56

def background():
    pass
    # root.blit(backgroundpic,(0,0))
    # root.blit(backgroundpic,(0,200))
    # root.blit(backgroundpic,(0,400))
    # root.blit(backgroundpic,(700,0))
    # root.blit(backgroundpic,(700,200))
    # root.blit(backgroundpic,(700,0))
    # root.blit(yellow_strip,(400,0))
    # root.blit(yellow_strip,(400,100))
    # root.blit(yellow_strip,(400,200))
    # root.blit(yellow_strip,(400,300))
    # root.blit(yellow_strip,(400,400))
    # root.blit(yellow_strip,(400,500))
    # root.blit(yellow_strip,(400,600))
    # root.blit(yellow_strip,(400,700))
    # root.blit(strip,(120,0))
    # root.blit(strip,(120,100))
    # root.blit(strip,(120,200))
    # root.blit(strip,(680,0))
    # root.blit(strip,(680,100))
    # root.blit(strip,(680,200))
main_font = pygame.font.SysFont("", 50)
score_font = pygame.font.SysFont("", 50)
l = ["1/car1.jpg","1/car2.jpg", "1/car3.jpg", "1/car4.jpg", "1/car7.jpg"]
def obstacle(obs_start_x, obs_start_y, obs):
    obs_img = pygame.image.load(l[obs])
    root.blit(obs_img, (obs_start_x, obs_start_y))
def obstacle1(obs_start_x, obs_start_y, obs):
    obs_img = pygame.image.load(l[obs])
    root.blit(obs_img, (obs_start_x, obs_start_y))       
def text_mes(s):
    label = main_font.render(s,1, red)
    root.blit(label, (325,350))
    pygame.display.update()
    time.sleep(3)
    main()

def scored(score):
    score_label = score_font.render(f"Score: {score}", 1, black)
    root.blit(score_label,(105,10))
      
def crashed():
    text_mes("You Crashed!")
  
def car(x,y):
    root.blit(car_img,(x,y))
def main():
    global height
    run = True
    x_change=0
    car_x = 375
    car_y = height-150
    obs = 0
    obs_speed = 15
    obs_start_x = random.randrange(150, width-150)
    obs_start_y = random.randrange(-700, -100)
    obs_width = 56
    obs_height = 110
    car_height = 110
    y2 = 7
    score = 0
    obs1 = obs
    old_x = obs_start_x
    old_y = obs_start_y
    
    while run:
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                quit()
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change=-12
                    
                if event.key == pygame.K_RIGHT:
                    x_change=12
                    

                if event.key == pygame.K_RETURN:
                    run = False
                    main()
                        

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_UP or event.key == pygame.K_DOWN:        
                    x_change = 0           

        car_x +=x_change
        root.fill(gray)
        rel_y = y2%backgroundpic.get_rect().width
        if rel_y < height:
            # pass
            root.blit(backgroundpic, (0,rel_y-backgroundpic.get_rect().width))
            root.blit(backgroundpic, (700,rel_y-backgroundpic.get_rect().width))
            root.blit(yellow_strip,(400,rel_y-100))
            root.blit(yellow_strip,(400,rel_y))
            root.blit(yellow_strip,(400,rel_y+100))
            root.blit(yellow_strip,(400,rel_y+200))
            root.blit(yellow_strip,(400,rel_y+300))
            root.blit(yellow_strip,(400,rel_y+400))
            root.blit(yellow_strip,(400,rel_y+500))
            root.blit(yellow_strip,(400,rel_y+600))
            root.blit(yellow_strip,(400,rel_y+700))
            root.blit(strip,(120,rel_y-100))
            root.blit(strip,(680,rel_y-100))
        y2+=obs_speed    
        background()
        car(car_x, car_y)
        obstacle(obs_start_x, obs_start_y, obs)
        obstacle1(old_x, old_y, obs1)
        obs_start_y = obs_start_y+obs_speed
        old_y = old_y+obs_speed
        no = random.choice([-50,50])
        c=random.randrange(1, 100)
        if obs_start_y > height-300:
            if c%2==0:
                obs1,old_x, old_y = obs, obs_start_x+no, obs_start_y
            else:
                obs1,old_x, old_y = obs, obs_start_x, obs_start_y    
            obs = random.randint(0,4)
            obs_start_x = random.randrange(180, width-180)
            obs_start_y = random.randrange(-50, -10)
            c=random.randrange(1, 100)

        if car_x > width-112-car_width or car_x < 100:
            crashed()

        if car_y < old_y+car_height:    
            # if car_x > obs_start_x and car_x < obs_start_x + obs_width or car_x + obs_width > obs_start_x and car_x < obs_start_x:
            #     crashed()
            if car_x > old_x and car_x < old_x + obs_width or car_x + obs_width > old_x and car_x < old_x:
                crashed()    
                 
        if old_y> car_y+car_height+50:
            score+=10
            scored(score)
            pygame.display.update()
            # score_label = score_font.render(f"Score: {score}", 1, black)
            # root.blit(score_label,(500,350))
            # pygame.display.update()    
        scored(score)
        clock.tick(fps)
main() 