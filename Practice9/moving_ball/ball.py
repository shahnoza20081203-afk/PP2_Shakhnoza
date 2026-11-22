import pygame

class Ball:
    def __init__(self):
        self.x = 800 // 2
        self.y = 600 // 2
        self.radius = 25
        self.speed = 20

    def move(self, keys, width, height):

        if keys[pygame.K_LEFT]:
            self.x -= self.speed

        if keys[pygame.K_RIGHT]:
            self.x += self.speed

        if keys[pygame.K_UP]:
            self.y -= self.speed

        if keys[pygame.K_DOWN]:
            self.y += self.speed

        self.x = max(
            self.radius,
            min(self.x, width - self.radius)
        )

        self.y = max(
            self.radius,
            min(self.y, height - self.radius)
        )

    def draw(self, screen):
        pygame.draw.circle(
            screen,
            (255, 0, 0),
            (self.x, self.y),
            self.radius
        )
