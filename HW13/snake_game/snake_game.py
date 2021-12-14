import pygame as pg
import sys
import random


class Snake:
    def __init__(self, x, y):
        self.head = SnakeHead(x, y)
        self.segments = []
        self.segments.insert(0, self.head)
        for i in range (1,4):
            y += 40
            self.segments.append(SnakeSegment(x, y))
        self.heading = [0, -40]
        self.current_heading = 3
        self.previous_heading = 3
        self.apples_eaten = 0
        self.eat_ups = 0

    def draw_snake(self, screen):
        for i in self.segments:
            screen.blit(i.image, i.rect)
            pg.draw.rect(screen, (0, 255, 0), i.rect, 1)

    def change_heading(self, heading):
        if heading == 1:
            self.heading = [40, 0]
        elif heading == 2:
            self.heading = [-40, 0]
        elif heading == 3:
            self.heading = [0, -40]
        elif heading == 4:
            self.heading = [0, 40]
        self.current_heading = heading

    def move_snake(self):
        for i in range(len(self.segments)-1, 0, -1):
            if i > 0:
                self.segments[i].rect.center = tuple(self.segments[i-1].rect.center)
        self.segments[0].rect.centerx += self.heading[0]
        self.segments[0].rect.centery += self.heading[1]

        if self.segments[0].rect.right > WIDTH:
            self.segments[0].rect.left = 0
        elif self.segments[0].rect.left < 0:
            self.segments[0].rect.right = WIDTH

        if self.segments[0].rect.bottom > HEIGHT:
            self.segments[0].rect.top = 0
        elif self.segments[0].rect.top < 0:
            self.segments[0].rect.bottom = HEIGHT

        self.previous_heading = self.current_heading

    def add_segment(self):
        self.segments.insert(1, SnakeSegment(self.head.rect.left, self.head.rect.top))
        print(len(snake.segments))

    def delete_segments(self, number):
        SnakeSegment.counter -= len(self.segments[number::])
        del self.segments[number::]
        print(len(snake.segments)-1)

    def check_self(self, menu):
        for i in range(1, len(self.segments)):
            if self.segments[0].rect.center == self.segments[i].rect.center:
                print(len(snake.segments)-1)
                self.delete_segments(i)
                self.eat_ups += 1
                if self.eat_ups >= 3:
                    menu.game_over = 1
                return

    def check_apple(self, apple):
        if apple.rect.left == self.segments[0].rect.left and apple.rect.top == self.segments[0].rect.top:
            self.add_segment()
            self.apples_eaten += 1
            apple.move_apple(self)


class SnakeHead(pg.sprite.Sprite):
    def __init__(self, x, y):
        pg.sprite.Sprite.__init__(self)

        self.image = pg.Surface((40, 40))
        self.image.fill((255, 0, 0))

        self.rect = self.image.get_rect()
        self.rect.left = x
        self.rect.top = y


class SnakeSegment(pg.sprite.Sprite):
    counter = 1
    
    def __init__(self, x, y):
        print(f"Building segment {SnakeSegment.counter}")
        pg.sprite.Sprite.__init__(self)

        self.image = pg.Surface([40,40])
        self.image.fill((0, 0, 0))

        self.rect = self.image.get_rect()
        self.rect.left = x
        self.rect.top = y
        SnakeSegment.counter += 1

class Apple(pg.sprite.Sprite):
    def __init__(self, width, height):
        print(f"Building apple")
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((40, 40))
        self.image.fill((0,255,0))

        self.rect = self.image.get_rect()
        self.board_width = width - 40
        self.board_height = height - 40
        self.rect.left = random.randint(0, self.board_width / 40) * 40
        self.rect.top = random.randint(0, self.board_height / 40) * 40

    def move_apple(self, snake):
        self.rect.left = random.randint(0, self.board_width / 40) * 40
        self.rect.top = random.randint(0, self.board_height / 40) * 40
        print(f"Apple new coords: {self.rect.left}, {self.rect.top}")
        for i in snake.segments:
            if self.rect.left == i.rect.left and self.rect.top == i.rect.top:
                self.move_apple(snake)
                return

    def draw_apple(self, screen):
        screen.blit(self.image, self.rect)
        pg.draw.rect(screen, (0, 255, 0), self.rect, 1)


class TextBlock:
    def __init__(self, text):
        self.font = pg.font.SysFont('Arial', 25, True, False)
        self.text = self.font.render(f"{text}", True, (128, 0, 0))
        self.text_size_x = (self.font.size(text))[0]
        self.text_size_y = (self.font.size(text))[1]

    def update_text(self, text):
        self.text = self.font.render(f"{text}", True, (128, 0, 0))
        self.text_size_x = (self.font.size(text))[0]
        self.text_size_y = (self.font.size(text))[1]


