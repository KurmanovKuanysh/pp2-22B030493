import pygame

pygame.init()

WINDOW_SIZE = (1000, 800)
screen = pygame.display.set_mode(WINDOW_SIZE)


BALL_RADIUS = 25
BALL_POSITION = [WINDOW_SIZE[0] // 2, WINDOW_SIZE[1] // 2]


WHITE = (255, 255, 255)
RED = (255, 0, 0)


MOVEMENT_SPEED = 20


clock = pygame.time.Clock()


while True:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        BALL_POSITION[1] = max(BALL_POSITION[1] - MOVEMENT_SPEED, BALL_RADIUS)
    elif keys[pygame.K_DOWN]:
        BALL_POSITION[1] = min(
            BALL_POSITION[1] + MOVEMENT_SPEED, WINDOW_SIZE[1] - BALL_RADIUS)
    elif keys[pygame.K_LEFT]:
        BALL_POSITION[0] = max(BALL_POSITION[0] - MOVEMENT_SPEED, BALL_RADIUS)
    elif keys[pygame.K_RIGHT]:
        BALL_POSITION[0] = min(
            BALL_POSITION[0] + MOVEMENT_SPEED, WINDOW_SIZE[0] - BALL_RADIUS)


    screen.fill(WHITE)

    pygame.draw.circle(screen, RED, BALL_POSITION, BALL_RADIUS)

    pygame.display.flip()
    clock.tick(60)
