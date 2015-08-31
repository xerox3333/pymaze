import pygame


class Boxes(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, color):
        super(Boxes, self).__init__()
        self.image = pygame.Surface([width, height])  # Create the box surface
        self.image.fill(color)  # Add a fill color to contrast with background

        # Initialize some variables for the instance
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

