# This prints instructions for the user and lets them set the level.

print ("You are about to play a small game.\nThere are 3 enemy ghosts. Do not touch them or you will lose.\nCollect the cherry to win.\nUse the arrow keys to move the pac-man.")
level = int(input("Please enter the level from 1 to 3 you want to play at where 1 is easy and 3 is difficult:"))       

# Imports the needed packages
import pygame
import random

# Initialises the pygame package

pygame.init()

# Sets the game screen size

screen_width = 2000
screen_height = 1000
screen = pygame.display.set_mode((screen_width,screen_height))

# Loads in all the images

player = pygame.image.load("player.jpg")
enemy1 = pygame.image.load("monsterBlue.jpg")
enemy2 = pygame.image.load("monsterRed.jpg")
enemy3 = pygame.image.load("monsterYellow.jpg")
prize = pygame.image.load("prize.jpg")

# Loads in the image dimensions
 
player_height = player.get_height()
player_width = player.get_width()
monsterBlue_height = enemy1.get_height()
monsterBlue_width = enemy1.get_width()
monsterRed_height = enemy2.get_height()
monsterRed_width = enemy2.get_width()
monsterYellow_height = enemy3.get_height()
monsterYellow_width = enemy3.get_width()
prize_height = prize.get_height()
prize_width = prize.get_width()

# Sets the player starting position to the middle of the screen

playerXPosition = (screen_width-player_width)/2
playerYPosition = (screen_height-player_height)/2

# Sets the enemy start positions to the corners of the screen

enemy1XPosition = 0
enemy1YPosition = 0
enemy2XPosition = 0
enemy2YPosition = screen_height-monsterRed_height
enemy3XPosition = screen_width-monsterYellow_width
enemy3YPosition = 0

#Sets the prize at a random position

prizeXPosition = random.randint(0,screen_width-prize_width)
prizeYPosition = random.randint(0,screen_height-prize_height)

# Declares all the keys that can be pressed during the game as false

keyUp= False
keyDown = False
keyLeft = False
keyRight = False

# Sets any directional movement for all enemies to false

enemy1MoveRight = False
enemy1MoveLeft = False
enemy1MoveUp = False
enemy1MoveDown = False

enemy2MoveRight = False
enemy2MoveLeft = False
enemy2MoveUp = False
enemy2MoveDown = False

enemy3MoveRight = False
enemy3MoveLeft = False
enemy3MoveUp = False
enemy3MoveDown = False

# sets the count variable to 0

count = 0

# This loop runs untill the user either wins or looses

