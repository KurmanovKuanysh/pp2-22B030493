import pygame

# initialize Pygame
pygame.init()

# set screen size
screen = pygame.display.set_mode((800, 600))

# set default colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# set default pen color and size
pen_color = BLACK
pen_size = 3

# set default eraser size
eraser_size = 20

# set default tool to pen
current_tool = "pen"

# define functions for drawing shapes
def draw_rectangle():
    mouse_pos = pygame.mouse.get_pos()
    pygame.draw.rect(screen, pen_color, (mouse_pos[0], mouse_pos[1], 50, 50))

def draw_circle():
    mouse_pos = pygame.mouse.get_pos()
    pygame.draw.circle(screen, pen_color, mouse_pos, 25)

def draw_eraser():
    mouse_pos = pygame.mouse.get_pos()
    pygame.draw.circle(screen, WHITE, mouse_pos, eraser_size)

# game loop
running = True
while running:
    # handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                current_tool = "rectangle"
            elif event.key == pygame.K_c:
                current_tool = "circle"
            elif event.key == pygame.K_e:
                current_tool = "eraser"
            elif event.key == pygame.K_b:
                pen_color = BLACK
            elif event.key == pygame.K_w:
                pen_color = WHITE
            elif event.key == pygame.K_q:
                pen_color = RED
            elif event.key == pygame.K_g:
                pen_color = GREEN
            elif event.key == pygame.K_s:
                pen_color = BLUE
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if current_tool == "rectangle":
                draw_rectangle()
            elif current_tool == "circle":
                draw_circle()
            elif current_tool == "eraser":
                draw_eraser()

    # draw current tool icon
    if current_tool == "rectangle":
        pygame.draw.rect(screen, pen_color, (10, 10, 50, 50))
    elif current_tool == "circle":
        pygame.draw.circle(screen, pen_color, (35, 35), 25)
    elif current_tool == "eraser":
        pygame.draw.circle(screen, WHITE, (35, 35), eraser_size)

    # draw color selection buttons
    pygame.draw.rect(screen, BLACK, (80, 10, 50, 50))
    pygame.draw.rect(screen, WHITE, (140, 10, 50, 50))
    pygame.draw.rect(screen, RED, (200, 10, 50, 50))
    pygame.draw.rect(screen, GREEN, (260, 10, 50, 50))
    pygame.draw.rect(screen, BLUE, (320, 10, 50, 50))

    # update display
    pygame.display.update()

# quit Pygame
pygame.quit()