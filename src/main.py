import pygame
from constants import *
from scenes.intro import Intro

# Initialisation de pygame et de différentes variables
pygame.init()
pygame.display.set_caption("Shoot clash")

pygame.mixer.init()  # Initialise le son
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()  # Horloge du jeu (limite les fps)
current_scene = Intro(screen)
running = True
pygame.mixer.music.load("assets/sounds/music/music_pirate.wav")
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.3)


# Boucle principal
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Limite à 60 fps et retourne le temps entre deux frames
    elapsed = clock.tick(MAX_FPS)

    if current_scene.is_finished == True:
        current_scene = current_scene.next_scene

    current_scene.update(elapsed)
    current_scene.draw()

    pygame.display.update()
  