while 1:

    # Sets a variable distance to a random number
    distance = random.randint(50,2000)

    # Chooses a directional random number from 1 - 4 (each number having a different direction) for each enemy - this allows the enemies to move in different directions at random
    enemy1Direction = random.randint(1,4)
    enemy2Direction = random.randint(1,4)
    enemy3Direction = random.randint(1,4)

    # The movements need to be reset to false to allow for only one direction to be true during the for loop

    enemy1MoveRight = False
    enemy1MoveLeft = False
    enemy1MoveUp = False
    enemy1MoveDown = False

    enemy2MoveRight = False
    enemy2MoveLeft = False
    enemy2MoveUp = False
    enemy2MoveDown = False

    enemy3MoveRight = False
    enemy3MoveLeft = False
    enemy3MoveUp = False
    enemy3MoveDown = False

    # Runs this loop for the random number of times randomly selected by the variable distance to allow the enemies to move in one direction for several loops
        
    for count in range (0,distance):

        # If the enemy direction (numbers 1-4) is randomly chosen above then the boolean values will become true for that number for each enemy: 

        if enemy1Direction == 1:
            enemy1MoveRight = True
        if enemy1Direction == 2:
            enemy1MoveLeft = True
        if enemy1Direction == 3:
            enemy1MoveUp = True
        if enemy1Direction == 4:
            enemy1MoveDown = True

        if enemy2Direction == 1:
            enemy2MoveRight = True
        if enemy2Direction == 2:
            enemy2MoveLeft = True
        if enemy2Direction == 3:
            enemy2MoveUp = True
        if enemy2Direction == 4:
            enemy2MoveDown = True

        if enemy3Direction == 1:
            enemy3MoveRight = True
        if enemy3Direction == 2:
            enemy3MoveLeft = True
        if enemy3Direction == 3:
            enemy3MoveUp = True
        if enemy3Direction == 4:
            enemy3MoveDown = True

        # If the enemies' movement value becomes true then the position of the image will change based on the which value becomes true in the previous step
        # Also depending on which direction it is travelling in the loop will break if one of the enemies reaches the screen boundries
        
        if enemy1MoveRight == True: 
            if enemy1XPosition > screen_width-monsterBlue_width:
                break
            enemy1XPosition +=  level
        if enemy1MoveLeft == True: 
            if enemy1XPosition < 0:
                break
            enemy1XPosition -= level
        if enemy1MoveDown == True:    
            if enemy1YPosition > screen_height-monsterBlue_height:
                break
            enemy1YPosition += level
        if enemy1MoveUp == True:  
            if enemy1YPosition < 0:
                break
            enemy1YPosition -= level

        if enemy2MoveRight == True: 
            if enemy2XPosition > screen_width-monsterRed_width:
                break
            enemy2XPosition += level
        if enemy2MoveLeft == True: 
            if enemy2XPosition < 0:
                break
            enemy2XPosition -= level
        if enemy2MoveDown == True:    
            if enemy2YPosition > screen_height-monsterRed_height:
                break
            enemy2YPosition += level
        if enemy2MoveUp == True:  
            if enemy2YPosition < 0:
                break
            enemy2YPosition -= level

        if enemy3MoveRight == True: 
            if enemy3XPosition > screen_width-monsterYellow_width:
                break
            enemy3XPosition += level
        if enemy3MoveLeft == True: 
            if enemy3XPosition < 0:
                break
            enemy3XPosition -= level
        if enemy3MoveDown == True:    
            if enemy3YPosition > screen_height-monsterYellow_height:
                break
            enemy3YPosition += level
        if enemy3MoveUp == True:  
            if enemy3YPosition < 0:
                break
            enemy3YPosition -= level

        # Clears the screen and moves the image to the new X and Y positions (The loop running through the changing positions is what makes the image appear to move)

        screen.fill(0) 
        screen.blit(player, (playerXPosition, playerYPosition))
        screen.blit(enemy1, (enemy1XPosition, enemy1YPosition))
        screen.blit(enemy2, (enemy2XPosition, enemy2YPosition))
        screen.blit(enemy3, (enemy3XPosition, enemy3YPosition))
        screen.blit(prize, (prizeXPosition, prizeYPosition))

        # This part of the code allows the user to change the values of the keys to true in order to move the player image

        pygame.display.flip()

        # This detects the position of the key as either up or down and then changes the values of the keys to either true or false

        for event in pygame.event.get():
                                
            if event.type == pygame.QUIT:
                pygame.quit()
                exit(0)
                                    
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    keyUp = True
                if event.key == pygame.K_DOWN:
                    keyDown = True
                if event.key == pygame.K_LEFT:
                    keyLeft = True
                if event.key == pygame.K_RIGHT:
                    keyRight = True

            if event.type == pygame.KEYUP:  
                if event.key == pygame.K_UP:
                    keyUp = False
                if event.key == pygame.K_DOWN:
                    keyDown = False
                if event.key == pygame.K_LEFT:
                    keyLeft = False
                if event.key == pygame.K_RIGHT:
                    keyRight = False

        # Moves the player image based on the true or false values of the keys being pressed
        # It also determines which direction the playes image will move in and has specific boundries for each changing position so that the player cannot move beyond the screen

        if keyUp == True:
            if playerYPosition > 0:
                playerYPosition -= 1
        if keyDown == True:
            if playerYPosition < screen_height - player_height:
                playerYPosition += 1
        if keyRight == True:
            if playerXPosition < screen_width - player_width:
                playerXPosition += 1
        if  keyLeft == True:
            if playerXPosition > 0:
                playerXPosition -= 1

        # Creates a box around each image to define its boundreis and allows the box to change position with the image

        playerBox = pygame.Rect(player.get_rect())
        playerBox.top = playerYPosition
        playerBox.left = playerXPosition

        enemy1Box = pygame.Rect(enemy1.get_rect())
        enemy1Box.top = enemy1YPosition
        enemy1Box.left = enemy1XPosition

        enemy2Box = pygame.Rect(enemy2.get_rect())
        enemy2Box.top = enemy2YPosition
        enemy2Box.left = enemy2XPosition

        enemy3Box = pygame.Rect(enemy3.get_rect())
        enemy3Box.top = enemy3YPosition
        enemy3Box.left = enemy3XPosition

        prizeBox = pygame.Rect(prize.get_rect())
        prizeBox.top = prizeYPosition
        prizeBox.left = prizeXPosition

        # If statement that will break the loop if two of the enemies touch eachother 

        if enemy1Box.colliderect(enemy2Box) or enemy1Box.colliderect(enemy3Box) or enemy2Box.colliderect(enemy3Box):
            break

        # If statement that will end the game and print you lose if the player touches one of the enemies

        if playerBox.colliderect(enemy1Box) or playerBox.colliderect(enemy2Box) or playerBox.colliderect(enemy3Box) :
            print("You lose!")
            pygame.quit()
            exit(0)

        # If statement that will end the game and print you win if the player touches the prize image

        if playerBox.colliderect(prizeBox):
            print("You win!")
            pygame.quit()
            exit(0)
            

        
