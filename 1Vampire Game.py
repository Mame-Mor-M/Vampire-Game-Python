#Mame Mor Mbacke
#May 28th 2019
#A vampire hunt game where the player has to hunt humans to stay alive
#Pygame Setup-----------------
import pygame
from random import randint
pygame.init()
def main(): #A function that holds the game, I can call this when I want to re-run the code
    WIDTH = 1200 #Make the width of the game window 1366
    HEIGHT = 700 #Make the height of the game window 768
    gameWindow = pygame.display.set_mode((WIDTH,HEIGHT)) #Define the game window with the Width and Height
    #Pygame Setup-----------------

    #Color Setup------------------
    BLACK = (0,0,0)
    WHITE = (255,255,255)
    RED = (255,0,0)
    sun_COLOR = (255,255,0)
    GROUND_COLOR = (0,255,0)
    DAY_COLOR = (136,206,250)
    SUNSET_COLOR = (0,0,200)
    BROWN = (165,42,42)
    BLUE = (0,0,255)
    #Color Setup------------------

    #Font Text------------------
    font = pygame.font.SysFont("Segoe Print",36)#Defines a font and a font size
    font2 = pygame.font.SysFont("Sans Serif",24)
    #Font Text------------------
    
    #Position Setup--------
    playerX = WIDTH/5 #The X position of the player is equal to the centerpoint of the screen
    playerY = HEIGHT/2 #The Y position of the player is equal to the centerpoint of the screen
    playerW = 10#The width of the player
    playerH = 60#The height of the player
    sunX = WIDTH-1600#The X position of the sun
    sunY = HEIGHT-HEIGHT #The Y position of the sun
    moonX = WIDTH-1600 #The X position of the moon
    moonY = HEIGHT-HEIGHT + 70 #The Y position of the moon
    healthX = 980 #The X position of the first health icon
    healthY = HEIGHT-600# The Y position of the first health icon
    health2X = 1060
    health2Y = HEIGHT-600
    health3X = 1140
    health3Y = HEIGHT-600
    treeX = 100
    treeY = 100
    tree2X = 1005
    tree2Y = 240
    tree3X = 10
    tree3Y = 260
    tree4X = 120
    tree4Y = 430
    tree5X = 780
    tree5Y = 430
    tree7X = 490
    tree7Y = 230
    tentX = 700
    tentY = HEIGHT-550
    tent2X = 1010
    tent2Y  = HEIGHT-550
    humanSpeedX = 5 #The speed of the first human on the X axis
    humanSpeedY = 5 #The speed of the first human on the Y axis
    human2SpeedX = -5
    human2SpeedY = 5
    human3SpeedX = 8
    human3SpeedY = 5
    humanX = -20 
    humanY = 500
    human2X = 1000
    human2Y = 550
    human3X = -20
    human3Y = 560
    hunterSpeedX = 6#The speed of the first hunter on the X axis
    hunterSpeedY = 7#The speed of the first hunter on the Y axis
    hunterX = -20
    hunterY = 500
    health = 4 #The amount of health the player starts with. It starts at 4 but it shows three health bars, this is for easier coding
    #Position Setup--------
    
    nightsSurvived = 0 #The players score, the amount of nights they have survived
    day = False #A boolean defining day as false
    night = True #A boolean defining night as true, the game will start at night time.
    pygame.display.update() #Update the code.
    inPlay = False #A boolean defining whether or not the game is being played, starts as false.
    instructions = False #The screen that tells you how the game works
    animation_counter = 0   
    #Player Images-----------------------------------------------
    playerStand = pygame.image.load("Vampire Standing.png")#Load the image of a vampire standing
    playerStandLeft = pygame.image.load("Vampire StandingLeft.png")
    playerRight = pygame.image.load("Vampire Right.png")
    playerLeft = pygame.image.load("Vampire Left.png")
    playerUpRight = pygame.image.load("Vampire UpRight.png")
    playerDown = pygame.image.load("Vampire Down.png")
    playerDownLeft = pygame.image.load("Vampire Down Left.png")
    playerUpLeft = pygame.image.load("Vampire UpLeft.png")
    playerUp = pygame.image.load("Vampire Up.png")
    playerDeath = pygame.image.load("Start Dying.png")
    playerDeath2 = pygame.image.load("Dying 2.png")
    playerDeath3 = pygame.image.load("Dying 3.png")
    playerDeath4 = pygame.image.load("Dying 4.png")
    playerDeath5 = pygame.image.load("Dying 5.png")
    playerDeath6 = pygame.image.load("Dying 6.png")
    playerDeath7 = pygame.image.load("Dying 7.png")
    playerDeath9 = pygame.image.load("Dying 9.png")
    playerDeath10 = pygame.image.load("Dying 10.png")
    playerDeath11 = pygame.image.load("Dying 11.png")
    player = playerStand
    #Player Images-----------------------------------------------

    #hunter and human Images-----------------------------------------------
    hunterStand = pygame.image.load("hunter Standing.png")
    hunterRight = pygame.image.load("hunter Right.png")
    hunterRight = pygame.transform.scale(hunterRight,(60,60))
    hunterLeft = pygame.image.load("hunter Left.png")
    hunterLeft = pygame.transform.scale(hunterLeft,(60,80))
    humanRight = pygame.image.load("human Right.png")
    humanRight = pygame.transform.scale(humanRight,(50,60))
    humanLeft = pygame.image.load("human Left.png")
    humanLeft = pygame.transform.scale(humanLeft,(50,60))
    #hunter and human Images-----------------------------------------------

    #Environment Images------------------------------------------
    sun = pygame.image.load("sun.png")
    sun = pygame.transform.scale(sun,(400,400))
    moon = pygame.image.load("moon.png")
    moon = pygame.transform.scale(moon,(250,250))
    #Environment Images------------------------------------------

    music = pygame.mixer.music.load('Vampire Music.mp3')# Loads music file
    pygame.mixer.music.play(-1) #Plays music indefinately
    pygame.mixer.music.set_volume(0.3) #Sets the volume for the music
    Heart = pygame.image.load("Heart.png")
    moving = False #Whether or not the player is moving
    RIGHT = False#Whether or not the player is going right
    LEFT = False#Whether or not the player is going left
    UP = False#Whether or not the player is going up
    DOWN = False#Whether or not the player is going DOWN
    
    #Start screen-------------------------------------------
    while not inPlay and instructions == False: 
        gameWindow.fill(RED)
        gameName = font.render(("VAMPIRE SURVIVAL"),1,BLACK) #Displays text that says "Vampire Survival"
        gameWindow.blit(gameName,(400,200))
        gameName = font2.render(("PRESS SPACEBAR TO CONTINUE"),1,BLACK) #Displays text that says "Vampire Survival"
        gameWindow.blit(gameName,(460,300))
        vampireGif = pygame.image.load("Vampire.gif")
        gameWindow.blit(vampireGif,(410,400)) #Displays the image under the variable 'vampireGif'
        pygame.event.get()
        keys = pygame.key.get_pressed() #Gives the variable keys every entry on the keyboard
        quitting = font2.render(("Press ESC to exit the game"),1,BLACK)
        gameWindow.blit(quitting,(980,670))
        if keys[pygame.K_SPACE]: #If the space key is pressed the game will start
            instructions = True
            clang = pygame.mixer.Sound('Clang.wav') #Loads a sound effect that will play when the player hits spacebar
            clang.play() #plays the sound effect
        if keys[pygame.K_ESCAPE]:
            pygame.quit()
    #Start screen-------------------------------------------  
        pygame.display.update()
    
    while not inPlay and instructions == True: #Displays the instructions of the game
        gameWindow.fill(RED)
        instructionScreen = pygame.image.load("Instructions.png")
        gameWindow.blit(instructionScreen,(0,0))
        pygame.event.get()
        keys = pygame.key.get_pressed()
        quitting = font2.render(("Press ESC to exit the game"),1,BLACK)
        gameWindow.blit(quitting,(980,670))
        if keys[pygame.K_RETURN]:
            instructions = False
            inPlay = True
            clang = pygame.mixer.Sound('Clang.wav')
            clang.play()
        if keys[pygame.K_ESCAPE]:
            pygame.quit()
        pygame.display.update()
    #Main game------------------------------------------------------
    while inPlay and instructions == False:
        gameWindow.fill(DAY_COLOR)
    #Day/Night Cycle-----------------------------------------------------------
        #Day Time----------------------------------------------------------------
        if day == True and night == False: #During the day
            sunX += 10 #sun moves 10 pixels per 10 miliseconds horizontally
            humanY = 300#Make the human appear on the screen by setting its Y position
            human2Y = 540
            human3Y = 400
            if humanX <= -40: #If the human is not on the screen they are 'dead'
                humanX = -20 #Change their X position to -20 pixels
                humanSpeedX = 0 #Reduce the human's speed so that they do not move
            if human2X <= -40:
                human2X = 1200
                human2SpeedX = 0
            if human3X <= -40:
                human3X = -20
                human3SpeedX = 0
            hunterY = -3400 #Move the hunter off of the screen.
            
            #Player loses all of their health if they are not colliding with one of these objects
            if not playerRect.colliderect(tree1Rect) and not playerRect.colliderect(tree2Rect) and not playerRect.colliderect(tree3Rect) and not playerRect.colliderect(tree4Rect) and not playerRect.colliderect(tree5Rect) and not playerRect.colliderect(tree7Rect) and not playerRect.colliderect(tentRect) and not playerRect.colliderect(tent2Rect):
                health=0 #Remove all of the players health
            if sunX >= WIDTH/2:#When the sun reaches the halfway point of the screen, it will become evening.
                SUNSET = pygame.draw.rect(gameWindow,SUNSET_COLOR,(0,0,WIDTH,HEIGHT-350)) #Draw a new image as the sky
            if sunX == WIDTH: #When the sun reaches the end of the screen
                sunX = WIDTH-1600#Move the sun back to the left side of the screen
                nightsSurvived += 1 #Add a number the the amount of nights the player has survived
                health-=1 #Reduce the players health by one
                hunterSpeedX = 6 #Increase the hunter's speed to 6 so that it starts moving when it is night
                day = False #It is no longer daytime
                night = True #It is night time
            gameWindow.blit(sun,(sunX,sunY))
        #Day Time----------------------------------------------------------------

        #Night Time----------------------------------------------------------------    
        if night == True and day == False: #During the night
            night_sky = pygame.draw.rect(gameWindow,BLACK,(0,0,WIDTH,HEIGHT-350)) #Draw a new image as the sky
            gameWindow.blit(moon,(moonX,moonY)) #Display the moon image
            moonX+= 10 
            hunterY = 300
            if human2X <= -40:
                human2X = 1200
                human2SpeedX = 0
            if human3X <= -40:
                human3X = -20
                human3SpeedX = 0
            if hunterX <= -40:
                hunterX = -20
                hunterSpeedX = 0
            humanY= -3400
            beatHunter = randint(1,2) #The possibility of beating the hunter will be random, between 1 and 2. 50% chance of beating the hunter
            if moonX == WIDTH:
                moonX = WIDTH-1600
                humanSpeedX = 5
                human2SpeedX = -5
                human3SpeedX = 5
                night = False
                day = True
        #Night Time----------------------------------------------------------------
                
    #Day/Night Cycle-----------------------------------------------------------
        
    #Drawing Environment, Character, and HUD-----
        grass = pygame.image.load("Grass.png")
        gameWindow.blit(grass,(0,HEIGHT-680))
        tent = pygame.image.load("tent.png")
        gameWindow.blit(tent,(tentX,tentY))
        tent2 = pygame.image.load("tent 2.png")
        gameWindow.blit(tent2,(tent2X,tent2Y))
        
    #Player and health---------------------------
        
        if moving == False and LEFT == False and health > 0: #While the player is not moving, draw the standing image
            player = playerStand
            gameWindow.blit(player,(playerX,playerY))
            LEFT = False
        if moving == False and LEFT == True and health > 0: #If the player is not moving but they are facing left, draw the standing left image
            player = playerStandLeft
            gameWindow.blit(player,(playerX,playerY))
        if moving == True and RIGHT == True and health > 0:
            if UP == True and RIGHT == True:
                player = playerUpRight
                gameWindow.blit(player,(playerX,playerY))
                UP = False
                LEFT = False
                RIGHT = False
            elif DOWN == True and RIGHT == True and health > 0:
                player = playerDown
                gameWindow.blit(player,(playerX,playerY))
                DOWN = False
                LEFT = False
                RIGHT = False
            else:
                player = playerRight
                gameWindow.blit(player,(playerX,playerY))
            moving = False
            LEFT = False
            RIGHT = False
        if moving == True and LEFT == True and health > 0:
            if UP == True and LEFT == True and health > 0:
                player = playerUpLeft
                gameWindow.blit(player,(playerX,playerY))
                UP = False
            elif DOWN == True and LEFT == True and health > 0:
                player = playerDownLeft
                gameWindow.blit(player,(playerX,playerY))
                DOWN = False
            else:
                player = playerLeft
                gameWindow.blit(player,(playerX,playerY))
            moving = False
        if moving == True and UP == True and health > 0:
            player = playerUp
            gameWindow.blit(player,(playerX,playerY))
            moving = False
            LEFT = False
            UP = False
        if moving == True and DOWN == True and health > 0:
            player = playerDown
            gameWindow.blit(player, (playerX,playerY))
            moving = False
            left = False
            DOWN = False
        if health >= 2:
            healthX = 980
            gameWindow.blit(Heart,(healthX,healthY-30))
        if health >= 3:
            health2X = 1060
            gameWindow.blit(Heart,(health2X,health2Y-30))
        if health >= 4:
            health3X = 1140
            health = 4
            gameWindow.blit(Heart,(health3X,health3Y-30))
    #Player and health---------------------------
            
    #humans and hunter boundaries---------------------------
        if humanX < -20: #If the human hits the left side of the screen
            humanSpeedX = humanSpeedX * -1 #They will go in the other direction
        if humanX >= WIDTH - 10:
            humanSpeedX = humanSpeedX * -1
        if humanY >= HEIGHT-100:
            humanSpeedY = humanSpeedY *-1
        if humanY <= HEIGHT-500:
            humanSpeedY = humanSpeedY *-1
        if humanSpeedX > 0:
            gameWindow.blit(humanRight,(humanX,humanY))
        elif humanSpeedX < 0:
            gameWindow.blit(humanLeft,(humanX,humanY))
            
        if human2X < -20: #If the human hits the left side of the screen
            human2SpeedX = human2SpeedX * -1 #They will go in the other direction
        if human2X >= WIDTH + 100:
            human2SpeedX = human2SpeedX * -1
        if human2Y >= HEIGHT-100:
            human2SpeedY = human2SpeedY *-1
        if human2Y <= HEIGHT-500:
            human2SpeedY = human2SpeedY *-1
        if human2SpeedX > 0:
            gameWindow.blit(humanRight,(human2X,human2Y))
        elif human2SpeedX < 0:
            gameWindow.blit(humanLeft,(human2X,human2Y))

        if human3X < -20: #If the human hits the left side of the screen
            human3SpeedX = human3SpeedX * -1 #They will go in the other direction
        if human3X >= WIDTH + 10:
            human3SpeedX = human3SpeedX * -1
        if human3Y >= HEIGHT-100:
            human3SpeedY = human3SpeedY *-1
        if human3Y <= HEIGHT-500:
            human3SpeedY = human3SpeedY *-1
        if human3SpeedX > 0:
            gameWindow.blit(humanRight,(human3X,human3Y))
        elif human3SpeedX < 0:
            gameWindow.blit(humanLeft,(human3X,human3Y))
            
        if hunterX < -20: #If the hunter hits the left side of the screen
            hunterSpeedX = hunterSpeedX * -1 # they will go in the other direction
        if hunterX >= WIDTH - 10:
            hunterSpeedX = hunterSpeedX * -1
        if hunterY >= HEIGHT-120:
            hunterSpeedY = hunterSpeedY *-1
        if hunterY <= HEIGHT-500:
            hunterSpeedY = hunterSpeedY *-1
        if hunterSpeedX > 0:
            gameWindow.blit(hunterRight,(hunterX,hunterY))
        elif hunterSpeedX < 0:
            gameWindow.blit(hunterLeft,(hunterX,hunterY))
    #humans and hunter boundaries---------------------------
            
        tree1 = pygame.image.load("tree.png")
        tree1 = pygame.transform.scale(tree1,(200,200))
        gameWindow.blit(tree1,(treeX,treeY+100))
        tree2 = pygame.image.load("tree.png")
        tree2 = pygame.transform.scale(tree2,(200,200))
        gameWindow.blit(tree2,(tree2X,tree2Y+100))
        tree3 = pygame.image.load("tree.png")
        tree3 = pygame.transform.scale(tree3,(200,200))
        gameWindow.blit(tree3,(tree3X,tree3Y+100))
        tree4 = pygame.image.load("tree.png")
        tree4 = pygame.transform.scale(tree4,(200,200))
        gameWindow.blit(tree4,(tree4X,tree4Y+100))
        tree5 = pygame.image.load("tree.png")
        tree5 = pygame.transform.scale(tree3,(200,200))
        gameWindow.blit(tree5,(tree5X,tree5Y+100))
        tree7 = pygame.image.load("tree.png")
        tree7 = pygame.transform.scale(tree7,(200,200))
        gameWindow.blit(tree7,(tree7X,tree7Y+100))
        tentInner = pygame.image.load("tent In.png")
        gameWindow.blit(tentInner,(tentX,tentY))
        tentInner2 = pygame.image.load("tent In 2.png")
        gameWindow.blit(tentInner2,(tent2X,tent2Y))
    #Drawing Environment, Character, and HUD-----

    #Collision-----------------
        playerRect = pygame.Rect(playerX,playerY,playerW,playerH) #Create a collision detection for the player based on their position, and their size
        tree1Rect = pygame.Rect(treeX,treeY+160,150,200)
        tree2Rect = pygame.Rect(tree2X,tree2Y+100,200,200)
        tree3Rect = pygame.Rect(tree3X-15,tree3Y,200,200)
        tree4Rect = pygame.Rect(tree4X-20,tree4Y+140,200,200)
        tree5Rect = pygame.Rect(tree5X+25,tree5Y+160,200,200)
        tree7Rect = pygame.Rect(tree7X-20,tree7Y+160,200,200)
        tentRect = pygame.Rect(tentX,tentY-60,144,142)
        tent2Rect = pygame.Rect(tent2X,tent2Y-60,144,142)
        human1Rect = pygame.Rect(humanX,humanY,60,60)
        human2Rect = pygame.Rect(human2X,human2Y,60,60)
        human3Rect = pygame.Rect(human3X,human3Y,60,60)
        hunter1Rect = pygame.Rect(hunterX,hunterY,60,60)
        if playerRect.colliderect(human1Rect) and keys[pygame.K_SPACE]: #Determines whether or not the player eats a human. They eat the human if they are colliding with them and they press the spacebar
            humanY= -300 #The human will be 'dead' so they will be moved off the screen
            health +=1 #The player will gain health.
            humanX = -40#Moves the human position behind the screen
            bite = pygame.mixer.Sound('Bite.wav')
            bite.play()
        if playerRect.colliderect(human2Rect) and keys[pygame.K_SPACE]:
            human2Y = -300
            health += 1
            human2X = -40
            bite = pygame.mixer.Sound('Bite.wav')
            bite.play()
        if playerRect.colliderect(human3Rect) and keys[pygame.K_SPACE]:
            human3Y = -300
            health += 1
            human3X = -40
            bite = pygame.mixer.Sound('Bite.wav')
            bite.play()
        if playerRect.colliderect(hunter1Rect) and keys[pygame.K_SPACE]:
            if beatHunter == 1 and nightsSurvived < 3: #If the beatHunter variable randomizes to one, the hunter will beat the player, so the player loses health
                health-= 1
                pain = pygame.mixer.Sound('Pain.wav')
                pain.play()
            elif beatHunter == 1 and nightsSurvived > 3: #Player will lose two hearts if they have survived more then three nights and the hunter beats them
                health -=2
                pain = pygame.mixer.Sound('Pain.wav')
                pain.play()
            elif beatHunter == 2: #If the beatHunter variable randomizes to two, the player will beat the hunter, so the player loses health
                health+=1
                bite = pygame.mixer.Sound('Bite.wav')
                bite.play()
            hunterX = -40#Moves the hunter position behind the screen
        
    #Collision-----------------

        
    #Keybinds----------------------
        pygame.event.get()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]: #If the player presses the UP key
            moving = True# They will be moving
            UP = True #They will be going up
            playerY -= 15 #Make the character move 15 pixels at a time negativaly on the Y axis
        if keys[pygame.K_DOWN]:
            moving = True
            DOWN = True
            playerY += 15
        if keys[pygame.K_LEFT]:
            moving = True
            LEFT = True
            playerX -= 15
        if keys[pygame.K_RIGHT]:
            moving = True
            RIGHT = True
            playerX += 15
        if keys[pygame.K_ESCAPE]:
            pygame.quit() #Close the game
    #Keybinds-----------------------

    #Boundary Setup-----------------
        if playerX >= WIDTH-playerW-18:
            playerX = WIDTH-playerW-18
        if playerX < 0:
            playerX = 0
        if playerY > HEIGHT-playerH:
            playerY = HEIGHT-playerH
        if playerY <= HEIGHT-500:
            playerY = HEIGHT-500
    #Boundary Setup-----------------

        if health <= 0: #When the health reaches zero, all the health bars will disappear and the player death animation will play
            health3X = -50
            health2X = -50
            healthX = -50
            animation_counter = animation_counter + 1
            if animation_counter >= 1:
                player = playerDeath
            if animation_counter >= 2:
                player = playerDeath2
            if animation_counter >= 3:
                player = playerDeath3
            if animation_counter >= 4:
                player = playerDeath4
            if animation_counter >= 5:
                player = playerDeath5
            if animation_counter >= 6:
                player = playerDeath6
            if animation_counter >= 7:
                player = playerDeath7
            if animation_counter >= 8:
                player = playerDeath9
            if animation_counter >= 9:
                player = playerDeath10
            if animation_counter >= 10:
                player = playerDeath11
            if animation_counter >= 20: #Once the death animation is finished, the main game will end
                inPlay = False
            sizzle = pygame.mixer.Sound('Sizzle.wav')
            sizzle.play()
            gameWindow.blit(player,(playerX,playerY))
        if health<=3:
            health3X = -50
        if health <= 2:
            health2X = -50
        if health <= 1:
            healthX = -50
            health=0
        gameScore = font.render(("Nights survived: " + str(nightsSurvived)),1,RED)
        gameWindow.blit(gameScore,(850,10))
        quitting = font2.render(("Press ESC to exit the game"),1,BLACK)
        gameWindow.blit(quitting,(980,670))
        pygame.time.delay(10)
        hunterX += hunterSpeedX #The hunter's X value will increase according to its speed
        hunterY += hunterSpeedY
        humanX += humanSpeedX
        humanY += humanSpeedY
        human2X += human2SpeedX
        human2X += human2SpeedX
        human3X += human3SpeedX
        human3Y += human3SpeedY
        pygame.display.update()
    #Main game------------------------------------------------------

        
    #End Screen--------------------
    endMusic = pygame.mixer.music.load('endMusic.mp3')
    pygame.mixer.music.play(-1)
    while health == 0: #When the player has no health
        gameWindow.fill(RED)
        if nightsSurvived == 1:
            gameScore = font.render(("You survived for " + str(nightsSurvived)+ " night"),1,BLACK)
        else:
            gameScore = font.render(("You survived for " + str(nightsSurvived)+ " nights"),1,BLACK) #Display the amount of nights they survived for
        pygame.event.get()
        keys = pygame.key.get_pressed()
        restart = font.render(("Press R to restart the game"),1,BLACK)
        quitting = font2.render(("Press ESC to exit the game"),1,BLACK)
        gameWindow.blit(quitting,(980,670))
        if keys[pygame.K_r]: #Game will restart when the player presses R
            main()
        if keys[pygame.K_ESCAPE]:
            pygame.quit()
        gameWindow.blit(gameScore,(400,200))
        gameWindow.blit(restart,(400,400))
        pygame.display.update()
    #End Screen--------------------
main()





