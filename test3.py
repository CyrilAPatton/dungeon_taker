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

    chaser_list = []
    testRoom = roomLib.testRoom
    while len(chaser_list) < 1:
        y = (random.randint(1,13))
        x = (random.randint(1,18))
        if testRoom[y][x] == 1:
            chaser_list.append(enemy.Basic_Chaser((x*40) + 20,(y*40) + 20))
            print("Made a new fly!")
    for chaser in chaser_list:
        enemy_sprites.add(chaser)
        all_sprites.add(chaser)
        colls_chaser = chaser.coll_boxes
        for box in colls_chaser:
            collision_sprites.add(box)

    bossTest = enemy.Lord_of_Flies()
    flyTest = enemy.Fly()
    enemy_sprites.add(flyTest)
    enemy_sprites.add(bossTest)
    all_sprites.add(flyTest)
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

    colls = flyTest.coll_boxes
    for box in colls:
        collision_sprites.add(box)

    colls = bossTest.coll_boxes
    for box in colls:
        collision_sprites.add(box)


    # testing fly collision

    # Loading area for rooms


    # A state machine for managing the main game loop


    # Generating 6 enemy "chasers" in empty floor tiles throughout the room.
    # chaser_list = []


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

        for chaser in chaser_list:
            if chaser.top_box in hits and chaser.left_box in hits and chaser.right_box in hits and chaser.bottom_box in hits:
                chaser.left_box.kill()
                chaser.right_box.kill()
                chaser.top_box.kill()
                chaser.bottom_box.kill()
                chaser.kill()

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

        # and now for the chaser object
        for chaser in chaser_list:
            if chaser.top_box in hits:
                chaser.go_up = False
            else:
                chaser.go_up = True

            if chaser.bottom_box in hits:
                chaser.go_down = False
            else:
                chaser.go_down = True

            if chaser.left_box in hits:
                chaser.go_left = False
            else:
                chaser.go_left = True

            if chaser.right_box in hits:
                chaser.go_right = False
            else:
                chaser.go_right = True


        # and now, for the fly object

        if flyTest.top_box in hits:
            flyTest.go_up = False
            # Cyril added random direction and angle
            x = random.randint(1,2)
            if x == 1:
                flyTest.go_left = True
            else: 
                flyTest.go_left = False
            k = random.randint(1,4)
            if k == 1:
                flyTest.vert_angle = True
                flyTest.lat_angle = False
            elif k == 2:
                flyTest.vert_angle = False
                flyTest.lat_angle = True
            else:
                flyTest.vert_angle = True
                flyTest.lat_angle = True



        if flyTest.bottom_box in hits:
            flyTest.go_up = True
            # Cyril added random direction and angle
            x = random.randint(1,2)
            if x == 1:
                flyTest.go_left = True
            else: 
                flyTest.go_left = False
            k = random.randint(1,4)
            if k == 1:
                flyTest.vert_angle = True
                flyTest.lat_angle = False
            elif k == 2:
                flyTest.vert_angle = False
                flyTest.lat_angle = True
            else:
                flyTest.vert_angle = True
                flyTest.lat_angle = True


        if flyTest.left_box in hits:
            flyTest.go_left = False
            # Cyril added random direction and angle
            x = random.randint(1,2)
            if x == 1:
                flyTest.go_up = True
            else: 
                flyTest.go_up = False
            k = random.randint(1,4)
            if k == 1:
                flyTest.vert_angle = True
                flyTest.lat_angle = False
            elif k == 2:
                flyTest.vert_angle = False
                flyTest.lat_angle = True
            else:
                flyTest.vert_angle = True
                flyTest.lat_angle = True


        if flyTest.right_box in hits:
            flyTest.go_left = True
            # Cyril added random direction and angle
            x = random.randint(1,2)
            if x == 1:
                flyTest.go_up = True
            else: 
                flyTest.go_up = False
            k = random.randint(1,4)
            if k == 1:
                flyTest.vert_angle = True
                flyTest.lat_angle = False
            elif k == 2:
                flyTest.vert_angle = False
                flyTest.lat_angle = True
            else:
                flyTest.vert_angle = True
                flyTest.lat_angle = True

        for chaser in chaser_list:
            chaser.update_basic_chaser(player)







        ticks = pygame.sprite.groupcollide(enemy_sprites, attack_sprites, True, False)
        if flyTest in ticks:
            print("YEEEEETT")
        for chaser in chaser_list:
            if chaser in ticks:
                chaser.left_box.kill()
                chaser.right_box.kill()
                chaser.top_box.kill()
                chaser.bottom_box.kill()
                chaser.kill()
                print("You killed a chaser lol!")
        if player in ticks:
            print("scored a hit")
        if ticks:
            print("the fly is hit!")
        # Draw / render
        drawHandling()

        pygame.display.flip()
    
    return ("INTRO")