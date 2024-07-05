#imports
import turtle as t
#variables
screen = t.Screen()
ganpati = t.Turtle()
blue = '#10557d'
white = '#ffffff'
red = '#ff0004'
black = '#000000'
yellow = '#ffb700'

screen.title('Ganpati Drawing')
ganpati.shape('turtle')

# pentagon
ganpati.color(blue, blue)
ganpati.begin_fill()
ganpati.left(angle=130)
ganpati.forward(distance=55)
ganpati.right(90)
ganpati.forward(70)
ganpati.right(65)
ganpati.forward(70)
ganpati.right(80)
ganpati.forward(55)
ganpati.right(70)
ganpati.forward(66)
ganpati.end_fill()

ganpati.penup()
ganpati.forward(10)
ganpati.left(90)
ganpati.forward(12.5)
ganpati.pendown()

#square
ganpati.color(yellow, yellow)
ganpati.begin_fill()
ganpati.forward(90)
for _ in range(3):
    ganpati.left(90)
    ganpati.forward(90)
ganpati.end_fill()

ganpati.penup()
ganpati.forward(10)
ganpati.pendown()

#rectangle 1
ganpati.color(red, red)
ganpati.begin_fill()
for _ in range(2):
    ganpati.forward(27.5)
    ganpati.right(90)
    ganpati.backward(90)
    ganpati.right(90)

ganpati.penup()
ganpati.right(180)
ganpati.forward(137.5)
ganpati.pendown()

#rectangle 2
for _ in range(2):
    ganpati.backward(27.5)
    ganpati.right(90)
    ganpati.forward(90)
    ganpati.right(90)
ganpati.end_fill()

ganpati.penup()
ganpati.left(180)
ganpati.forward(57.5)
ganpati.left(90)
ganpati.forward(5)
ganpati.left(90)
ganpati.pendown()

# Bindi line 1
ganpati.color(white)
ganpati.backward(50)

ganpati.penup()
ganpati.right(90)
ganpati.forward(5)
ganpati.left(90)
ganpati.pendown()

#Bindi line 2
ganpati.forward(50)

ganpati.penup()
ganpati.right(90)
ganpati.forward(5)
ganpati.left(90)
ganpati.pendown()

#Bindi line 3
ganpati.backward(50)

ganpati.penup()
ganpati.right(90)
ganpati.forward(10)
ganpati.pendown()

#Eye 1
ganpati.color(black, black)
ganpati.begin_fill()
ganpati.circle(5)

ganpati.penup()
ganpati.left(90)
ganpati.forward(50)
ganpati.pendown()

#Eye 2import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up display
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Simple Game')

# Set up colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Set up player
player_pos = [400, 300]
player_size = 50

# Set up game clock
clock = pygame.time.Clock()

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Get key states
    keys = pygame.key.get_pressed()

    # Update player position based on key input
    if keys[pygame.K_LEFT]:
        player_pos[0] -= 5
    if keys[pygame.K_RIGHT]:
        player_pos[0] += 5
    if keys[pygame.K_UP]:
        player_pos[1] -= 5
    if keys[pygame.K_DOWN]:
        player_pos[1] += 5

    # Fill the screen with white
    screen.fill(WHITE)

    # Draw the player as a red rectangle
    pygame.draw.rect(screen, RED, (player_pos[0], player_pos[1], player_size, player_size))

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(30)
ganpati.circle(5)
ganpati.end_fill()

ganpati.penup()
ganpati.right(180)
ganpati.forward(30)
ganpati.left(90)
ganpati.forward(25)
ganpati.pendown()

#Nose
ganpati.color(red, red)
ganpati.begin_fill()
ganpati.forward(100)
ganpati.left(90)
ganpati.forward(50)
ganpati.left(90)
ganpati.forward(20)
ganpati.left(90)
ganpati.forward(30)
ganpati.right(90)
ganpati.forward(80)
ganpati.end_fill()

# finisher
ganpati.penup()
ganpati.forward(1000)

screen.mainloop()