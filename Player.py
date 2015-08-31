import pygame

WHITE = (255, 255, 255)


class Player(pygame.sprite.Sprite):

    def __init__(self, x, y):
        super(Player, self).__init__()  # Calls the init method of the class Player extends (pygame.sprite.Sprite)
        self.image = pygame.Surface([15, 15])  # Create the visible square for the player object
        self.image.fill(WHITE)  # Fill player in white

        # Initialize some variables for the player instance
        self.change_x = 0
        self.change_y = 0
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x

    def changeSpeed(self, x, y):
        """ Update the players velocity """
        self.change_x += x
        self.change_y += y

    def move(self, walls, boxes):
        """ Move the player object and check for wall collisions """
        self.rect.x += self.change_x  # Add the change to the players horizontal vector
        wallobjects = pygame.sprite.spritecollide(self, walls, False)  # Create a list of collidable walls
        boxobjects = pygame.sprite.spritecollide(self, boxes, False)  # Create a list of collidable boxes

        for collidable in wallobjects:
            if self.change_x > 0:  # Moving Right
                self.rect.right = collidable.rect.left  # Set the players Right to the position of the walls Left
            else:
                self.rect.left = collidable.rect.right  # Set the players Left to the position of the walls Right

        for collidable in boxobjects:
            if self.change_x > 0:  # If player is moving right
                collidable.rect.x = (self.rect.x + 15)  # Set the boxes x ahead of the player
            else:
                collidable.rect.x = (self.rect.x - 15)

        self.rect.y += self.change_y  # Add the change to the players vertical vector
        wallobjects = pygame.sprite.spritecollide(self, walls, False)  # Create a list of collidable walls
        boxobjects = pygame.sprite.spritecollide(self, boxes, False)  # Create a list of collidable boxes

        for collidable in wallobjects:
            if self.change_y > 0:  # Moving Down
                self.rect.bottom = collidable.rect.top  # Set the players Bottom to the position of the walls top
            else:
                self.rect.top = collidable.rect.bottom  # Set the players Top to the position of the players bottom

        for collidable in boxobjects:
            if self.change_y > 0:  # If player is moving Down
                collidable.rect.y = (self.rect.y + 15)  # Set the boxes y ahead of the player
            else:
                collidable.rect.y = (self.rect.y - 15)



