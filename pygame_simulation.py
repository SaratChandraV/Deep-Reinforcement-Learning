import pygame
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 400, 300
PLAYER_WIDTH, PLAYER_HEIGHT = 20, 20
OBSTACLE_WIDTH, OBSTACLE_HEIGHT = 20, 20
PLAYER_COLOR = (0, 255, 0)
OBSTACLE_COLOR = (255, 0, 0)
BACKGROUND_COLOR = (0, 0, 0)
JUMP_HEIGHT = 80
GRAVITY = 150
FPS = 30

# Create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Jumping Game")

# Player attributes
player_x = 50
player_y = HEIGHT - PLAYER_HEIGHT
player_jump = False
player_jump_height = 0
player_velocity_up = 0

# Obstacle attributes
obstacles = []
obstacle_speed = 5
obstacle_spawn_timer = 0
obstacle_spawn_interval = 60

# Game loop
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q and not player_jump:
                player_jump = True
                player_velocity_up = 100

    player_y = player_y - player_velocity_up * 1 / FPS
    player_velocity_up = player_velocity_up - GRAVITY * 1 / FPS

    # Ensure player doesn't go below the ground
    if player_y >= HEIGHT - PLAYER_HEIGHT:
        player_y = HEIGHT - PLAYER_HEIGHT
        player_jump = False

    # Generate obstacles
    obstacle_spawn_timer += 1
    if obstacle_spawn_timer >= obstacle_spawn_interval:
        obstacle_x = WIDTH
        obstacle_y = HEIGHT - OBSTACLE_HEIGHT
        obstacles.append(pygame.Rect(obstacle_x, obstacle_y, OBSTACLE_WIDTH, OBSTACLE_HEIGHT))
        obstacle_spawn_timer = 0

    # Move and draw obstacles
    for obstacle in obstacles:
        obstacle.x -= obstacle_speed

    # Remove obstacles that are off the screen
    obstacles = [obstacle for obstacle in obstacles if obstacle.x + OBSTACLE_WIDTH > 0]

    # Check for collisions with obstacles
    player_rect = pygame.Rect(player_x, player_y, PLAYER_WIDTH, PLAYER_HEIGHT)
    for obstacle in obstacles:
        if player_rect.colliderect(obstacle):
            running = False
            pass

    # Clear the screen
    screen.fill(BACKGROUND_COLOR)

    # Draw the player
    pygame.draw.rect(screen, PLAYER_COLOR, (player_x, player_y, PLAYER_WIDTH, PLAYER_HEIGHT))

    # Draw the obstacles
    for obstacle in obstacles:
        pygame.draw.rect(screen, OBSTACLE_COLOR, obstacle)

    pygame.display.flip()

    # Control the frame rate
    clock.tick(FPS)

# Quit the game
pygame.quit()