#!/usr/bin/env python

"""beetbox.py: Trigger script for the BeetBox."""

import pygame
import RPi.GPIO as GPIO
import mpr121 #References all headings and connections for the mpr121

# Use GPIO Interrupt Pin
GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.IN)

# Use mpr121 class for everything else
mpr121.TOU_THRESH = 0x30
mpr121.REL_THRESH = 0x33
mpr121.setup(0x5a)

# User pygame for sounds
pygame.mixer.pre_init(44100, -16, 12, 512) #(Frequency, size, channels, buffer)
pygame.init()

#Define Sounds for Drum Kit
drumKit = []
kick = pygame.mixer.Sound('samples/kick.wav')
kick.set_volume(.65);
snare = pygame.mixer.Sound('samples/snare.wav')
snare.set_volume(.65);
openhh = pygame.mixer.Sound('samples/open.wav')
openhh.set_volume(.65);
closedhh = pygame.mixer.Sound('samples/closed.wav')
closedhh.set_volume(.65);
clap = pygame.mixer.Sound('samples/clap.wav')
clap.set_volume(.65);
cymbal = pygame.mixer.Sound('samples/cymbal.wav')
cymbal.set_volume(.65);
<<<<<<< HEAD

test = pygyame.mixer.Sound('samples/other/test.wav')
test.set_volume(.65)


=======
>>>>>>> 8b3ef5c1ea72b575c0dfd215c06b7dc78da8357b
drumKit.append(kick)
drumKit.append(snare)
drumKit.append(openhh)
drumKit.append(closedhh)
drumKit.append(clap)
drumKit.append(cymbal)

# Track touches
touches = [0,0,0,0,0,0];

<<<<<<< HEAD
interrupted = False

#Run main loop
while interrupted == False:
=======
#Run main loop
while True:
>>>>>>> 8b3ef5c1ea72b575c0dfd215c06b7dc78da8357b
	try:

		#Detect input
		if (GPIO.input(7)): # Interupt pin is high
			pass
		else: # Interupt pin is low
			touchData = mpr121.readData(0x5a) #Take data from SDA Line
			for i in range(6): #Checks each touch value
				if (touchData & (1<<i)):
					if (touches[i] == 0):
						print( 'Pin ' + str(i) + ' was just touched') #Track changes, can be commented out
<<<<<<< HEAD
                                                                                                if touches[0] == 1:
                                                                                                        test.play()
                                                                                                        print('test worked')
                                                                                                else:
                                                                                                        drumKit[i].play()	
=======
						drumKit[i].play()	
>>>>>>> 8b3ef5c1ea72b575c0dfd215c06b7dc78da8357b

						#if (i == 0):
						#	kick.play()
						#elif (i == 1):
						#	snare.play()
						#elif (i == 2):
						#	openhh.play()
						#elif (i == 3):
						#	closedhh.play()
						#elif (i == 4):
						#	clap.play()
						#elif (i == 5):
						#	cymbal.play()

					touches[i] = 1;
				else:
					if (touches[i] == 1):
						print( 'Pin ' + str(i) + ' was just released')
					touches[i] = 0;
	except KeyboardInterrupt:
		print "Thank you for using Touching Fruit!!!"
<<<<<<< HEAD
		interrupted = True
=======
>>>>>>> 8b3ef5c1ea72b575c0dfd215c06b7dc78da8357b



