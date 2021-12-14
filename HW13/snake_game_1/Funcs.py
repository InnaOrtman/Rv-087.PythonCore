import pygame as pg


def draw_board(screen, width, height):
    for i in range(0, height + 40, 40):
        pg.draw.line(screen,(255, 255, 255), (0, i), (width, i), 1)
    for i in range(0, width + 40, 40):
        pg.draw.line(screen, (255, 255, 255), (i, 0), (i, height), 1)
