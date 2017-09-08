# 1. import pygame
import pygame
# from the math module built into python, get the fabs object
from math import fabs

# 2. Init pygame
pygame.init()

#3. create a screen with a particular size
#the screen size must be a tuple
screen_size = (512,480)
# actually tell pygame to set the screen up and store it
pygame_screen = pygame.display.set_mode(screen_size)
## set a pointless caption
pygame.display.set_caption("Gobin_Chase")
# set up a wvar with our image
background_image = pygame.image.load('./images/background.png')

hero_image = pygame.image.load('./images/hero.png')

goblin_image = pygame.image.load('./images/goblin.png')

#make a font so we can write on the screen
font = pygame.font.Font(None, 25)
wins_text = font.render("Wins: %d" % (hero['wins']), True, (0,0,0))


# 8.. Set up the hero location
hero = {
	"x": 100,
	"y": 100,
	"speed": 20,
	"wins": 0
}

#make a font so we can write on the screen
font = pygame.font.Font(None, 25)
wins_text = font.render("Wins: %d" % (hero['wins']), True, (0,0,0))

goblin = {
	"x": 200,
	"y": 200,
	"speed": 15
}

keys = {
	"up": 273,
	"down": 274,
	"right": 275,
	"left": 276
}

keys_down = {
	"up": False,
	"down": False,
	"left": False,
	"right": False
}



# 4.create a game loop (While)
# create a boolean for whether the game should be going or not
game_on = True
while game_on:
	# we are inside the main game loop
	# it will keep running as long as our bool is true

	# 5. add a quit event (python needs an escape)
	# pygame comes with an event loop (sort of like JS)
	for event in pygame.event.get():
		# we're after the quit event
		if (event.type == pygame.QUIT):
			# The user clicked the red x in the top left
			game_on = False
		elif event.type == pygame.KEYDOWN:
			# print "User pressed a key!"
			if event.key == keys['up']:
				keys_down['up']= True
				# user pressed up!!
				# hero['y'] -= hero['speed']
			elif event.key == keys['down']:
				keys_down['down'] = True
				# hero['y'] += hero['speed']
			elif event.key == keys['left']:
				keys_down['left'] = True
				# hero['y'] += hero['speed']
			elif event.key == keys['right']:
				keys_down['right'] = True
				# hero['x'] += hero['speed']
		elif event.type == pygame.KEYUP:
			# the user let go of a key. see if it's one that matters.
			# if user let go of the up key, Flip the boolean.
			if event.key == keys['up']:
				keys_down['up'] = False
			if event.key == keys['down']:
				keys_down['down'] = False
			if event.key == keys['left']:
				keys_down['left'] = False
			if event.key == keys['right']:
				keys_down['right'] = False

	# the key may be up or down to move the hero
	# the images are 32 x 32
	if keys_down['up']:
		hero['y'] -= hero['speed']
	elif keys_down['down']:
		hero['y'] += hero['speed']
	# the key may be right or left
	if keys_down['left']:
		hero['x'] -= hero['speed']
	elif keys_down['right']:
		hero['x'] += hero['speed']

	# COLLISION DETECTION!!   (absolute value - don't care which axis- just find distances < 32, they're
	#. touching). fabs = floating pt absolute
	distance_between = fabs(hero['x'] - goblin['x']) + fabs(hero['y'] - goblin['y'])
	if distance_between < 32:
		print 'collision!'
	else:
		print 'not touching!'

	#make a font so we can write on the screen
	font = pygame.font.Font(None, 25)
	wins_text = font.render("Wins: %d" % (hero['wins']), True, (0,0,0))

		# the key may be up or down to move the goblin
	# if keys_down['up']:
	# 	hero['y'] -= hero['speed']
	# elif keys_down['down']:
	# 	hero['y'] += hero['speed']
	# # the key may be right or left
	# if keys_down['left']:
	# 	hero['x'] -= hero['speed']
	# elif keys_down['right']:
	# 	hero['x'] += hero['speed']
			

	# 6. fill in the screen with a color (or image)
	# blit takes 2 arguments
	# 1. what do youwant to draw
	# 2. where do you want to draw it [0,0]
	pygame_screen.blit(background_image, [0,0])
	# this must have a list
	pygame_screen.blit(hero_image, [hero['x'], hero['y']])

	pygame_screen.blit(goblin_image, [goblin['x'], goblin['y']])


	# 7.  repeat 6 over and over over...
	pygame.display.flip()


