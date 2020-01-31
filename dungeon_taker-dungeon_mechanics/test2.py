import pygame

import character
import enemy
import roomLib

import random



def main():
    # Initialize pygame
    pygame.init()

    ######################################################################
    #SETTINGS
    screenWidth = 800
    screenHeight = 600
    FPS = 30
    # timeDelay = 50 DEPRECATED





    #Creates window, and clock, sets Icon
    screen = pygame.display.set_mode((screenWidth, screenHeight ))
    pygame.display.set_caption("Dungeon Taker: OTA")
    icon = pygame.image.load('images/oubliette.png')
    pygame.display.set_icon(icon)
    clock = pygame.time.Clock()

    ######################################################################

    player = character.Character()

    running = True

    def drawHandling():
        #this function handles the drawing in layers
        #RGB VALUES
        screen.fill((0,0,0))
        # pDraw()
        floor_sprites.draw(screen)
        all_sprites.draw(screen)
        wall_sprites.draw(screen)
        collision_sprites.draw(screen)
        attack_sprites.draw(screen)


    # def spawn_handling():
    #     if player.attack == True:
    #         print("spawn thing now")
    #         attack = character.Player_Attack(player.direction, player, 10)
    #         all_sprites.add(attack)
    #         player.attack = False
    #         return(attack)

    # sprite groups! <3 
    floor_sprites = pygame.sprite.Group()
    wall_sprites = pygame.sprite.Group()
    attack_sprites = pygame.sprite.Group()
    all_sprites = pygame.sprite.Group()
    collision_sprites = pygame.sprite.Group()
    enemy_sprites = pygame.sprite.Group()
    all_sprites.add(player)
    #get a list of sprites with built in location information

    dungeonTiles = roomLib.drawTestRoom()
    for tile in dungeonTiles:
        if tile.tile_type == 1:
            floor_sprites.add(tile)
        if tile.tile_type == 0:
            wall_sprites.add(tile)

# Sad cyril attempt at populating world with enemies.
# I guess I wasn't cut out for populating the world. OUCH!
    # def populate_with_enemies():
    #     testRoom = roomLib.testRoom
    #     for y in range(1, (len(testRoom)) - 1, 1):
    #         for x in range(1, (len(testRoom[y])) - 1, 1):
    #             print("this is x", x)
    #             print("this is y", y)
    #             if testRoom[y][x] == 1:
    #                 print("y,x = 1")
    #                 # if roomLib.searchTest(testRoom, x, y, 5, 5) == True:
    #                 # print("search returned true")
    #                 fly_y = (y*40) + 20
    #                 fly_x = (x*40) + 20
    #                 fly_holder = enemy.Fly(fly_y,fly_x)
    #                 print("fly created at,", x, ",", y)
    #                 return fly_holder
    # flyTest = populate_with_enemies()
    fly_list = []
    for i in range(0, 600, 1):
        y = ((random.randint(1,13))*40) + 20
        x = ((random.randint(1,18))*40) + 20
        fly_list.append(enemy.Fly(x,y))
        print("Made a new fly!")
    for fly in fly_list:
        enemy_sprites.add(fly)
        all_sprites.add(fly)
        colls = fly.coll_boxes
        for box in colls:
            collision_sprites.add(box)
    # roomLib.procRoomX()

    coll_boxes = player.coll_list
    for box in coll_boxes:
        collision_sprites.add(box)



    # testing fly collision

    # Loading area for rooms


    # A state machine for managing the main game loop



    while running:

        clock.tick(FPS)
        # pygame.time.delay(timeDelay) DEPRECATED

        #Update
        
        all_sprites.update()
        # attack = spawn_handling()
        if player.attack == True:
            # print("spawn thing now")
            attack = character.Player_Attack(player.direction, player, 10)
            attack_sprites.add(attack)
            # all_sprites.add(attack)
            player.attack = False
        attack_sprites.update()
        collision_sprites.update()
        wall_sprites.update()
        running = player.game_running
        

        hits = pygame.sprite.groupcollide(collision_sprites, wall_sprites, False, False)
        if player.top_box in hits:
            player.collide_up = True
        else: 
            player.collide_up = False
        if player.bottom_box in hits:
            player.collide_down = True
        else:
            player.collide_down = False
        if player.left_box in hits:
            player.collide_left = True
        else:
            player.collide_left = False
        if player.right_box in hits:
            player.collide_right = True
        else:
            player.collide_right = False

        # and now, for the fly object
        for fly in fly_list:
            if fly.top_box in hits:
                fly.go_up = False
            if fly.bottom_box in hits:
                fly.go_up = True
            if fly.left_box in hits:
                fly.go_left = False
            if fly.right_box in hits:
                fly.go_left = True


        ticks = pygame.sprite.groupcollide(enemy_sprites, attack_sprites, True, False)
        for fly in fly_list:
            if fly in ticks:
                
                print("YEEEEETT")
        if player in ticks:
            print("scored a hit")
        if ticks:
            print("the fly is hit!")
        # Draw / render
        drawHandling()

        pygame.display.flip()
    
    return ("END")