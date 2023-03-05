from Key import Key
import pygame

class Board:

    # Creating an empty list for the background and keys.
    background = []
    keys = []

    def __init__(self, screen) -> None:
        """
        It loads the images for the background and creates the keys.
        
        :param screen: The screen that the game is being played on
        """
        # Setting the screen to the screen that the game is being played on.
        self.screen = screen

        # Loading the images for the background and appending them to the background list.
        for element in [ "background", "grid", "base"]:
            temp_image = pygame.image.load("assets/base/" + element + ".png").convert_alpha()
            self.background.append(temp_image)

        # Creating a key for each color and adding it to the list of keys.
        for color in [ "yellow", "blue", "red", "green" ]:
            self.keys.append(Key(color))

        ## Values (in pixels) extracted from Photoshop 
        # Yellow Key has an x of 119 and a y of 129
        # Blue Key has an x of 561 and a y of 129
        # Red Key has an x of 119 and a y of 551
        # Green Key has an x of 561 and a y of 551

        # Setting the position of the keys.
        count = 0
        for y in [129, 551]:
            for x in [119, 561]:
                self.keys[count].set_position(x, y)
                count += 1

    def display(self):
        """
        It draws the background and the keys to the screen
        """
        # Drawing the background to the screen.
        for element in self.background:
            self.screen.blit(element, (0,0))
        
        # Drawing the keys to the screen.
        for key in self.keys:
            self.screen.blit(key.sprite, (0,0))
            if key.debug:
                    pygame.draw.rect(self.screen, (255,0,0), pygame.Rect(key.x - 1, key.y - 1, key.width + 1, key.height + 1), 2)

        # It updates the screen.
        pygame.display.flip()