import pygame as pg


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