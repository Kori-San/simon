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

        # It's loading the image of the key and the sound of the key.
        self.sprite = pygame.image.load("assets/keys/off/" + self.color + ".png").convert_alpha()

        # It's loading the sound of the key.
        self.sound = pygame.mixer.Sound("sound/" + self.color + ".wav")
            
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

    def activate(self) -> None:
        """
        It's setting the key to on mode and playing the sound of the key
        """
        # It's setting the key to on mode and playing the sound of the key.
        self.set_mode(True)
        pygame.mixer.Sound.play(self.sound)
        
    def touched(self, pos_x, pos_y) -> bool:
        """
        It checks if the mouse is within the key's hitbox. If it is, it returns
        True. If it isn't, it returns False
        
        :param pos_x: The x position of the mouse
        :param pos_y: The y position of the mouse
        :return: a boolean value.
        """
        # It's checking if the mouse is within the key's hitbox.
        if self.x < pos_x < (self.x + self.width) and self.y < pos_y < (self.y + self.height):
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