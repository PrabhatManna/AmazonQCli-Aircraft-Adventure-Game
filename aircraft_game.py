import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Game window settings
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Aircraft Adventure")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
SKY_BLUE = (135, 206, 235)

# Player settings
player_width = 50
player_height = 40
player_x = WIDTH // 2 - player_width // 2
player_y = HEIGHT - player_height - 20
player_speed = 5

# Bullet settings
bullets = []
bullet_width = 5
bullet_height = 15
bullet_speed = 7

# Enemy settings
enemies = []
enemy_width = 40
enemy_height = 30
enemy_speed = 2
enemy_spawn_rate = 60  # Frames between enemy spawns

# Game settings
score = 0
game_over = False
clock = pygame.time.Clock()
FPS = 60
font = pygame.font.SysFont(None, 36)

# Load background image (or create a simple one)
background = pygame.Surface((WIDTH, HEIGHT))
background.fill(SKY_BLUE)
for i in range(20):  # Add some clouds
    cloud_x = random.randint(0, WIDTH)
    cloud_y = random.randint(0, HEIGHT)
    cloud_size = random.randint(20, 60)
    pygame.draw.circle(background, WHITE, (cloud_x, cloud_y), cloud_size)

def draw_player(x, y):
    # Draw the player aircraft
    pygame.draw.polygon(screen, BLUE, [
        (x + player_width // 2, y),  # Nose
        (x, y + player_height),      # Bottom left
        (x + player_width, y + player_height)  # Bottom right
    ])
    # Add details to the aircraft
    pygame.draw.rect(screen, WHITE, (x + player_width // 4, y + player_height // 2, 
                                    player_width // 2, player_height // 2))

def draw_bullet(x, y):
    pygame.draw.rect(screen, RED, (x, y, bullet_width, bullet_height))

def draw_enemy(x, y):
    # Draw the enemy aircraft
    pygame.draw.polygon(screen, RED, [
        (x + enemy_width // 2, y + enemy_height),  # Bottom point
        (x, y),                                   # Top left
        (x + enemy_width, y)                      # Top right
    ])
    # Add details to the enemy aircraft
    pygame.draw.rect(screen, BLACK, (x + enemy_width // 4, y, 
                                    enemy_width // 2, enemy_height // 2))

def show_score():
    score_text = font.render(f"Score: {score}", True, BLACK)
    screen.blit(score_text, (10, 10))

def show_game_over():
    game_over_text = font.render(f"Game Over! Final Score: {score}", True, BLACK)
    reset_text = font.render("Press 'R' to Play Again", True, BLACK)
    screen.blit(game_over_text, (WIDTH // 2 - game_over_text.get_width() // 2, HEIGHT // 2 - 50))
    screen.blit(reset_text, (WIDTH // 2 - reset_text.get_width() // 2, HEIGHT // 2 + 10))

def reset_game():
    global player_x, player_y, bullets, enemies, score, game_over
    player_x = WIDTH // 2 - player_width // 2
    player_y = HEIGHT - player_height - 20
    bullets = []
    enemies = []
    score = 0
    game_over = False
# Main game loop
frame_count = 0
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r and game_over:
                reset_game()
            if event.key == pygame.K_SPACE and not game_over:
                # Fire a bullet from the center of the player
                bullet_x = player_x + player_width // 2 - bullet_width // 2
                bullet_y = player_y
                bullets.append([bullet_x, bullet_y])

    if not game_over:
        # Handle player movement
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            player_x = max(0, player_x - player_speed)
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            player_x = min(WIDTH - player_width, player_x + player_speed)
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            player_y = max(HEIGHT // 2, player_y - player_speed // 2)
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            player_y = min(HEIGHT - player_height, player_y + player_speed // 2)

        # Update bullets
        for bullet in bullets[:]:
            bullet[1] -= bullet_speed
            if bullet[1] < 0:
                bullets.remove(bullet)

        # Spawn enemies
        frame_count += 1
        if frame_count % enemy_spawn_rate == 0:
            enemy_x = random.randint(0, WIDTH - enemy_width)
            enemy_y = -enemy_height
            enemies.append([enemy_x, enemy_y])

        # Update enemies
        for enemy in enemies[:]:
            enemy[1] += enemy_speed
            if enemy[1] > HEIGHT:
                enemies.remove(enemy)

        # Check for collisions
        # Bullet-enemy collisions
        for bullet in bullets[:]:
            for enemy in enemies[:]:
                if (bullet[0] < enemy[0] + enemy_width and
                    bullet[0] + bullet_width > enemy[0] and
                    bullet[1] < enemy[1] + enemy_height and
                    bullet[1] + bullet_height > enemy[1]):
                    if bullet in bullets:
                        bullets.remove(bullet)
                    if enemy in enemies:
                        enemies.remove(enemy)
                    score += 10

        # Player-enemy collisions
        for enemy in enemies[:]:
            if (player_x < enemy[0] + enemy_width and
                player_x + player_width > enemy[0] and
                player_y < enemy[1] + enemy_height and
                player_y + player_height > enemy[1]):
                game_over = True

    # Draw everything
    screen.blit(background, (0, 0))
    
    # Draw bullets
    for bullet in bullets:
        draw_bullet(bullet[0], bullet[1])
    
    # Draw enemies
    for enemy in enemies:
        draw_enemy(enemy[0], enemy[1])
    
    # Draw player
    draw_player(player_x, player_y)
    
    # Draw UI
    show_score()
    if game_over:
        show_game_over()
    
    # Update display
    pygame.display.flip()
    
    # Cap the frame rate
    clock.tick(FPS)

# Quit the game
pygame.quit()
sys.exit()
