import pygame
import sys

# --- 1. INITIALIZATION AND SETUP ---
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Pygame Platformer Prototype")

# Colors
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)

# Clock to control frame rate
clock = pygame.time.Clock()
FPS = 120

# --- 2. PLAYER CLASS (THE HERO) ---
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([30, 50]) # Player size (width, height)
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        
        # Initial position (start near the bottom left)
        self.rect.x = 50
        self.rect.y = SCREEN_HEIGHT - 100 

        # Physics variables
        self.speed = 5
        self.gravity = 1
        self.vertical_velocity = 0
        self.on_ground = True
        self.jump_strength = 20

    def apply_gravity(self):
        """Increases the downward velocity of the player."""
        self.vertical_velocity += self.gravity
        self.rect.y += self.vertical_velocity

        # If the player falls off the screen, reset them (or handle death)
        if self.rect.bottom > SCREEN_HEIGHT:
             self.rect.bottom = SCREEN_HEIGHT - 10 # Simple respawn
             self.vertical_velocity = 0
             self.on_ground = True


    def move(self, keys):
        """Handles horizontal movement and jumping."""
        
        # 1. Horizontal Movement
        dx = 0
        if keys[pygame.K_LEFT]:
            dx = -self.speed
        if keys[pygame.K_RIGHT]:
            dx = self.speed
        
        self.rect.x += dx
        
        # Keep player within screen boundaries
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH

        # 2. Jumping
        if keys[pygame.K_SPACE] and self.on_ground:
            self.vertical_velocity = -self.jump_strength
            self.on_ground = False

    def update(self):
        """The main update function called every frame."""
        self.apply_gravity()
        
        # Basic Ground Collision Detection (Simple floor)
        # If the player falls below the floor, set them to the floor and stop falling.
        floor_y = SCREEN_HEIGHT - 50
        if self.rect.bottom >= floor_y:
            self.rect.bottom = floor_y
            self.vertical_velocity = 0
            self.on_ground = True
        
        # The horizontal movement is handled in the main loop's key check
        # (We keep the 'move' function separate to pass the key state easily)

# --- 3. LEVEL/WORLD SETUP ---
# We will create a simple platform object
class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

# --- 4. GAME LOOP ---
def run_game():
    # Setup game sprites
    all_sprites = pygame.sprite.Group()
    platform_group = pygame.sprite.Group()
    
    # Create the player
    player = Player()
    all_sprites.add(player)

    # Create the ground platform (The primary floor)
    ground = Platform(0, SCREEN_HEIGHT - 50, SCREEN_WIDTH, 50)
    platform_group.add(ground)
    all_sprites.add(ground)

    running = True
    while running:
        # 1. Event Handling (Checking if keys are pressed or released)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            # If we were to check key press down/up here, we could detect actions.
            
        keys = pygame.key.get_pressed()
        
        # 2. Update Logic
        
        # Player movement (Handles horizontal motion and jumping)
        player.move(keys)
        
        # Player gravity/physics update
        player.update() 

        # 3. Drawing (Rendering the frame)
        screen.fill(BLACK) # Clear the screen every frame
        
        platform_group.draw(screen) # Draw the platform
        all_sprites.draw(screen)   # Draw the player (and ground)
        
        # Update the screen display
        pygame.display.flip()

        # 4. Control Speed
        clock.tick(FPS)

    # Quit Pygame when the loop ends
    pygame.quit()
    sys.exit()

if __name__ == '__main__':
    run_game()