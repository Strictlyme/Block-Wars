import pygame
class Healthbar:
    def __init__(self):
        pygame.init()
        self.MaxHealth = 100
        self.CurrentHealth = 100
        self.Background, self.Foreground = (255,255,255), (0,255,255)
    def health_bar(self,surface, x, y, w, h, current_health, max_health):
        health_ratio = current_health/max_health
        pygame.draw.rect(surface, self.Background, (x,y,w,h))
        pygame.draw.rect(surface, self.Foreground, (x,y,w*health_ratio,h))