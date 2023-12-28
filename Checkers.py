import pygame, random

# Importing Font
pygame.font.init()

# Specifying the width and height in squares i.e a grid of 90.
width_in_sq, height_in_sq = 10,9

# Square Dimension
square_dimension = 80

# Specifying values for screen
screen = pygame.display.set_mode((width_in_sq*square_dimension, height_in_sq*square_dimension))
pygame.display.set_caption("Race To The Finish Line!!")

'''
Game Instructions for the User- 
This game is called "Race To The Finish Line!!", in this game we observe 2 computer-controlled players taking turns to 
reach the final tile/block, the one who reaches there first wins the game!! Enjoy observing the game!!

In this game, three board features have been used, they are-
1. Numbered Tiles - The tiles have been numbered from 1 to 90.
2. Exact Requirements - The players cannot move past the end of the board.
3. Sorry Collisions - If a player lands on top of another, it gets sent back to the start.
'''

# Specifying Color values
white = (255, 255, 255)
black = (  0,   0,   0)
red = (255, 0, 0)
blue = (0, 0, 255)

colour = white

# Specifying Start-Coordinates for both players.
player_1_x = 40
player_1_y = 40
player_2_x = 40
player_2_y = 40

# Drawing the Checkerboard
for i in range(0, height_in_sq):
	for j in range(0, width_in_sq):
		pygame.draw.rect(screen, colour, (j * square_dimension, i * square_dimension, square_dimension, square_dimension))
		pygame.display.update()	
		if colour == white:
			colour = black
		else:
			colour = white
	if colour == white:
		colour = black
	else:
		colour = white

# Numbering the Checkerboard/Tiles
n = 1
for i in range(0, height_in_sq):
    for j in range(0, width_in_sq):
        fontt = pygame.font.SysFont ("Ariel", 30)
        text = fontt.render(str(n), True, (120,120,120))
        screen.blit(text, ((j*square_dimension)+9 ,(i*square_dimension)+10))
        n+=1
        pygame.display.update()
new_screen = screen.copy()

# The Two pieces have been drawn with one being smaller than the other to make it easy to spot them. 
pygame.draw.circle(screen, blue, (player_1_x, player_1_y), 30)
pygame.draw.circle(screen, red, (player_2_x, player_2_y), 20)
pygame.display.update()
pygame.event.pump()
pygame.time.delay(1500)

# Main body of code that consists of Control flow, if and else statements.
running = True
while running:
    diceroll_1 = random.randint(1, 6)              # 2 dicerolls(6 sided) for player 1 using random.randint.
    diceroll_2 = random.randint(1, 6)

    dice_1 = diceroll_1 + diceroll_2
    print("Player 1 rolled",diceroll_1,"and",diceroll_2,". You move",dice_1,"blocks.\n")

    player_1_x += dice_1*square_dimension

    if player_1_x > 800:
        player_1_x = player_1_x - 800
        player_1_y = player_1_y + square_dimension
        screen.blit(new_screen, (0,0))
        pygame.draw.circle(screen, blue, (player_1_x, player_1_y), 30)
        pygame.draw.circle(screen, red, (player_2_x, player_2_y), 20)
        pygame.display.update()
        pygame.event.pump()
        pygame.time.delay(1000)

    else:
        pygame.draw.circle(screen, blue, (player_1_x, player_1_y), 30)
        pygame.display.update()
        screen.blit(new_screen, (0,0))
        pygame.draw.circle(screen, blue, (player_1_x, player_1_y), 30)
        pygame.draw.circle(screen, red, (player_2_x, player_2_y), 20)
        pygame.display.update()
        pygame.event.pump()
        pygame.time.delay(1000)

    if (player_1_x,player_1_y) == (player_2_x,player_2_y):             # Code for board feature - "Sorry Collisions"
        player_1_x = 40
        player_1_y = 40
    
    if player_1_y > 680:                             # Win condition for player 1/ player cannot move past the end of the boards
        print("Player 1 Wins the Game!!")
        running = False
        quit()
    
    diceroll_3 = random.randint(1, 6)               # 2 dicerolls(6 sided) for player 2 using random.randint.
    diceroll_4 = random.randint(1, 6)

    dice_2 = diceroll_3 + diceroll_4
    print("Player 2 rolled",diceroll_3,"and",diceroll_4,". You move",dice_2,"blocks.\n")

    player_2_x += dice_2*square_dimension


    if player_2_x > 800:
        player_2_x = player_2_x - 800 
        player_2_y = player_2_y + square_dimension
        screen.blit(new_screen, (0,0))
        pygame.draw.circle(screen, blue, (player_1_x, player_1_y), 30)
        pygame.draw.circle(screen, red, (player_2_x, player_2_y), 20)
        pygame.display.update()
        pygame.event.pump()
        pygame.time.delay(1000)

    else:
        pygame.draw.circle(screen, red, (player_2_x, player_2_y), 20)
        pygame.display.update()
        screen.blit(new_screen, (0,0))
        pygame.draw.circle(screen, blue, (player_1_x, player_1_y), 30)
        pygame.draw.circle(screen, red, (player_2_x, player_2_y), 20)
        pygame.display.update()
        pygame.event.pump()
        pygame.time.delay(1000)

    if (player_2_x,player_2_y) == (player_1_x,player_1_y):              # Code for board feature - "Sorry Collisions"
        player_2_x = 40
        player_2_y = 40  

    if player_2_y > 680:                                # Win condition for player 2/ player cannot move past the end of the boards
        print("Player 2 Wins the Game!!")
        running = False
        quit()