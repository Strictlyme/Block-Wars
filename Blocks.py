import pygame; from random import randint; from tkinter import Tk; from secrets import randbelow
class blocks:
    def __init__(self):
        pygame.init()
        self.__ = Tk()
        self.WIDTH = self.__.winfo_screenwidth()
        self.HEIGHT = self.__.winfo_screenheight()-50
        self.Player_speed = 7
        self.EnemyDamage = 1
        self.HeavenyBlock = pygame.Rect(randint(0,self.WIDTH-300),randint(60,200), 60, 60)
        self.HeavenyBlock2 = pygame.Rect(randint(0,self.WIDTH-300),randint(60,200), 60, 60)
        self.HeavenyBlock3 = pygame.Rect(randint(0,self.WIDTH-300),randint(60,200), 60, 60)
        self.HeavenyBlock4 = pygame.Rect(randint(0,self.WIDTH-300),randint(60,200), 60, 60)
        self.HeavenyBlock5 = pygame.Rect(randint(0,self.WIDTH-300),randint(60,200), 60, 60)
        self.HeavenyBlock6 = pygame.Rect(randint(0,self.WIDTH-300),randint(60,200), 60, 60)
        self.clock = pygame.time.Clock()
        self.FPS = 60
        self.Rect_width, self.Rect_height = 50, 50
        self.Player = pygame.Rect((self.WIDTH/2), (self.HEIGHT-150), self.Rect_width, self.Rect_height)
        self.Enemies = [pygame.Rect(randbelow(self.WIDTH-self.Rect_width), 10, self.Rect_width, self.Rect_height) for x in range(20)]
        self.Rect_Colors = (255,0,0)
        self.Player_Color = (0,255,0)