import pygame as pg
from Textblock import *


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
            screen.blit(self.restart_game.text, [self.restart_game_pos[0], self.restart_game_pos[1]])
            screen.blit(self.quit_game.text, [self.quit_game_pos[0], self.quit_game_pos[1]])
        elif self.game_started == 0:
            screen.blit(self.start_game.text, [self.start_game_pos[0], self.start_game_pos[1]])
            screen.blit(self.quit_game.text, [self.quit_game_pos[0], self.quit_game_pos[1]])
        elif self.game_started == 1:
            screen.blit(self.restart_game.text, [self.restart_game_pos[0], self.restart_game_pos[1]])
            screen.blit(self.continue_game.text, [self.continue_game_pos[0], self.continue_game_pos[1]])
            screen.blit(self.quit_game.text, [self.quit_game_pos[0], self.quit_game_pos[1]])