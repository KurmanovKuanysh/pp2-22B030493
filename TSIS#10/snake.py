import pygame
import pygame as pg
from random import *
import time
from snake_users_data import user_name, level, update

pygame.init()
sc = pg.display.set_mode((800, 600))
check = True
sp_check = True
x = 800 // 2
y = 600 // 2
speed_x = 0
speed_y = 0
old_level = level
apple = randrange(0, 800, 20), randrange(0, 600, 20)
size_full_apple_x = 20
size_full_apple_y = 20
pause = pygame.image.load('TSIS/TSIS#10/images/Pause-PNG-Image-Transparent.png')
start = pygame.image.load('TSIS/TSIS#10/images/Play-Button-Transparent-Image.png')
pause = pygame.transform.scale(pause, (50, 50))
start = pygame.transform.scale(start, (50, 50))
sp = pause
snake_body = [(x, y)]
clock = pg.time.Clock()
f = pg.font.SysFont('arial', 30)
score = 0
FPS = 15
score_table = f.render(str(score), True, 'red')
table_user_name = f.render(user_name, True, 'red')
cent = table_user_name.get_rect(center=(400, 10))
l = 1
speed = 20
apple_v = choice([1, 0.5])
if apple_v == 1:
    size_full_apple_x = 20
    size_full_apple_y = 20
if apple_v == 0.5:
    size_full_apple_x = 10
    size_full_apple_y = 10
timer = time.time()
while check:
    user_name2 = f"{user_name} {level}"
    table_user_name = f.render(user_name2, True, 'red')
    sc.fill(0)
    score_table = f.render(str(score), True, 'red')
    sc.blit(table_user_name, (cent))
    sc.blit(score_table, (10, -5))
    sc.blit(sp, (750, -5))
    [(pg.draw.rect(sc, pg.Color("white"), (i, j, 20, 20)))
     for i, j in snake_body]
    pg.draw.rect(sc, pg.Color("red"),
                 (*apple, size_full_apple_x, size_full_apple_y))
    for i in pg.event.get():
        if not sp_check:
            while not sp_check:
                for i in pg.event.get():
                    if i.type == pg.MOUSEBUTTONDOWN and i.button == 1:
                        if 750 <= i.pos[0] <= 800 and -5 <= i.pos[1] <= 40:
                            sp_check = not sp_check
                            if not sp_check:
                                sp = start
                            if sp_check:
                                sp = pause
        elif i.type == pg.MOUSEBUTTONDOWN and i.button == 1:
            if 750 <= i.pos[0] <= 800 and -5 <= i.pos[1] <= 40:
                sp_check = not sp_check
                if not sp_check:
                    sp = start
                if sp_check:
                    sp = pause
        if i.type == pg.KEYDOWN:
            if i.key == pg.K_RETURN or snake_body[-1] == (800, range(0, 600)):
                check = False
            elif i.key == pg.K_d and speed_x != -speed:
                speed_x = speed
                speed_y = 0
            elif i.key == pg.K_a and speed_x != speed:
                speed_x = -speed
                speed_y = 0
            elif i.key == pg.K_w and speed_y != speed:
                speed_y = -speed
                speed_x = 0
            elif i.key == pg.K_s and speed_y != -speed:
                speed_y = speed
                speed_x = 0
    if snake_body[-1] == apple:
        timer = time.time()
        l += 1
        score += apple_v
        apple_v = choice([1, 0.5])
        if apple_v == 1:
            size_full_apple_x = 20
            size_full_apple_y = 20
        if apple_v == 0.5:
            size_full_apple_x = 10
            size_full_apple_y = 10
        apple = randrange(0, 800, 20), randrange(40, 600, 20)
        if score % 3 == 0 and score != 0:
            level += 1
        elif float(score - 0.5) % 3 == 0 and float(score - 0.5) != 0:
            level += 1
    if time.time() - timer > 5.0:
        timer = time.time()
        apple_v = choice([1, 0.5])
        if apple_v == 1:
            size_full_apple_x = 20
            size_full_apple_y = 20
        if apple_v == 0.5:
            size_full_apple_x = 10
            size_full_apple_y = 10
        apple = randrange(0, 800, 20), randrange(40, 600, 20)
    for i in snake_body:
        if snake_body.count(i) > 1:
            check = False
    a, b = snake_body[-1]
    if a < 0 or a > 780 or b < 40 or b > 580:
        check = False
    x += speed_x
    y += speed_y
    snake_body.append((x, y))
    snake_body = snake_body[-l:]
    pg.display.update()
    clock.tick(FPS + (2 * level))

update(user_name, level)
while check:
    print("Main loop")
    # rest of the code
