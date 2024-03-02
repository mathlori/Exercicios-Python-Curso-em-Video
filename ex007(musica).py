import pygame
from pygame.locals import *
pygame.init()
tela = pygame.display.set_mode((400, 400))
musica = pygame.mixer.music.load("tv.mp3")
pygame.mixer.music.play(-1) #coloquei -1 para ficar em loop
while True:
  for event in pygame.event.get():
    if event.type == QUIT:
      pygame.quit()
  pygame.display.update()