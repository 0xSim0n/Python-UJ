import pygame
import random

pygame.init()

width, height = 250, 500
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snowflake Melter")

white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)

# Main settings of game
snowflake_radius = 15
base_snowflake_speed = 3
max_snowflake_speed = 10
snowflake_spawn_rate = 0.08
snowflakes = []
snowpile_height = 0
max_snowpile_height = height
pile_increment = 5

clock = pygame.time.Clock()

score = 0
font = pygame.font.Font(None, 36)

game_running = True
while game_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_running = False

    screen.fill(black)

    for snowflake in snowflakes:
        snowflake[1] += snowflake[2]
        pygame.draw.circle(screen, white, (snowflake[0], int(snowflake[1])), snowflake_radius)

        if snowflake[1] >= height:
            snowflakes.remove(snowflake)
            snowpile_height += pile_increment

    if snowpile_height >= max_snowpile_height:
        game_running = False

    if random.random() < snowflake_spawn_rate:
        snowflake_speed = base_snowflake_speed + (score / 10)
        snowflake_speed = min(snowflake_speed, max_snowflake_speed)
        snowflakes.append([random.randint(0, width), 0, snowflake_speed])

    mouse_x, mouse_y = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if click[0] == 1:
        for snowflake in snowflakes:
            distance = pygame.math.Vector2(mouse_x - snowflake[0], mouse_y - snowflake[1]).length()
            if distance < snowflake_radius:
                score += 1
                snowflakes.remove(snowflake)

    pygame.draw.rect(screen, white, (0, height - snowpile_height, width, snowpile_height))

    text = font.render(f"Score: {score}", True, red)
    screen.blit(text, (10, 10))

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
