import pygame

import character
import enemy
import roomLib
# Cyril added random import
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
        bullet_sprites.draw(screen)


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
    bullet_sprites = pygame.sprite.Group()
    all_sprites.add(player)
    #get a list of sprites with built in location information


    bossTest = enemy.Lord_of_Flies()
    enemy_sprites.add(bossTest)
    all_sprites.add(bossTest)
    # roomLib.procRoomX()   # ||||||||||||||||||||||||||||||||||||||||
    dungeonTiles = roomLib.drawTestRoom()
    for tile in dungeonTiles:
        if tile.tile_type == 1:
            floor_sprites.add(tile)
        if tile.tile_type == 0:

            wall_sprites.add(tile)

    coll_boxes = player.coll_list
    for box in coll_boxes:
        collision_sprites.add(box)



###############Running Loop!###############Running Loop!###############Running Loop!###############Running Loop!###############
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
        bullet_sprites.update()
        running = player.game_running

# creates a bulet ||||||||||||||||| creates a bullet |||||||||||||||| creates a bullet |||||||||||||||||||||
        new_bullet = bossTest.shoot(player)
        if new_bullet != None:
            print("made bullet")
            bullet_sprites.add(new_bullet)
            all_sprites.add(new_bullet)
            enemy_sprites.add(new_bullet)

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




        ticks = pygame.sprite.groupcollide(enemy_sprites, attack_sprites, True, False)


        if player in ticks:
            print("scored a hit")
        if ticks:
            print("the fly is hit!")
        # Draw / render
        drawHandling()

        pygame.display.flip()
    
    return ("INTRO")