class GameMenu:
    def __init__(self, screen):
        self.used = 0
        self.game_started = 0
        self.game_paused = 0
        self.game_over = 0
        self.x = 0
        self.y = 0
        self.size_x = 1280
        self.size_y = 800
        self.center_x = screen.get_rect().centerx
        self.center_y = screen.get_rect().centery
        self.restart_game = TextBlock("RESTART GAME")
        self.restart_game_pos = self.restart_game.text.get_rect(topleft=(self.center_x - self.restart_game.text_size_x / 2, self.center_y / 2 - self.restart_game.text_size_y))
        self.restart_game_rect = pg.Rect(self.restart_game_pos[0], self.restart_game_pos[1], self.restart_game.text_size_x, self.restart_game.text_size_y)
        self.start_game = TextBlock("START NEW GAME")
        self.start_game_pos = self.start_game.text.get_rect(topleft=(self.center_x - self.start_game.text_size_x/2, self.center_y/2))
        self.start_game_rect = pg.Rect(self.start_game_pos[0], self.start_game_pos[1], self.start_game.text_size_x, self.start_game.text_size_y)
        self.continue_game = TextBlock("CONTINUE GAME")
        self.continue_game_pos = self.continue_game.text.get_rect(topleft=(self.center_x - self.continue_game.text_size_x/2, self.center_y/2))
        self.continue_game_rect = pg.Rect(self.continue_game_pos[0], self.continue_game_pos[1], self.continue_game.text_size_x, self.continue_game.text_size_y)
        self.quit_game = TextBlock("QUIT GAME")
        self.quit_game_pos = self.start_game.text.get_rect(topleft=(self.center_x - self.quit_game.text_size_x / 2, self.center_y / 2 + self.quit_game.text_size_y))
        self.quit_game_rect = pg.Rect(self.quit_game_pos[0],self.quit_game_pos[1], self.quit_game.text_size_x, self.quit_game.text_size_y)
        self.game_over_text = TextBlock("Game Over")

    def show_game_menu(self, screen):
        if self.game_over == 1:
            screen.blit(menu.restart_game.text, [menu.restart_game_pos[0], menu.restart_game_pos[1]])
            screen.blit(menu.quit_game.text, [menu.quit_game_pos[0], menu.quit_game_pos[1]])
        elif self.game_started == 0:
            screen.blit(menu.start_game.text, [menu.start_game_pos[0], menu.start_game_pos[1]])
            screen.blit(menu.quit_game.text, [menu.quit_game_pos[0], menu.quit_game_pos[1]])
        elif self.game_started == 1:
            screen.blit(menu.restart_game.text, [menu.restart_game_pos[0], menu.restart_game_pos[1]])
            screen.blit(menu.continue_game.text, [menu.continue_game_pos[0], menu.continue_game_pos[1]])
            screen.blit(menu.quit_game.text, [menu.quit_game_pos[0], menu.quit_game_pos[1]])


def draw_board(screen, width, height):
    for i in range(0, height + 40, 40):
        pg.draw.line(screen,(255, 255, 255), (0, i), (width, i), 1)
    for i in range(0, width + 40, 40):
        pg.draw.line(screen, (255, 255, 255), (i, 0), (i, height), 1)


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
            print("Mouse button pressed")
            if event.button == 1:
                if not menu.game_started:
                    if menu.start_game_rect.collidepoint(event.pos):
                        print("Start game button pressed.")
                        menu.used = 1
                        menu.game_started = 1
                        menu.game_paused = 0
                    if menu.quit_game_rect.collidepoint(event.pos):
                        menu.used = 1
                        print("Exit Game button pressed.")
                        pg.quit()
                        sys.exit()
                elif menu.game_paused and not menu.game_over:
                    if menu.restart_game_rect.collidepoint(event.pos):
                        print("reStart game button pressed.")
                        menu.used = 1
                        menu.game_started = 1
                        menu.game_paused = 0
                        SnakeSegment.counter = 0
                        snake = Snake(WIDTH / 2, HEIGHT / 2)
                    if menu.continue_game_rect.collidepoint(event.pos):
                        print("continue game button pressed.")
                        menu.used = 1
                        menu.game_started = 1
                        menu.game_paused = 0
                    if menu.quit_game_rect.collidepoint(event.pos):
                        menu.used = 1
                        print("Exit Game button pressed.")
                        pg.quit()
                        sys.exit()
                elif menu.game_over:
                    if menu.restart_game_rect.collidepoint(event.pos):
                        print("reStart game button pressed.")
                        menu.used = 1
                        menu.game_started = 1
                        menu.game_over = 0
                        menu.game_paused = 0
                        SnakeSegment.counter = 0
                        snake = Snake(WIDTH / 2, HEIGHT / 2)
                    if menu.quit_game_rect.collidepoint(event.pos):
                        menu.used = 1
                        print("Exit Game button pressed.")
                        pg.quit()
                        sys.exit()
        if event.type == pg.KEYDOWN:
            print("Key Pressed")
            print(f"{menu.game_started} and {not menu.game_paused} and {not menu.game_over}")
            if menu.game_started == 1 and not menu.game_paused and not menu.game_over:
                print("menu.game_started and not menu.game_paused and not menu.game_over")
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
                    print("Escape pressed")
                    menu.game_paused = 1
            elif menu.game_started and menu.game_paused and not menu.game_over:
                if event.key == pg.K_ESCAPE:
                    print("Escape pressed")
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
        if counter >= 10:
            snake.move_snake()
            snake.check_self(menu)
            snake.check_apple(apple)
            counter = 0
    clock.tick(100)
