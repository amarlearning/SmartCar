# -*- coding: utf-8 -*-
# @Author: Amar Prakash Pandey
# @Date:  
# @Email: amar.om1994@gmail.com  
# @Github username: @amarlearning
# @Last Modified by: Amar Prakash Pandey  
# @Last Modified date:  
# MIT License. You can find a copy of the License
# @http://amarlearning.mit-license.org

# import library here
import pygame
import time
import random
from os import path

# Pygame module initialised 
pygame.init()

# constants are defined
display_width = 600
display_height = 600

# Material color init
white = (255,255,255)
black = (0,0,0)

# Folder path init
assets = path.join(path.dirname(__file__), 'assets')
extras = path.join(path.dirname(__file__), 'extras')

# Init images & sounds
gameIcon = pygame.image.load(path.join(assets + '/gameicon.png'))

# Game windown, caption initialised
gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('SmartCar')
pygame.display.update()

# Game icon init
pygame.display.set_icon(gameIcon)
gameplay = True

# Heart starts beating, Don't stop it!
while gameplay:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			gameplay = False
		else:
			print event

	gameDisplay.fill(white)
	pygame.display.update()


# You will win, try one more time. Don't Quit.
pygame.quit()

# you can signoff now, everything looks good!
quit()