import pygame as pg


class Snake:
    def __init__(self, x, y):
        self.head = SnakeHead(x, y)
        self.segments = []
        self.segments.insert(0, self.head)
        for i in range(1, 4):
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

    def move_snake(self, width, height):
        for i in range(len(self.segments) - 1, 0, -1):
            if i > 0:
                self.segments[i].rect.center = tuple(self.segments[i - 1].rect.center)
        self.segments[0].rect.centerx += self.heading[0]
        self.segments[0].rect.centery += self.heading[1]

        if self.segments[0].rect.right > width:
            self.segments[0].rect.left = 0
        elif self.segments[0].rect.left < 0:
            self.segments[0].rect.right = width

        if self.segments[0].rect.bottom > height:
            self.segments[0].rect.top = 0
        elif self.segments[0].rect.top < 0:
            self.segments[0].rect.bottom = height

        self.previous_heading = self.current_heading

    def add_segment(self):
        self.segments.insert(1, SnakeSegment(self.head.rect.left, self.head.rect.top))
        print(len(self.segments))

    def delete_segments(self, number):
        SnakeSegment.counter -= len(self.segments[number::])
        del self.segments[number::]
        print(len(self.segments) - 1)

    def check_self(self, menu):
        for i in range(1, len(self.segments)):
            if self.segments[0].rect.center == self.segments[i].rect.center:
                print(len(self.segments) - 1)
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

        self.image = pg.Surface([40, 40])
        self.image.fill((0, 0, 0))

        self.rect = self.image.get_rect()
        self.rect.left = x
        self.rect.top = y
        SnakeSegment.counter += 1