import pygame


class Wall(pygame.sprite.Sprite):
    """ Represents the walls in the game """

    def __init__(self, x, y, width, height, color):
        super(Wall, self).__init__()

        self.image = pygame.Surface([width, height])
        self.image.fill(color)

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y