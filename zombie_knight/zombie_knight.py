import pygame, random
# use 2d vectos
vector = pygame.math.Vector2

# Initialize pygame
pygame.init()

# set display surface (tile size is 32 x 32 so 1280/32 = 40 tiles wide, 736/32 = 23 tiles high )
WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 736
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Zombie Knight')

# set FPS and clock
FPS = 60
clock = pygame.time.Clock()


# Define classes
class Game:
    "A class to help manage gameplay"

    def __init__(self):
        """Initialize the game"""
        pass

    def update(self):
        """Update the game"""
        pass

    def draw(self):
        """Draw the game HUD"""
        pass

    def add_zombie(self):
        """Add a zombie to the game"""
        pass

    def check_collision(self):
        """Check collisions that affect the game play"""
        pass

    def check_round_completion(self):
        """Check if the player survived a single night"""
        pass

    def check_game_over(self):
        """Check to see if the player lost the game"""
        pass

    def start_new_round(self):
        """Start a new night"""
        pass

    def pause_game(self):
        """Pause the game"""
        pass

    def reset_game(self):
        """Reset the game"""
        pass


class Tile(pygame.sprite.Sprite):
    """A class to represent a 32 x 32 pixel area in our display"""

    def __init__(self):
        """Initialize the tile"""
        pass


class Player(pygame.sprite.Sprite):
    """A class the user can control"""

    def __init__(self):
        """Initialize the class"""
        pass

    def update(self):
        """UPdat the player"""
        pass

    def move(self):
        """Move the player"""
        pass

    def check_collisions(self):
        """Check for collisions with platform and portal"""
        pass

    def check_animations(self):
        """Check to see if the jump/fire animation should run"""
        pass

    def jump(self):
        """Jump upwards if on a platform"""
        pass

    def fire(self):
        """Fire a bullet from a sword"""
        pass

    def reset(self):
        """Reset the player's position"""
        pass

    def animate(self):
        """Animate the player's action"""
        pass


class Bullet(pygame.sprite.Sprite):
    """A projectile launched by the player"""

    def __init__(self):
        """Initialize the class Bullet"""
        pass

    def update(self):
        """Update the bullet"""
        pass


class Zombie(pygame.sprite.Sprite):
    """An enemy class that moves across the screen"""

    def __init__(self):
        """Initialize Zombie class"""
        pass

    def update(self):
        """Update the Zombie"""
        pass

    def move(self):
        """Move the Zomie"""
        pass

    def check_collisions(self):
        """Check for collisions with platform and portal"""
        pass

    def check_animations(self):
        """Check to see if the death/rise animation should run"""
        pass

    def reset(self):
        """Reset the player's position"""
        pass

    def animate(self):
        """Animate the player's action"""
        pass



# load in a background image
background_image = pygame.transform.scale(pygame.image.load('images/background.png'), (1280, 736))
background_rect = background_image.get_rect()
background_rect.topleft = (0, 0)

# the main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # blit the background
    display_surface.blit(background_image, background_rect)

    # update the display and tick the clock
    pygame.display.update()
    clock.tick(FPS)

# end the game
pygame.quit()
