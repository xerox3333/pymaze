import pygame
from Wall import Wall
from Boxes import Boxes

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
PURPLE = (255, 0, 255)


class Level(object):
    """ Base class for all levels """
    wall_list = None
    obsticles = None

    def __init__(self):
        self.wall_list = pygame.sprite.Group()
        self.obsticles = pygame.sprite.Group()


class Level1(Level):
    """ First level """
    def __init__(self):
        
        super(Level1, self).__init__()  # Call the Level super class constructor aka (Level.__init__(self))

        # Define the walls of the first level
        walls = [[0, 0, 20, 250, WHITE],
                 [0, 350, 20, 250, WHITE],
                 [780, 0, 20, 250, WHITE],
                 [780, 350, 20, 250, WHITE],
                 [20, 0, 760, 20, WHITE],
                 [20, 580, 760, 20, WHITE],
                 [390, 50, 20, 500, WHITE]]

        obsticles = [[100, 150, 15, 15, RED]]

        # Loop through the walls for the level and add objects to the main wall list
        for thiswall in walls:
            wall = Wall(thiswall[0], thiswall[1], thiswall[2], thiswall[3], thiswall[4])
            self.wall_list.add(wall)

        for thisObsticle in obsticles:
            box = Boxes(thisObsticle[0], thisObsticle[1], thisObsticle[2], thisObsticle[3], thisObsticle[4])
            self.obsticles.add(box)


class Level2(Level):
    """This creates all the walls in room 2"""
    def __init__(self):
        super(Level2, self).__init__()  # Call the Level super class constructor

        # Define the walls of the second level
        walls = [[0, 0, 20, 250, RED],
                 [0, 350, 20, 250, RED],
                 [780, 0, 20, 250, RED],
                 [780, 350, 20, 250, RED],
                 [20, 0, 760, 20, RED],
                 [20, 580, 760, 20, RED],
                 [190, 50, 20, 500, GREEN],
                 [590, 50, 20, 500, GREEN]]

        for item in walls:
            wall = Wall(item[0], item[1], item[2], item[3], item[4])
            self.wall_list.add(wall)


class Level3(Level):
    """This creates all the walls in room 3"""
    def __init__(self):
        super(Level3, self).__init__()

        walls = [[0, 0, 20, 250, PURPLE],
                 [0, 350, 20, 250, PURPLE],
                 [780, 0, 20, 250, PURPLE],
                 [780, 350, 20, 250, PURPLE],
                 [20, 0, 760, 20, PURPLE],
                 [20, 580, 760, 20, PURPLE]]

        for item in walls:
            wall = Wall(item[0], item[1], item[2], item[3], item[4])
            self.wall_list.add(wall)

        for x in range(100, 800, 100):
            for y in range(50, 450, 300):
                wall = Wall(x, y, 20, 200, RED)
                self.wall_list.add(wall)

        for x in range(150, 700, 100):
            wall = Wall(x, 200, 20, 200, WHITE)
            self.wall_list.add(wall)

        for x in range(20, 800, 50):
            wall = Wall(x, 20, 200, 20, BLUE)
            self.wall_list.add(wall)


class Level4(Level):
    def __init__(self):
        super(Level4, self).__init__()

        walls = [[0, 0, 20, 400, BLUE],
                 [0, 500, 20, 100, BLUE],
                 [780, 0, 20, 250, BLUE],
                 [780, 350, 20, 350, BLUE],
                 [20, 0, 760, 20, BLUE],
                 [20, 580, 760, 20, BLUE]]

        for item in walls:
            wall = Wall(item[0], item[1], item[2], item[3], item[4])
            self.wall_list.add(wall)
