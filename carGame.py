# -*- coding: utf-8 -*-
# @Author: Amar Prakash Pandey
# @Date: 25-08-2016 
# @Email: amar.om1994@gmail.com  
# @Github username: @amarlearning 
# MIT License. You can find a copy of the License
# @http://amarlearning.mit-license.org

# import library here
import pygame
import time
import random
from os import path

# Material color init
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
darkBlue = (0,0,128)
white = (255,255,255)
black = (0,0,0)
grey = (211,211,211)

# Pygame module initialised 
pygame.init()

# Folder path init
assets = path.join(path.dirname(__file__), 'assets')
extras = path.join(path.dirname(__file__), 'extras')

# Display width and height are defined
display_width = 700
display_height = 600

# greenland width and height
grass_width = 170
grass_height = 600

# Road and Greenland seperator
border_width = 30
border_height = 600

# Road's divider width and height
divider_width = 20
divider_height = 80

#  Increment of divider
block = 0

# Images position locations
carLeftPosiitonX = 240
carLeftPosiitonY = 480
carRightPosiitonX = 400
carRightPosiitonY = 480

# Frames per second
FPS = 10

# Init images & sounds
gameIcon = pygame.image.load(path.join(assets + '/gameicon.png'))
grassRoad = pygame.image.load(path.join(assets + '/grassslip.png'))
grass = pygame.image.load(path.join(assets + '/grass-sp.png'))
SmartCarImage = pygame.image.load(path.join(assets + '/smartcar.png'))
clock = pygame.time.Clock()

# Image transformation 
SmartCarImage = pygame.transform.rotate(SmartCarImage, 90)

# Game windown, caption initialised
gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('SmartCar')

# Game basic design init [Left side]
pygame.draw.rect(gameDisplay, green, (0, 0, grass_width, grass_height))
pygame.draw.rect(gameDisplay, grey, (grass_width, 0, border_width, border_height))

# Game basic design init [Right side]
pygame.draw.rect(gameDisplay, green, (display_width - grass_width, 0, grass_width, grass_height))
pygame.draw.rect(gameDisplay, grey, (display_width - grass_width - border_width, 0, border_width, border_height))

gameDisplay.blit(grassRoad, (0,0))
gameDisplay.blit(grassRoad, (0,63))
gameDisplay.blit(grassRoad, (0,63*2))
gameDisplay.blit(grassRoad, (0,63*3))
gameDisplay.blit(grassRoad, (0,63*4))
gameDisplay.blit(grassRoad, (0,63*5))
gameDisplay.blit(grassRoad, (0,63*6))
gameDisplay.blit(grassRoad, (0,63*7))
gameDisplay.blit(grassRoad, (0,63*8))
gameDisplay.blit(grassRoad, (0,63*9))



# Picturising car image, sorry SmartCar image
gameDisplay.blit(SmartCarImage, (carLeftPosiitonX,carLeftPosiitonY))

pygame.display.update()



# Game icon init
pygame.display.set_icon(gameIcon)
gameplay = True

# Heart starts beating, Don't stop it!
while gameplay:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			gameplay = False
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_RIGHT:
				gameDisplay.blit(SmartCarImage, (carRightPosiitonX,carRightPosiitonY))
				pygame.display.update()
			if event.key == pygame.K_LEFT:
				gameDisplay.blit(SmartCarImage, (carLeftPosiitonX,carLeftPosiitonY))
				pygame.display.update()
		else:
			print event

	# Dividing th road, not the people 
	pygame.draw.rect(gameDisplay, white, ((display_width/2 - 10),20 + block,divider_width,divider_height))
	block += 140

	pygame.display.update()

	clock.tick(FPS)

# You will win, try one more time. Don't Quit.
pygame.quit()

# you can signoff now, everything looks good!
quit()
