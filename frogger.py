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
screen_width = 700
screen_height = 500
size = (screen_width, screen_height)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Frogger")

list_of_sprites = pygame.sprite.Group()
car_list1 = pygame.sprite.Group()
car_list2 = pygame.sprite.Group()
car_list3 = pygame.sprite.Group()

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
		self.score = 0

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
			self.moveLeft(5)
		if keys[pygame.K_RIGHT]:
			self.moveRight(5)
		if keys[pygame.K_UP]:
			self.moveUp(5)
		if keys[pygame.K_DOWN]:
			self.moveDown(5)
	def checkCollision(self,player,car):
		pygame.sprite.groupcollide(player,car,True,False)
		if len(list_of_sprites) == 0:
			newFrog = Frog(RED,20,30)
			newFrog.resetPos()
			list_of_sprites.add(newFrog)
			newFrog.handleKeys()
			pygame.display.flip()
		else:
			play = True
	def resetPos(self):
		self.rect.x = 350
		self.rect.y = 450
		self.handleKeys()

class Car(pygame.sprite.Sprite):
	def __init__(self,color,width,height):
		super().__init__()
		self.image = pygame.Surface([width,height])
		self.image.fill(WHITE)
		pygame.draw.rect(self.image,color,[0,0,width,height])
		#self.image = pygame.image.load("car.png").convert()
		self.image.set_colorkey(WHITE)
		self.rect = self.image.get_rect()
	def reset_pos(self):
		self.rect.x = 0
		pygame.display.flip()
	def update(self,speed):
		if self.rect.x > screen_width:
			self.reset_pos()
		'''elif self.rect.x > (screen_width/8):
			self.carCopy()'''
		self.rect.x += speed

	'''def carCopy(self):
		newCar() = self.reset_pos()
		car_list1.add(newCar)'''


def GameOver():
	pygame.font.init()
	endgame = pygame.font.SysFont("Calibri",50)
	textsurface = endgame.render("GAME OVER",True,BLACK)
	screen.blit(textsurface,(100,100))
	pygame.display.flip()


#create frog sprite
frog1 = Frog(RED,20,30)
frog1.rect.x = 350
frog1.rect.y = 450
list_of_sprites.add(frog1)

#creates lane 1 cars
car1 = Car(BLACK,40,60)
car1.rect.x = 0
car1.rect.y = 59
car_list1.add(car1)
#creates lane 2 cars
car2 = Car(BLACK,40,60)
car2.rect.x = 0
car2.rect.y = 206
car_list2.add(car2)
#creates lane 3 cars
car3 = Car(BLACK,40,60)
car3.rect.x = 0
car3.rect.y = 356
car_list3.add(car3)

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
	frog1.checkCollision(list_of_sprites,car_list1)
	frog1.checkCollision(list_of_sprites,car_list2)
	frog1.checkCollision(list_of_sprites,car_list3)

	speed1 = random.randrange(10,20)
	speed2 = random.randrange(10,20)
	speed3 = random.randrange(10,20)

	car_list1.update(speed1)
	car_list2.update(speed2)
	car_list3.update(speed3)
	list_of_sprites.update()

	for froggo in list_of_sprites:
		froggo.handleKeys()

	#creates screen and lanes
	screen.fill(GREEN)
	pygame.draw.rect(screen, GREY, [0,350,700,75])
	pygame.draw.rect(screen, GREY, [0,200,700,75])
	pygame.draw.rect(screen, GREY, [0,50,700,75])


	#draws all sprites to screen
	list_of_sprites.draw(screen)
	car_list1.draw(screen)
	car_list2.draw(screen)
	car_list3.draw(screen)

	# --- Go ahead and update the screen with what we've drawn.
	pygame.display.flip()

	# --- Limit to 60 frames per second
	clock.tick(20)

# Close the window and quit.
pygame.quit()