#Anika Czander
#Computing Concepts
#Frogger Game!

import time
import pygame
import random

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
car_list = pygame.sprite.Group()

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
		if pixels < 700:
			self.rect.x += pixels
	def moveLeft(self,pixels):
		if pixels > 0:
			self.rect.x -= pixels
	def moveUp(self,pixels):
		if pixels < 500:
			self.rect.y -= pixels
	def moveDown(self,pixels):
		if pixels > 0:
			self.rect.y += pixels
	def handleKeys(self):
		keys = pygame.key.get_pressed()
		if keys[pygame.K_LEFT]:
			frog1.moveLeft(5)
		if keys[pygame.K_RIGHT]:
			frog1.moveRight(5)
		if keys[pygame.K_UP]:
			frog1.moveUp(5)
		if keys[pygame.K_DOWN]:
			frog1.moveDown(5)

class Car(pygame.sprite.Sprite):
	def __init__(self,color,width,height,speed):
		super().__init__()
		self.image = pygame.Surface([width,height])
		self.image.fill(WHITE)
		pygame.draw.rect(self.image,color,[0,0,width,height])
		#self.image = pygame.image.load("car.png").convert()
		self.image.set_colorkey(WHITE)
		self.rect = self.image.get_rect()
		self.speed = speed

	def moveRight(self,speed):
		if self.rect.x < 700:
			self.rect.x += speed
	def moveLeft(self,speed):
		self.rect.x -= pixels
	def moveForward(self, speed):
		self.rect.y += self.speed * speed / 20
	def moveBackward(self, speed):
		self.rect.y -= self.speed * speed / 20
	def changeSpeed(self, speed):
		self.speed = speed



for i in range(5):
	carObj = Car(BLACK,40,50,random.randint(50,100))
	carObj.rect.x = random.randint(0,500)
	carObj.rect.y = random.randint(0,500)
	car_list.add(carObj)
for j in range(0,len(car_list)):
	carObj.moveRight(5)

#create frog sprite
frog1 = Frog(RED,20,30)
frog1.rect.x = 200
frog1.rect.y = 300
list_of_sprites.add(frog1)

#Main program Loop
play = True
while play:
	# --- Main event loop
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			play = False
		elif event.type==pygame.KEYDOWN:
			if event.key==pygame.K_x:
				play = False

	list_of_sprites.update()
	frog1.handleKeys()

	#creates screen and lanes
	screen.fill(GREEN)
	pygame.draw.rect(screen, GREY, [0,350,700,75])
	pygame.draw.rect(screen, GREY, [0,200,700,75])
	pygame.draw.rect(screen, GREY, [0,50,700,75])


	#draws all sprites to screen
	list_of_sprites.draw(screen)
	car_list.draw(screen)

	# --- Go ahead and update the screen with what we've drawn.
	pygame.display.flip()

	# --- Limit to 60 frames per second
	clock.tick(60)

# Close the window and quit.
pygame.quit()