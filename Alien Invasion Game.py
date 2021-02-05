import pygame
import os
import time
import random
pygame.font.init()
os.chdir(r"C:\Users\Jwalant Modi")
WIDTH, HEIGHT = 800, 750
root = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Shooter")

# Load images
RED_SPACE_SHIP = pygame.image.load("1/pixel_ship_red_small.png")
GREEN_SPACE_SHIP = pygame.image.load("1/pixel_ship_green_small.png")
BLUE_SPACE_SHIP = pygame.image.load("1/pixel_ship_blue_small.png")

# Player player
YELLOW_SPACE_SHIP = pygame.image.load("1/pixel_ship_yellow.png")

# Lasers
RED_LASER = pygame.image.load("1/pixel_laser_red.png")
GREEN_LASER = pygame.image.load("1/pixel_laser_green.png")
BLUE_LASER = pygame.image.load("1/pixel_laser_blue.png")
YELLOW_LASER = pygame.image.load("1/pixel_laser_yellow.png")

# Background
BG = pygame.transform.scale(pygame.image.load("1/background-black.png"),(WIDTH,HEIGHT))
main_font = pygame.font.SysFont("Arial", 28)

class Laser:
    def __init__(self, x, y, img):
        self.x = x
        self.y = y
        self.img = img
        self.mask = pygame.mask.from_surface(self.img)

    def draw(self, window):
        window.blit(self.img, (self.x, self.y))

    def move(self, vel):
        self.y += vel

    def off_screen(self, height):
        return not(self.y <= height and self.y >= 0)

    def collision(self, obj):
        return collide(self, obj)

class Ship:
    COOLDOWN = 5
    def __init__(self, x, y, health=100):
        self.x = x
        self.y = y
        self.health = health
        self.ship_img = None
        self.laser_img = None
        self.lasers = []
        self.cool_down_counter = 0
    def draw(self, window):
        window.blit(self.ship_img, (self.x, self.y))
        for laser in self.lasers:
            laser.draw(window)

    def get_width(self):
        return self.ship_img.get_width()

    def get_height(self):
        return self.ship_img.get_height()

    def cooldown(self):
        if self.cool_down_counter>=self.COOLDOWN:
            self.cool_down_counter=0
        elif self.cool_down_counter > 0:
            self.cool_down_counter+=1

    def move_lasers(self, vel, obj):
        self.cooldown()
        for laser in self.lasers:
            laser.move(vel)
            if laser.off_screen(HEIGHT):
                self.lasers.remove(laser)
            elif laser.collision(obj):
                obj.health -= 10
                obj.score-=10
                self.lasers.remove(laser)                

    def shoot(self):
        if self.cool_down_counter == 0:
            laser = Laser(self.x, self.y, self.laser_img)
            self.lasers.append(laser)
            self.cool_down_counter=1

class Player(Ship):
    def __init__(self, x, y, health=100):
        super().__init__(x, y, health)
        self.ship_img = YELLOW_SPACE_SHIP
        self.laser_img = YELLOW_LASER
        self.mask = pygame.mask.from_surface(self.ship_img)
        self.max_health = health
        self.score = 0

    def move_lasers(self, vel, objs):
        self.cooldown()
        for laser in self.lasers:
            laser.move(vel)
            if laser.off_screen(HEIGHT):
                self.lasers.remove(laser)
            else:
                for obj in objs:
                    if laser.collision(obj):
                        objs.remove(obj)
                        self.score+=10
                        if laser in self.lasers:
                            self.lasers.remove(laser)
                      

class Enemy(Ship):
    color_map = {
        "red":(RED_SPACE_SHIP,RED_LASER),
        "blue":(BLUE_SPACE_SHIP, BLUE_LASER),
        "green":(GREEN_SPACE_SHIP, GREEN_LASER)
    }


    def __init__(self,x,y,color,health = 100):
        super().__init__(x,y, health)
        self.ship_img,self.laser_img = self.color_map[color]
        self.mask = pygame.mask.from_surface(self.ship_img)

    def move(self, vel):
        self.y+=vel

    def shoot(self):
        if self.cool_down_counter == 0:
            laser = Laser(self.x-25, self.y, self.laser_img)
            self.lasers.append(laser)
            self.cool_down_counter=1


def collide(obj1, obj2):
    offset_x = obj2.x - obj1.x
    offset_y = obj2.y - obj1.y
    return obj1.mask.overlap(obj2.mask, (offset_x, offset_y)) != None
def main():
    run = True
    fps = 35
    lives=5
    player_vel = 5
    enemies = []
    wave_length = 0
    enemy_vel = 1
    laser_vel = 15
    enemy_laser_vel = 8
    lost = False
    lost_font = pygame.font.SysFont("Arial", 50)
    lost_count=0
    player = Player(300,650)
    clock = pygame.time.Clock()

    def redraw_window():
        root.blit(BG,(0,0))
        lives_label = main_font.render(f"Lives: {lives}",1,(255,255,255)) 
        level_label = main_font.render(f"Score: {player.score}",1,(255,255,255)) 
        root.blit(lives_label, (10,10))
        root.blit(level_label, (WIDTH-level_label.get_width()-10,10))

        for enemy in enemies:
            enemy.draw(root)
        player.draw(root)

        if lost:
            root.blit(BG,(0,0))
            lost_label = lost_font.render(f"You Lost, Press Enter to Restart the Game", 1, (255,255,255))
            root.blit(lost_label, (WIDTH/2-int(lost_label.get_width())/2,350))
        
        pygame.display.update()
    while run:
        clock.tick(fps)
        redraw_window()  
        if lives<=0 or player.health<=0:
            # lives = 5
            lost = True
            lost_count+=1      
           
        if len(enemies)==0:
            wave_length+=8
            for i in range(wave_length):
                enemy = Enemy(random.randrange(50,WIDTH-100), random.randrange(-1000,-50), random.choice(["red","blue","green"]))
                enemies.append(enemy)



        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player.x-player_vel>0:
            player.x-=12
            
        elif keys[pygame.K_RIGHT] and player.x+player_vel<WIDTH-player.get_width():
            player.x+=12

        elif keys[pygame.K_RETURN]:
            run = False
            main()   

                 
       

        for enemy in enemies:
            enemy.move(enemy_vel)
            enemy.move_lasers(enemy_laser_vel, player)


            if random.randrange(0,85)==1:
                enemy.shoot()   
            if collide(enemy, player):
                lives-=1
                player.health-=10
                enemies.remove(enemy)     
            elif enemy.y+enemy.get_height()>HEIGHT:
                lives-=1
                enemies.remove(enemy)
        while random.randrange(0,2)==1:
            player.shoot()        

        player.move_lasers(-laser_vel, enemies) 

                      
main()

