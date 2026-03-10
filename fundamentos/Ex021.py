#Tocador MP3

#import pygame
#pygame.mixer.init()
#musica=r"C:\Users\vinic\Music\musica.mp3"
#pygame.mixer.music.load(musica)
#pygame.mixer.music.play()
#while pygame.mixer.music.get_busy():
#    pass

from pygame import mixer
mixer.init()
mixer.music.load('musica.mp3')
mixer.music.play()
while mixer.music.get_busy() :
    pass









