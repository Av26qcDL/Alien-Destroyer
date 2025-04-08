import pygame
from sys import exit
from random import randint

def display_score(score_value):
    score_surf = test_font.render(f'Score: {score_value}',False,(64,64,64))
    score_rect = score_surf.get_rect(center = (400,50))
    screen.blit(score_surf,score_rect)
    return score_value

def obstacle_movement(obstacle_list):
    if obstacle_list:
        for obstacle_rect in obstacle_list:
            obstacle_rect.x -= 5

            if obstacle_rect.bottom == 310:screen.blit(blue_one_eyed_alien_surf,obstacle_rect)
            else:screen.blit(yellow_five_eyed_alien_surf,obstacle_rect)

        obstacle_list = [obstacle for obstacle in obstacle_list if obstacle.x > -100]

        return obstacle_list
    else: return []

def collisions(player, obstacles):
    if obstacles:
        for obstacle_rect in obstacles:
            if player.colliderect(obstacle_rect): return False
    return True 

def update_player_position(player, movement):
    if movement == -5:  # Move left
        player.x -= 5
    elif movement == 5:  # Move right
        player.x += 5

    # Ensure the player stays within screen bounds
    if player.left <= 0:
        player.left = 0
    elif player.right >= 800:
        player.right = 800

    return player


def bullet_movement(bullets):
    if bullets:
        for bullet in bullets:
            bullet.x += 7  # Bullets move right (positive x direction)
            screen.blit(bullet_surf, bullet)

        # Remove bullets that have gone off-screen
        active_bullets = [bullet for bullet in bullets if bullet.x < 900]
        return active_bullets
    else:
        return []

def check_bullet_collisions(bullets, obstacles):
    if bullets and obstacles:
        for bullet in bullets[:]:  # Creating a copy of the list to avoid issues during iteration
            for obstacle in obstacles[:]:  # Same here
                if bullet.colliderect(obstacle):
                    hit_position = (
                        obstacle.centerx,  # Use centerx instead of x
                        obstacle.centery  # Use centery instead of y
                    )

                    # Remove both the bullet and obstacle
                    if bullet in bullets:
                        bullets.remove(bullet)
                    if obstacle in obstacles:
                        obstacles.remove(obstacle)
                    # Return collision position
                    return True, hit_position
    return False, None  # No collision

# initialize pygame
pygame.mixer.pre_init(44100, -16, 2, 2048)
pygame.mixer.init(44100, -16, 2, 64)
gun_sound = pygame.mixer.Sound('assets/sounds/gun_fire.wav')
gun_sound.set_volume(0.5)
explosion_sound = pygame.mixer.Sound('assets/sounds/explosion.wav')
pygame.init()



# create the screen
screen = pygame.display.set_mode((800, 400), pygame.SRCALPHA) # Use SRCALING for better scaling on different resolutions
# Caption and Icon
pygame.display.set_caption("Alien Destroyer")
clock = pygame.time.Clock()
test_font = pygame.font.Font('assets/Font/Momo.ttf', 50)
game_active = False
game_over = False
start_time = 0
score = 0

sky_surf = pygame.image.load('assets/graphics/sky1.png').convert_alpha()
ground_surf = pygame.image.load('assets/graphics/Piso2.png').convert_alpha()

# Obstacles
blue_one_eyed_alien_surf = pygame.image.load('assets/images/blueoneeyedalien.png').convert_alpha()
yellow_five_eyed_alien_surf = pygame.image.load('assets/images/yellowfiveeyedalien.png').convert_alpha()

obstacle_rect_list = []

# Player char
player_surf = pygame.image.load('assets/images/person.png').convert_alpha()
player_rect = player_surf.get_rect(midbottom=(45, 310))
player_gravity = 0 
player_movement = 0  # Initialize player movement

# Bullets
bullet_surf = pygame.image.load('assets/images/bullet.png').convert_alpha()
bullet_list = []  # List to store active bullets

# Explosion parameters
explosion_list = []  # Store active explosions
explosion_duration = 10  # Frames the explosion lasts
# Image of explosion:
explosion_surf = pygame.Surface((30, 30))
explosion_surf.fill('orange')

# Constant Variables
ufo_stand = pygame.image.load('assets/images/ufo.png').convert_alpha()
ufo_stand = pygame.transform.rotozoom(ufo_stand,0,2)
ufo_stand_rect = ufo_stand.get_rect(center = (400, 200))

