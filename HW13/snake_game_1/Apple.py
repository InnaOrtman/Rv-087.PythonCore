import pygame as pg
import random


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
