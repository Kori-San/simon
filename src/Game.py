from Board import Board
import pygame
import random

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

        # Initializing the mixer and setting the volume of the music to 25%.
        pygame.mixer.init()
        pygame.mixer.music.set_volume(0.25)

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

        # A variable that is used as an index for the sequence array
        sequence_count = 0
        
        # Generate the first key of the sequence
        self.generate_seq()

        # The main loop of the game.
        while self.running:

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

                # Checking if the user has clicked on the screen.
                if event.type == pygame.MOUSEBUTTONDOWN:
                    # Getting the position of the mouse.
                    pos_x, pos_y = pygame.mouse.get_pos()
                    # If the key is touched it will activate the key that the user has clicked on.
                    for key in self.board.keys:
                        if key.touched(pos_x, pos_y):
                            key.activate()
                            print("Touch " + key.color.capitalize())

                            # If a the key being pressed is the same color as the key currently in queue in the sequence
                            if key.color == self.sequence[sequence_count].color:
                                # If it is the last key to be pressed on
                                if sequence_count == len(self.sequence) - 1:
                                    # Add a new key and reset sequence counter
                                    self.generate_seq()
                                    sequence_count = 0
                                # If it is not the last key then increase the sequence counter
                                else:
                                    sequence_count += 1
                            else:
                                print("\n---\nGame Over!\nMaximum Score:", len(self.sequence) - 1)
                                return

                            break

            # Updating the screen.
            self.clock.tick(self.fps)
            self.board.display()
            
            # Setting the mode of all the keys to False.
            for key in self.board.keys:
                key.set_mode(False)
    
    def generate_seq(self):
        # First display to avoid black screen causing the player not being  able to see the first key of the first sequence.
        self.board.display()
        
        # Disable all keys 
        for key in self.board.keys:
            key.set_mode(False)
        
        # Second display to show a toggled off gameboard (with no key on)
        self.board.display()

        # Big wait to make people understand that the sequence is going to be played
        pygame.time.wait(1000)

        # Generate a new key using randint and appending it to the sequence
        new_key = self.board.keys[random.randint(0,3)]
        self.sequence.append(new_key)
        
        # Play the whole sequence
        for key in self.sequence:
            # Activate the key and show it's activation the wait
            key.activate()
            self.board.display()
            pygame.time.wait(500)
            
            # Disable the key and refresh display
            key.set_mode(False)
            self.board.display()