game_name = test_font.render('Alien Destroyer', False,(111,196,169))
game_name_rect = game_name.get_rect(center = (400, 100))
game_over_message = test_font.render('Game Over', False,(111,196,169))
game_over_message_rect = game_over_message.get_rect(center = (400, 100))

game_message = test_font.render('Press space to start game', False,(111,196,169))
game_message_rect = game_message.get_rect(center = (400, 300)) 

instruction_message = test_font.render('Once in game, press space to jump and F to fire', False,(111,196,169))
instruction_message_rect = instruction_message.get_rect(center = (400, 350))

# Timer
obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer, 1500)


icon = pygame.image.load('assets/images/ufo.png')
pygame.display.set_icon(icon)


# Game Loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if game_active: 
            
            # Move left when 'a' is pressed
            if event.type == pygame.KEYDOWN:  # Corrected to KEYDOWN
                if event.key == pygame.K_a: 
                    player_movement = -5 

            # Move right when 'd' is pressed
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_d: 
                    player_movement = 5

            # Stop movement when 'a' or 'd' is released
            if event.type == pygame.KEYUP:  # Handle key release
                if event.key in [pygame.K_a, pygame.K_d]:
                    player_movement = 0

            if event.type == pygame.MOUSEBUTTONDOWN and player_rect.bottom >= 310:
                if player_rect.collidepoint(event.pos):
                    player_gravity = -20  # Jump when the player clicks on the character

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and player_rect.bottom >= 310:
                    player_gravity = -20 # Jump when space is pressed

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_f:  # 'f' key for fire
                    # Create a new bullet at the player's position
                    bullet_rect = bullet_surf.get_rect(midleft=(player_rect.right, player_rect.centery))
                    bullet_list.append(bullet_rect)
                    gun_sound.play()

        else:       # Use spacebar to restart the game at start or game over screen
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
                start_time = int(pygame.time.get_ticks() / 1000)
                score = 0

        if event.type == obstacle_timer and game_active:
            if randint(0,2):
                obstacle_rect_list.append(blue_one_eyed_alien_surf.get_rect(bottomright = (randint(900,1100), 310)))
            else:
                obstacle_rect_list.append(yellow_five_eyed_alien_surf.get_rect(bottomright=(randint(900, 1100), 210)))

    if game_active:
        screen.blit(sky_surf, (0, 0))
        screen.blit(ground_surf, (0, 300))
        bullet_list = bullet_movement(bullet_list)
        score = display_score(score)

        # Player
        player_gravity += 1
        player_rect.y += player_gravity 
        player_rect.x += player_movement  # Apply horizontal movement
        if player_rect.bottom >= 310: player_rect.bottom = 310
        screen.blit(player_surf, player_rect)

        # Obstacle movement
        obstacle_rect_list = obstacle_movement(obstacle_rect_list)

        # collision
        game_active = collisions(player_rect, obstacle_rect_list)  # Check collisions

        hit, collision_pos = check_bullet_collisions(bullet_list, obstacle_rect_list)
        if hit:
            explosion_sound.play()
            score += 1
            # Add explosion at the collision position
            explosion_list.append([collision_pos[0], collision_pos[1], explosion_duration])

        # Drawing all active explosions
        for explosion in explosion_list[:]:
            x, y, duration = explosion
            # Draw explosion
            explosion_rect = explosion_surf.get_rect(center=(x, y))
            screen.blit(explosion_surf, explosion_rect)
            # Decrease duration
            explosion[2] -= 1
            # Remove finished explosions
            if explosion[2] <= 0:
                explosion_list.remove(explosion)

    else:
        screen.fill((94,129,162))
        screen.blit(ufo_stand, ufo_stand_rect)
        obstacle_rect_list.clear()
        player_rect.midbottom = (80, 310)
        player_gravity = 0

        score_message = test_font.render(f'Your Score: {score}', False,(111,196,169))
        score_message_rect = score_message.get_rect(center = (400,300))
        screen.blit(game_name, game_name_rect)

        if score > 0:
            screen.blit(score_message, score_message_rect)
        else: screen.blit(game_message, game_message_rect) 
        screen.blit(instruction_message, instruction_message_rect)


    pygame.display.update()
    clock.tick(60)