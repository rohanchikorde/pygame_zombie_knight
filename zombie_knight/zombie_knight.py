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

    def __init__(self, x, y, image, main_group, sub_group=''):
        """Initialize the tile"""
        super().__init__()
        # load in the correct image and add it to the correct sub group
        if image_int == 1:
            self.image = pygame.transform.scale(pygame.image.load('images/tiles/Tile (1).png'), (32, 32))
            # platform tiles
        elif image_int == 2:
            self.image = pygame.transform.scale(pygame.image.load('images/tiles/Tile (2).png'), (32, 32))
            sub_group.add(self)
        elif image_int == 3:
            self.image = pygame.transform.scale(pygame.image.load('images/tiles/Tile (3).png'), (32, 32))
            sub_group.add(self)
        elif image_int == 4:
            self.image = pygame.transform.scale(pygame.image.load('images/tiles/Tile (4).png'), (32, 32))
            sub_group.add(self)
        elif image_int == 5:
            self.image = pygame.transform.scale(pygame.image.load('images/tiles/Tile (5).png'), (32, 32))
            sub_group.add(self)

        # add every tile to the main group
        main.group.add(self)

        # get the


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

    def animate(self):
        """Animate the player's action"""
        pass


class RubyMaker(pygame.sprite.Sprite):
    """A tile that is animated. A ruby will be generated here"""

    def __init__(self):
        """Initialize the ruby maker"""
        pass

    def update(self):
        """update the ruby maker"""
        pass

    def animate(self):
        """Animate the ruby maker"""
        pass


class Ruby(pygame.sprite.Sprite):
    """A class the player must collect to earn points and health"""

    def __init__(self):
        """Initialize the ruby"""
        pass

    def update(self):
        """Update the ruby"""
        pass

    def move(self):
        """Move the ruby"""
        pass

    def check_collisions(self):
        """Check for collisions with platforms and portals"""
        pass

    def animate(self):
        """Animate the ruby"""
        pass


class Portal(pygame.sprite.Sprite):
    """A class that if collided with transport you"""

    def __init__(self):
        """Initialize the portal"""
        pass

    def update(self):
        """update the portal"""
        pass

    def animate(self):
        """Animate the portal"""
        pass


# create sprite groups
my_main_tile_group = pygame.sprite.Group()
my_platform_group = pygame.sprite.Group()
my_player_group = pygame.sprite.Group()
my_bullet_group = pygame.sprite.Group()
my_zombie_group = pygame.sprite.Group()
my_portal_group = pygame.sprite.Group()
my_ruby_group = pygame.sprite.Group()

# create the tile map
# 0 - no tile
# 1 - dirt, 2-5 - platform
# 23 rows and 40 columns
tile_map = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8, 0],
    [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 0, 0, 0, 0, 6, 0, 0, 0, 0, 0, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [4, 4, 4, 4, 4, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 4, 4, 4, 4, 4],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 0, 0, 0, 0, 0, 0, 0, 0, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 4, 4, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 0],
    [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

# Generate tile object from the tile map
# loop through thr 23 rows
for i in range(len(tile_map)):
    # loop through the 40 elements in a given list (cols)
    for j in range(len(tile_map[i])):
        # dirt tile
        if tile_map[i][j] == 1:
            Tile(j*32, i*32, 1, my_main_tile_group)
        elif tile_map[i][j] == 2:
            Tile(j*32, i*32, 2, my_main_tile_group, my_platform_group)
        elif tile_map[i][j] == 3:
            Tile(j*32, i*32, 3, my_main_tile_group, my_platform_group)
        elif tile_map[i][j] == 4:
            Tile(j*32, i*32, 4, my_main_tile_group, my_platform_group)
        elif tile_map[i][j] == 5:
            Tile(j*32, i*32, 5, my_main_tile_group, my_platform_group)
        # Ruby maker
        elif tile_map[i][j] == 7:
            pass
        elif tile_map[i][j] == 8:
            pass
        elif tile_map[i][j] == 9:
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
