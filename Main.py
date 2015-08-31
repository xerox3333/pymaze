import pygame
import Level
from Player import Player

BLACK = (0, 0, 0)


class Main(object):

    def main():
        """ Main program """
        WIDTH, HEIGHT = 800, 600

        # Initialize pygame
        pygame.init()
        myfont = pygame.font.SysFont("monospace", 15)

        # Set screen dimensions
        screen = pygame.display.set_mode([WIDTH, HEIGHT])

        # Create the player
        player = Player(50, 50)
        movingsprites = pygame.sprite.Group()
        movingsprites.add(player)

        # Initialize the game map
        levels = []

        level = Level.Level1()
        levels.append(level)
        level = Level.Level2()
        levels.append(level)
        level = Level.Level3()
        levels.append(level)
        level = Level.Level4()
        levels.append(level)

        currentLevelNo = 0
        currentLevel = levels[currentLevelNo]

        clock = pygame.time.Clock()

        quit = False
        # Main game loop to check user input
        while not quit:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        player.changeSpeed(-5, 0)
                    if event.key == pygame.K_RIGHT:
                        player.changeSpeed(5, 0)
                    if event.key == pygame.K_UP:
                        player.changeSpeed(0, -5)
                    if event.key == pygame.K_DOWN:
                        player.changeSpeed(0, 5)

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT:
                        player.changeSpeed(5, 0)
                    if event.key == pygame.K_RIGHT:
                        player.changeSpeed(-5, 0)
                    if event.key == pygame.K_UP:
                        player.changeSpeed(0, 5)
                    if event.key == pygame.K_DOWN:
                        player.changeSpeed(0, -5)

            # Game Logic
            player.move(currentLevel.wall_list, currentLevel.obsticles)

            if player.rect.x < -15:
                if currentLevelNo == 0:
                    currentLevelNo = 3
                    currentLevel = levels[currentLevelNo]
                    player.rect.x = 790
                elif currentLevelNo == 3:
                    currentLevelNo = 2
                    currentLevel = levels[currentLevelNo]
                    player.rect.x = 790
                    player.rect.y = 285
                elif currentLevelNo == 2:
                    currentLevelNo = 1
                    currentLevel = levels[currentLevelNo]
                    player.rect.x = 790
                else:
                    currentLevelNo = 0
                    currentLevel = levels[currentLevelNo]
                    player.rect.x = 790

            if player.rect.x > 801:
                if currentLevelNo == 0:
                    currentLevelNo = 1
                    currentLevel = levels[currentLevelNo]
                    player.rect.x = 0
                elif currentLevelNo == 1:
                    currentLevelNo = 2
                    currentLevel = levels[currentLevelNo]
                    player.rect.x = 0
                elif currentLevelNo == 2:
                    currentLevelNo = 3
                    currentLevel = levels[currentLevelNo]
                    player.rect.x = 0
                    player.rect.y = 425
                else:
                    currentLevelNo = 0
                    currentLevel = levels[currentLevelNo]
                    player.rect.x = 0

            screen.fill(BLACK)
            label = myfont.render("Level: %s" % (currentLevelNo + 1), 1, (255, 255, 0))
            screen.blit(label, (25, 50))

            movingsprites.draw(screen)
            currentLevel.wall_list.draw(screen)
            currentLevel.obsticles.draw(screen)

            pygame.display.flip()

            clock.tick(60)

        pygame.quit()

    if __name__ == '__main__':
        main()
