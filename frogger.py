#Anika Czander
#Computing Concepts
#Frogger Game!


import pygame
import random
from random import *

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (4, 150, 4)
RED = (255, 0, 0)
GREY = (210, 210 ,210)

# Set the width and height of the screen [width, height]
size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Frogger")

list_of_sprites = pygame.sprite.Group()

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

class Frog(pygame.sprite.Sprite):
	#class for Frog sprite
	def __init__(self,color,width,height):
		#constructor that takes the x and y positions of the frog
		super().__init__()
		#loads image
		self.image = pygame.Surface([width,height])
		self.image.fill(WHITE)
		pygame.draw.rect(self.image,color,[0,0,width,height])
		#self.image = pygame.image.load("frog.png").convert()
		#makes white background transparent
		self.image.set_colorkey(WHITE)
		self.rect = self.image.get_rect()
#Main program Loop
while not done:
	# --- Main event loop
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True
	#creates screen and lanes
	screen.fill(GREEN)
	pygame.draw.rect(screen, GREY, [0,350,700,75])
	pygame.draw.rect(screen, GREY, [0,200,700,75])
	pygame.draw.rect(screen, GREY, [0,50,700,75])
	#create frog sprite
	frog1 = Frog(RED,20,30)
	frog1.rect.x = 200
	frog1.rect.y = 300
	list_of_sprites.add(frog1)

	#draws all sprites to screen
	list_of_sprites.draw(screen)
	# --- Go ahead and update the screen with what we've drawn.
	pygame.display.flip()

	# --- Limit to 60 frames per second
	clock.tick(60)

# Close the window and quit.
pygame.quit()