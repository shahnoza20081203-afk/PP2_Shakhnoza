import pygame
import math
import os
from datetime import datetime


class MickeyClock:
    def __init__(self):
        self.base_dir = os.path.dirname(os.path.abspath(__file__))
        self.image_dir = os.path.join(self.base_dir, "images")

        self.minute_image = pygame.image.load(
            os.path.join(self.image_dir, "mickey_hand.png")
        ).convert_alpha()

        self.second_image = pygame.image.load(
            os.path.join(self.image_dir, "mickey_hand2.png")
        ).convert_alpha()

        self.minute_image = pygame.transform.smoothscale(
            self.minute_image, (55, 230)
        )

        self.second_image = pygame.transform.smoothscale(
            self.second_image, (45, 190)
        )

        self.center = (400, 350)
        self.radius = 220

        self.font = pygame.font.SysFont("Arial", 35)
        self.time_font = pygame.font.SysFont("Arial", 24)

    def draw_face(self, screen):
        pygame.draw.circle(
            screen, (0, 0, 0), self.center, self.radius, 5
        )

        for number in range(1, 13):
            angle = math.radians(number * 30 - 90)

            x = self.center[0] + 175 * math.cos(angle)
            y = self.center[1] + 175 * math.sin(angle)

            text = self.font.render(str(number), True, (0, 0, 0))
            rect = text.get_rect(center=(x, y))

            screen.blit(text, rect)

        pygame.draw.circle(screen, (220, 40, 40), self.center, 12)

    
    def draw_hand(self, screen, image, angle):
        # Rotate the hand image
        rotated_image = pygame.transform.rotate(image, -angle)

        # Original pivot: top center of the image
        pivot = pygame.math.Vector2(
            image.get_width() / 2,
            0
        )

        # Position of the clock center
        center = pygame.math.Vector2(self.center)

        # Calculate the new pivot after rotation
        rotated_pivot = pygame.math.Vector2(
            rotated_image.get_rect().center
        ) + (pivot - pygame.math.Vector2(
            image.get_rect().center
        )).rotate(angle)

        # Draw image at the correct position
        rect = rotated_image.get_rect(
            center=(center.x, center.y)
        )

        rect.center = (
            center.x + rotated_pivot.x - rotated_image.get_width() / 2,
            center.y + rotated_pivot.y - rotated_image.get_height() / 2
        )

        screen.blit(rotated_image, rect)


    def draw(self, screen):
        now = datetime.now()

        minutes = now.minute
        seconds = now.second

        minute_angle = minutes * 6
        second_angle = seconds * 6

        self.draw_face(screen)

        self.draw_hand(
            screen, self.minute_image, minute_angle
        )

        self.draw_hand(
            screen, self.second_image, second_angle
        )

        time_text = self.time_font.render(
            now.strftime("%H:%M:%S"),
            True,
            (30, 30, 30)
        )

        time_rect = time_text.get_rect(
            center=(self.center[0], 650)
        )

        screen.blit(time_text, time_rect)
