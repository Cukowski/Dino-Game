import random
import pygame
from pygame.locals import *
import time

pygame.init()
pygame.mixer.init()

class Dino():
    def __init__(self):

        self.Img = pygame.image.load("dino_.png") # it's just waiting
        self.WIDTH, self.HEIGHT = 44 ,48

        self.Img = pygame.transform.scale(self.Img, (self.WIDTH, self.HEIGHT))

        self.image = self.Img

        self.x = 20
        self.y = 170

        # make gravity for jumping
        self.g = -0.25
        self.up = 7
        self.t = 0 #time
        
        self.hitbox = pygame.Rect(self.x + 5, self.y, self.WIDTH - 15, self.HEIGHT - 5) # tested for collision

        # run animation
        self.runImg1 = pygame.image.load("assets/dino_1.png")
        self.runImg2 = pygame.image.load("assets/dino_2.png")
        self.runImg1 = pygame.transform.scale(self.runImg1, (self.WIDTH, self.HEIGHT)) # overrideing
        self.runImg2 = pygame.transform.scale(self.runImg2, (self.WIDTH, self.HEIGHT))

        # duck animation for ptera coming (we can jump or duck)
        self.duck1 = pygame.image.load("assets/dino_ducking1.png")
        self.duck2 = pygame.image.load("assets/dino_ducking2.png")

        self.duck1 = pygame.transform.scale(self.duck1, (self.WIDTH + 15, self.HEIGHT)) # beacuse when it ducks it gets longer
        self.duck2 = pygame.transform.scale(self.duck2, (self.WIDTH + 15, self.HEIGHT)) # beacuse when it ducks it gets longer

        self.is_ducking = False

        # dino
        self.duckImgs = [self.duck1, self.duck2]
        self.runImgs = [self.runImg1, self.runImg2]

        #sound for jumping
        self.jump_sound = pygame.mixer.Sound("assets/jump_sound.wav")
        self.count = 0

        self.jumping = False # it will be on ground and jump only pressed

    def jump(self):

        # jumping is y axis to upper
        self.y -= self.up # when jump y decreases upward
        
        self.jumping = True # user pressed jump

        self.jump_sound.play() # toi play the audio file

    def update(self):
        # only update when it's jumping (170 to up)

        if self.y < 170: # check if jumping or not. Make gravity pyhischcs
            self.up  = self.up + self.g * self.t # v = g * t hız = ivme * zaman newton fisrt law
            self.y -= self.up
            self.t += 0.12

        if self.y > 170: # check if jump is complete and reset all vars
            self.y = 170
            self.t = 0
            self.up = 7
            self.jumping = False

        if self.is_ducking:

            self.hitbox = pygame.Rect(self.x+5 , self.y+20, self.WIDTH + 12, self.HEIGHT - 20) # it's ducking so height is lower

            self.image = self.duckImgs[int(self.count)%2] # for 2 ducking images
            self.count += 0.2
        elif self.jumping:
            self.hitbox = pygame.Rect(self.x+5, self.y, self.WIDTH-15, self.HEIGHT - 5) # hitbox also needs to jump and reset
            self.image = self.Img
        else:
            self.hitbox = pygame.Rect(self.x+5, self.y, self.WIDTH - 17, self.HEIGHT - 5)
            self.image = self.runImgs[int(self.count)%2] # for 2 ducking images
            self.count += 0.15

    def draw(self, screen):

        screen.blit(self.image, (self.x, self.y))
        pygame.draw.rect(screen, (255, 0 , 0), self.hitbox, 2) # draw the hitbox, give it red color, give it 2px thickness

class Cactus():
    def __init__(self):
        self.image0 = pygame.image.load("assets/cacti-small.png")
        self.image1 = pygame.image.load("assets/cacti-big.png")
        # same height but dif width
        self.width0 = 45
        self.height = 45
        self.width1 = 65

        # scale to the size
        self.image0 = pygame.transform.scale(self.image0, (self.width0, self.height))
        self.image1 = pygame.transform.scale(self.image1, (self.width1, self.height))

        # we want cactuses appare immediately, ptera should start later
        self.is_cactus = True
        self.is_ptera = False

        # we want cactueses appear randomly, we make a list inside of random choice
        self.image, self.width = random.choice([[self.image0, self.width0], [self.image1, self.width1]])

        self.x = random.randint(720, 1000) # appear along x axis
        self.y = 175 # appear along x axis
        self.speed = 4 # same size as ground

        #check collision, so make a box out of cactus
        self.hitbox = pygame.Rect(self.x, self.y, self.width, self.height)

    #
    def update(self):
        self.x-=self.speed # move left on x axis
        self.hitbox = pygame.Rect(self.x, self.y, self.width, self.height) # move with cactus

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y)) # image we want to siplay in the loaction we want to dispaly

