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

	def moveRight(self,pixels):
		self.rect.x += pixels
	def moveLeft(self,pixels):
		self.rect.x -= pixels
	def moveUp(self,pixels):
		self.rect.y -= pixels
	def moveDown(self,pixels):
		self.rect.y += pixels

class Car(pygame.sprite.Sprite):
	def __init__(self,color,width,height):
		super().__init__()
		self.image = pygame.Surface([width,height])
		self.image.fill(WHITE)
		pygame.draw.rect(self.image,color,[0,0,width,height])
		#self.image = pygame.image.load("car.png").convert()
		self.image.set_colorkey(WHITE)
		self.rect = self.image.get_rect()
	def moveRight(self,speed):
		self.rect.x += speed
	def moveLeft(self,speed):
		self.rect.x -= speed

#create frog sprite
frog1 = Frog(RED,20,30)
frog1.rect.x = 200
frog1.rect.y = 300
list_of_sprites.add(frog1)

#create base car sprite
car1 = Car(BLACK,20,30)
car1.rect.x = 50
car1.rect.y = 150
list_of_sprites.add(car1)

#Main program Loop
while not done:
	# --- Main event loop
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True
		elif event.type==pygame.KEYDOWN:
			if event.key==pygame.K_x:
				carryOn=False
		car1.moveRight(5)

	keys = pygame.key.get_pressed()
	if keys[pygame.K_LEFT]:
		frog1.moveLeft(5)
	if keys[pygame.K_RIGHT]:
		frog1.moveRight(5)
	if keys[pygame.K_UP]:
		frog1.moveUp(5)
	if keys[pygame.K_DOWN]:
		frog1.moveDown(5)

	list_of_sprites.update()

	#creates screen and lanes
	screen.fill(GREEN)
	pygame.draw.rect(screen, GREY, [0,350,700,75])
	pygame.draw.rect(screen, GREY, [0,200,700,75])
	pygame.draw.rect(screen, GREY, [0,50,700,75])


	#draws all sprites to screen
	list_of_sprites.draw(screen)
	# --- Go ahead and update the screen with what we've drawn.
	pygame.display.flip()

	# --- Limit to 60 frames per second
	clock.tick(60)

# Close the window and quit.
pygame.quit()