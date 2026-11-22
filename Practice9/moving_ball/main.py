import pygame
from ball import Ball

pygame.init()

WIDTH = 800
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Moving Ball")

WHITE = (255, 255, 255)

clock = pygame.time.Clock()

ball = Ball()

running = True

while running:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    ball.move(keys, WIDTH, HEIGHT)

    ball.draw(screen)

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