# make a ptrea and make it flap
class Ptera():
    def __init__(self):
        self.width, self.height = 50, 40
        self.im1 = pygame.image.load("assets/ptera1.png")
        self.im2 = pygame.image.load("assets/ptera2.png")

        self.im1 = pygame.transform.scale(self.im1, (self.width, self.height))
        self.im2 = pygame.transform.scale(self.im2, (self.width, self.height))

        self.flaps = [self.im1, self.im2]

        # flying x axis 
        self.altitudes = [175, 150, 110]
        self.x = random.randint(750, 1000)
        self.y = random.choice(self.altitudes)

        self.speed = 5 # ground is 4, ptera is faster
        self.count = 0 #
        self.is_ptera = True # when it's called, it'll move from that moment
        self.is_cactus = False # they won't appear at the same time

        self.hitbox = (self.x, self.y+10, self.width, self.height -12) # it can appeaar a little hiugher
        
    def update(self):
        self.image = self.flaps(int(self.count)%2) # modulus
        self.count += 0.1 # make im1 and im2 change turns to make it flap

        self.x-=self.speed # moves to left

        if self.x < 50: # ptera has reached almost x axis, we can have a new ptera
            self.allowed = True
            
        self.hitbox = pygame.Rect(self.x, self.y+10, self.width, self.height - 10)

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))
        # we'll draw it later
        # pygame.draw.rect(screen, (255, 0, 0), self.hitbox, 2) # draw it on screen and give color red




class Ground():

    def __init__(self):
        self.ground_length = 1201
        self.ground1 = pygame.image.load("assets/ground.png")
        self.ground1_x = 0
        self.ground1_y = 200
        
        self.ground2 = pygame.image.load("assets/ground.png")
        self.ground2_x = self.ground1_x + self.ground_length
        self.ground2_y = self.ground1_y

        self.speed = 4

    def draw(self, screen):
        screen.blit(self.ground1, (self.ground1_x, self.ground1_y))
        screen.blit(self.ground2, (self.ground2_x, self.ground2_y))

    def update(self):
        self.ground1_x -= self.speed
        self.ground2_x -= self.speed

        if self.ground1_x + self.ground_length < 0:
            self.ground1_x = self.ground2_x + self.ground_length
        elif self.ground2_x + self.ground_length < 0:
            self.ground2_x = self.ground1_x + self.ground_length

class Cloud():
    def __init__(self): #constructor method
        self.image = pygame.image.load("assets/cloud.png")
        self.WIDTH, self.HEIGHT = 70, 40
        # transfrom image to the desired size
        self.image = pygame.transform.scale(self.image, (self.WIDTH, self.HEIGHT))

        # speed of cloud is les than the ground
        self.speed = 1
        self.x = 600
        self.y = 50

    def update(self):
        self.x-=self.speed # moves to left size -

        if self.x<-self.WIDTH: #if the cloud is out of screen
            self.x = 600 
            self.y = random.randint(10, 100) # cloud will appear in random this values

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))




def game():
    screen = pygame.display.set_mode((750, 250))
    clock = pygame.time.Clock()

    # font

    check_point = pygame.mixer.Sound("assets/checkPoint.wav")
    death_sound = pygame.mixer.Sound("assets/die.wav")

    dino_icon = pygame.image.load("assets/dino.png")
    pygame.display.set_icon(dino_icon)

    pygame.display.set_caption("Dino Run")

    game_over = pygame.image.load("assets/game_over.png")
    replay_button = pygame.image.load("assets/replay_button.png")
    logo = pygame.image.load("assets/logo.png")

    GREY = (240, 240, 240)

    ground = Ground()
    ground.draw(screen)
    ground.update()

    # after devlaring go make the class Cloud
    cloud = Cloud()
    cloud.draw(screen)
    cloud.update()

    #creat instance of the class as list
    obstacles = [Cactus()]

    #creat instance of the class
    dino = Dino()

    pygame.display.update()


running = True
while(running):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            running = False

    game()