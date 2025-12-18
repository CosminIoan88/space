import math
import random

import pygame


class GameObject:
    def __init__(self):
        self.image = None
        self.rect = pygame.Rect(0, 0, 0, 0)

    def update(self):
        pass

    def draw(self, window):
        if self.image:
            window.blit(self.image, (self.rect.x, self.rect.y))


class Bounded:
    def __init__(self, x, y, width, height):
        self.bounds = pygame.Rect(x, y, width, height)


class Meteor(GameObject):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        pygame.draw.rect(self.image, (200, 0, 0), (0, 0, 50, 50))
        self.rect = pygame.Rect(x, y, 50, 50)
        self.dir = (
            math.cos(random.uniform(0, 2 * math.pi)),
            math.sin(random.uniform(0, 2 * math.pi)),
        )

    def update(self):
        self.rect.x += self.dir[0] * 2
        self.rect.y += self.dir[1] * 2

        if self.rect.right < 0:
            self.rect.left = 900
        elif self.rect.left > 900:
            self.rect.right = 0
        if self.rect.bottom < 0:
            self.rect.top = 500
        elif self.rect.top > 500:
            self.rect.bottom = 0


class Spaceship(GameObject, Bounded):
    pass


class Bullet(GameObject):
    pass
