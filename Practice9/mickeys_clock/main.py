import pygame
from clock import MickeyClock

pygame.init()

WIDTH = 800
HEIGHT = 700

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mickey's Clock")

clock = pygame.time.Clock()

mickey_clock = MickeyClock()

running = True

while running:
    screen.fill((255, 255, 255))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    mickey_clock.draw(screen)

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
