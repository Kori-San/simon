import pygame

class Key:

    # It's setting the debug variable to False.
    debug = False

    # It's setting the width, height, x, and y of the key.
    width = 320
    height = 320
    x = 0
    y = 0

    def __init__(self, color) -> None:
        """
        It sets the color of the key to the color that was passed in, and it loads the image of the key
        
        :param color: The color of the key
        """
        # It sets the color of the key to the color that was passed in.
        self.color = color

        # It loads the image of the key
        self.sprite = pygame.image.load("assets/keys/off/" + self.color + ".png").convert_alpha()
    
    def set_mode(self, mode):
        """
        If the mode is on, then the sprite is set to the on version of the key, otherwise it's set to the
        off version
        
        :param mode: Whether the key is on or off
        """
        # Setting the sprite to the on or off version of the key.
        on_off = "on" if mode else "off"
        self.sprite = pygame.image.load("assets/keys/" + on_off + "/" + self.color + ".png").convert_alpha()
    
    def set_position(self, x, y) -> None:
        """
        It sets the x and y position of the key
        
        :param x: The x position of the key
        :param y: The y position of the key
        """
        # It sets the x and y position of the key.
        self.x = x
        self.y = y

    def touched(self, pos_x, pos_y) -> bool:
        """
        It checks if the mouse is within the key's hitbox. If it is, it sets the key to on mode and returns
        True. If it isn't, it returns False
        
        :param pos_x: The x position of the mouse
        :param pos_y: The y position of the mouse
        :return: a boolean value.
        """
        # It checks if the mouse is within the key's hitbox. If it is, it sets the key to on mode and returns
        # True. If it isn't, it returns False.
        if self.x < pos_x < (self.x + self.width) and self.y < pos_y < (self.y + self.height):
            self.set_mode(True)
            return True
        else:
            return False

    def hitbox(self) -> None:
        """
        If the debug variable is True, set it to False, otherwise set it to True
        """
        # A toggle. If debug is True, it sets it to False. If debug is False, it sets it to True.
        if self.debug:
            self.debug = False
        else:
            self.debug = True