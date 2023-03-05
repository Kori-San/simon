from Board import Board
import pygame

class Game:

    # Setting the variables to the default values.
    running = True
    sequence = []

    def __init__(self, resolution) -> None:
        """
        `__init__` is a function that is called when an object is created
        
        :param resolution: The resolution of the screen
        """
        # Setting the resolution of the screen.
        self.resolution = resolution

    def setup(self) -> None:
        """
        It sets up the game
        """
        # It initializes the pygame module.
        pygame.init()
        
        # Setting the screen and the board.
        self.screen = pygame.display.set_mode(self.resolution, pygame.DOUBLEBUF)
        self.screen.set_alpha(None)
        self.board = Board(self.screen)

        # Setting the fps of the game to 60.
        self.fps = 60
        self.clock = pygame.time.Clock()

        # Setting the icon of the game.
        self.logo = pygame.image.load("assets/icon/logo.png").convert_alpha()
        pygame.display.set_icon(self.logo)

        # It sets the title of the window.
        self.caption = "Simon"
        pygame.display.set_caption(self.caption)
    
    def launch(self) -> None:
        """
        It sets up the game and then runs the main loop
        """
        # Calling the setup function.
        self.setup()

        # The main loop of the game.
        while self.running:
            
            # Setting the mode of all the keys to False.
            for key in self.board.keys:
                key.set_mode(False)
            
            # Checking if the user has clicked the close button.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
            
                # Checking if the user has pressed the F1 key. If the user has pressed the F1 key, then it will
                # display the hitboxes of the keys.
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_F1:
                        for key in self.board.keys:
                            key.hitbox()

                # Checking if the user has clicked on the screen. If the user has clicked on the screen, then it will
                # check if the user has clicked on a key.
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos_x, pos_y = pygame.mouse.get_pos()
                    for key in self.board.keys:
                        if key.touched(pos_x, pos_y):
                            print("Touch " + key.color.capitalize())
                            break

            # Updating the screen.
            self.clock.tick(self.fps)
            self.board.display()