import pygame as pg
import sys
from Snake import *
from Apple import *
from Menu import *
from Funcs import *

pg.init()
# Assigning core variables
WIDTH = 1280
HEIGHT = 800
# Declaring display
background_color = (128, 128, 128)
screen = pg.display.set_mode((WIDTH, HEIGHT))
clock = pg.time.Clock()
pg.display.set_caption("Snake")
screen.fill(background_color)
pg.display.flip()
font = pg.font.SysFont('Arial', 25, True, False)

# Declaring stuff
counter = 1
screen_center_x = screen.get_rect().centerx
screen_center_y = screen.get_rect().centery
menu = GameMenu(screen)
snake = Snake(WIDTH/2, HEIGHT/2)
apple = Apple(WIDTH, HEIGHT)

SPEED = 50

# Game loop
game = True
while game:
    counter += 1
    pg.display.set_caption(f"Snake game. Apples eaten: {snake.apples_eaten}. Snake length: {len(snake.segments)}. Times bit own tail: {snake.eat_ups}.")
    for event in reversed(pg.event.get()):
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
        if event.type == pg.MOUSEBUTTONDOWN:
            if event.button == 1:
                if not menu.game_started:
                    if menu.start_game_rect.collidepoint(event.pos):
                        menu.used = 1
                        menu.game_started = 1
                        menu.game_paused = 0
                    if menu.quit_game_rect.collidepoint(event.pos):
                        menu.used = 1
                        pg.quit()
                        sys.exit()
                elif menu.game_paused and not menu.game_over:
                    if menu.restart_game_rect.collidepoint(event.pos):
                        menu.used = 1
                        menu.game_started = 1
                        menu.game_paused = 0
                        SnakeSegment.counter = 0
                        snake = Snake(WIDTH / 2, HEIGHT / 2)
                    if menu.continue_game_rect.collidepoint(event.pos):
                        menu.used = 1
                        menu.game_started = 1
                        menu.game_paused = 0
                    if menu.quit_game_rect.collidepoint(event.pos):
                        menu.used = 1
                        pg.quit()
                        sys.exit()
                elif menu.game_over:
                    if menu.restart_game_rect.collidepoint(event.pos):
                        menu.used = 1
                        menu.game_started = 1
                        menu.game_over = 0
                        menu.game_paused = 0
                        SnakeSegment.counter = 0
                        snake = Snake(WIDTH / 2, HEIGHT / 2)
                    if menu.quit_game_rect.collidepoint(event.pos):
                        menu.used = 1
                        pg.quit()
                        sys.exit()
        if event.type == pg.KEYDOWN:
            if menu.game_started == 1 and not menu.game_paused and not menu.game_over:
                if event.key == pg.K_RIGHT:
                    if snake.current_heading != 1 and snake.current_heading != 2 and snake.previous_heading != 2:
                        snake.change_heading(1)
                elif event.key == pg.K_LEFT:
                    if snake.current_heading != 2 and snake.current_heading != 1 and snake.previous_heading != 1:
                        snake.change_heading(2)
                elif event.key == pg.K_UP:
                    if snake.current_heading != 3 and snake.current_heading != 4 and snake.previous_heading != 4:
                        snake.change_heading(3)
                elif event.key == pg.K_DOWN:
                    if snake.current_heading != 4 and snake.current_heading != 3 and snake.previous_heading != 3:
                        snake.change_heading(4)
                if event.key == pg.K_ESCAPE:
                    menu.game_paused = 1
            elif menu.game_started and menu.game_paused and not menu.game_over:
                if event.key == pg.K_ESCAPE:
                    menu.game_paused = 0

    if menu.game_over == 1:
        menu.show_game_menu(screen)
        menu.game_paused = 1
        pg.display.flip()
    elif menu.used == 0 or menu.game_paused == 1:
        menu.show_game_menu(screen)
        pg.display.flip()
    elif menu.game_started == 1 and menu.game_paused == 0:
        screen.fill(background_color)
        draw_board(screen, WIDTH, HEIGHT)
        snake.draw_snake(screen)
        apple.draw_apple(screen)
        pg.display.flip()
        if counter >= SPEED:
            snake.move_snake(WIDTH, HEIGHT)
            snake.check_self(menu)
            snake.check_apple(apple)
            counter = 0
    clock.tick(100)
