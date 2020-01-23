import pygame

# define colors
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)


class Collision_Box(pygame.sprite.Sprite):
    def __init__(self, parent, pos, shape):
        pygame.sprite.Sprite.__init__(self)
        if shape == 'vert':
            self.image = pygame.Surface((8, 24))
        if shape == 'lat':
            self.image = pygame.Surface((24, 8))
        # Setting color for testing.
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.pos = pos
        self.rect.center = self.pos
        self.parent = parent
        


    def update(self):
        self.rect.x = self.parent.rect.x + self.pos[0]
        self.rect.y = self.parent.rect.y + self.pos[1]

# class Collision_Group(pygame.sprite.Sprite):
#     def __init__(self, parent, offset):




class Player_Attack(pygame.sprite.Sprite):
    def __init__(self, direction, origin, offset = 5):
        pygame.sprite.Sprite.__init__(self)
        if direction == 'UP' or direction == 'DOWN':
            self.image = pygame.Surface((32,8))
        if direction == 'LEFT' or direction == 'RIGHT':
            self.image = pygame.Surface((8,32))
        self.image.fill(RED)
        self.rect = self.image.get_rect()

        self.lifetime_frames = 7

        if direction == 'UP':
            target = (origin.rect.midtop[0], origin.rect.midtop[1] - offset)
            self.rect.center = target
        if direction == 'DOWN':
            target = (origin.rect.midbottom[0], origin.rect.midbottom[1] + offset)
            self.rect.center = target
        if direction == 'LEFT':
            target = (origin.rect.midleft[0] - offset, origin.rect.midleft[1] )
            self.rect.center = target
        if direction == 'RIGHT':
            target = (origin.rect.midright[0] + offset, origin.rect.midright[1])
            self.rect.center = target
            # self.rect.center[0] += offset

        self.game_running = True

    def update(self):
        self.lifetime_frames -= 1
        if self.lifetime_frames < 1:
            self.kill()

        # self.rect.center = 

class Character(pygame.sprite.Sprite):
    def __init__(self, xPos = 370, yPos = 480, speed = 3, attack = 1, health = 10):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((32,32))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.center = (xPos, yPos)
        self.xPos = xPos
        self.yPos = yPos
        self.speed = speed
        self.attack = attack
        self.health = health
        
        self.direction = 'UP'
        self.upTrigger = False
        self.downTrigger = False
        self.rightTrigger = False
        self.leftTrigger = False
        self.attack = False
        
        ######## Set collision boxes
        self.top_box = Collision_Box(self, (4, 2), shape = 'lat')
        self.bottom_box = Collision_Box(self, (4, 22), shape = 'lat')
        self.left_box = Collision_Box(self, (2,4), shape = 'vert')
        self.right_box = Collision_Box(self, (22,4), shape = 'vert')


        # all directional colliders to be added to groups.
        self.coll_list = [self.top_box, self.bottom_box, self.left_box, self.right_box]
        # This is the trigger to end the game
        self.game_running = True

    def update(self):
        self.movement()
        self.inputHandler()
        pass

    def movement(self):
        if self.upTrigger:
            self.direction = 'UP'
            self.yPos -= self.speed

        if self.downTrigger:
            self.direction = 'DOWN'
            self.yPos += self.speed

        if self.leftTrigger:
            self.direction = 'LEFT'
            self.xPos -= self.speed

        if self.rightTrigger:
            self.direction = 'RIGHT'
            self.xPos += self.speed
        self.rect.center = (self.xPos, self.yPos)

    def inputHandler(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.leftTrigger = True
                if event.key == pygame.K_RIGHT:
                    self.rightTrigger = True
                if event.key == pygame.K_UP:
                    self.upTrigger = True
                if event.key == pygame.K_DOWN:
                    self.downTrigger = True
                # Now handling attack input
                if event.key == pygame.K_SPACE:
                    self.attack = True
                    print("Attack key pressed")
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    self.leftTrigger = False
                if event.key == pygame.K_RIGHT:
                    self.rightTrigger = False
                if event.key == pygame.K_UP:
                    self.upTrigger = False
                if event.key == pygame.K_DOWN:
                    self.downTrigger = False

            if event.type == pygame.QUIT:
                print("I clicked quit")
                self.game_running = False
            else: self.game_running = True
        
    