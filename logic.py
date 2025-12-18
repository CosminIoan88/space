import random

import pygame

from models import Meteor


class Game:
    def __init__(self, screen_width=900, screen_height=500):
        pygame.init()
        self.width = screen_width
        self.height = screen_height

        self.window = pygame.display.set_mode((self.width, self.height))
        self.clock = pygame.time.Clock()
        pygame.display.set_caption("Space fight")
        self.fps = 60

        # Initializari pentru joc
        self.all_objects = []
        self.meteors = []

        self.prepare_game()

    def addMeteor(self):
        m = Meteor(random.randint(0, self.width), random.randint(0, self.height))
        self.all_objects.append(m)
        self.meteors.append(m)

    def removeMeteor(self, meteor):
        if meteor in self.all_objects:
            self.all_objects.remove(meteor)
        if meteor in self.meteors:
            self.meteors.remove(meteor)

    def prepare_game(self):
        self.all_objects = []
        self.meteors = []
        for i in range(3):
            self.addMeteor()

    def run(self):
        is_Running = True
        while is_Running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    is_Running = False
                    self.quit()

            # update all objects
            for obj in self.all_objects:
                obj.update()

            # Clear screen
            self.window.fill((0, 0, 0))

            # draw all objects
            for obj in self.all_objects:
                obj.draw(self.window)

            # update screen and limit fps
            pygame.display.update()
            self.clock.tick(self.fps)

    def quit(self):
        pygame.quit()
