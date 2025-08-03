import pygame; from tkinter import Tk; from sys import exit; from Blocks import blocks; from HealthBar import Healthbar
from secrets import randbelow; from tkinter import messagebox
class BlockWars:
    def __init__(self, name):
        pygame.init()
        self.name = name
        self.Running = True
        self.__ = Tk()
        self.__.withdraw()
        self.WIDTH = self.__.winfo_screenwidth()
        self.HEIGHT = self.__.winfo_screenheight()-50
        self.Screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        self.Background = (0,0,0)
        self.bl_ck = blocks()
        self.hb = Healthbar()
        self.txtColor = (255,255,255)
        self.Score = 0
        self.hbb = [self.bl_ck.HeavenyBlock]
        self.hbb_ = [self.bl_ck.HeavenyBlock2]
        self._hbb_ = [self.bl_ck.HeavenyBlock3]
        self.hbb2 = [self.bl_ck.HeavenyBlock4]
        self.hbb3 = [self.bl_ck.HeavenyBlock5]
        self.hbb4 = [self.bl_ck.HeavenyBlock6]
        self.HeavenlyBlocksCollected = 0
        self.font = pygame.font.Font(None,32)
        pygame.display.set_caption(self.name)
    def Run(self):
        while self.Running:
            self.Screen.fill(self.Background)
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    self.Running = False
            self.Keys = pygame.key.get_pressed()
            if self.Keys[pygame.K_UP]:
                self.bl_ck.Player.y -= self.bl_ck.Player_speed
            if self.Keys[pygame.K_DOWN]:
                self.bl_ck.Player.y += self.bl_ck.Player_speed
            if self.Keys[pygame.K_LEFT]:
                self.bl_ck.Player.x -= self.bl_ck.Player_speed
            if self.Keys[pygame.K_RIGHT]:
                self.bl_ck.Player.x += self.bl_ck.Player_speed
            if self.bl_ck.Player.y > self.HEIGHT - self.bl_ck.Rect_height:
                self.bl_ck.Player.y = self.HEIGHT - self.bl_ck.Rect_height
            if self.bl_ck.Player.y < 100:
                self.bl_ck.Player.y = 100
            if self.bl_ck.Player.x < 0:
                self.bl_ck.Player.x = self.WIDTH
            if self.bl_ck.Player.x > self.WIDTH:
                self.bl_ck.Player.x = 0
            if self.hb.CurrentHealth <= 0:
                self.Running = False
                exit()
            self.Collected = self.font.render(f"Blocks Collected: {self.HeavenlyBlocksCollected}", True, self.txtColor)
            self.displayText = self.font.render(f"Score: {self.Score:,.2f}",True, (255,255,255))
            self.textRect_ = self.Collected.get_rect(bottomleft=(10, self.HEIGHT-40))
            self.textRect = self.displayText.get_rect(center=(self.HEIGHT-40,10))
            self.Screen.blit(self.Collected, self.textRect_)
            self.Screen.blit(self.displayText, self.textRect)
            self.hb.health_bar(self.Screen, 10, 10, 400, 20, self.hb.CurrentHealth, self.hb.MaxHealth)
            pygame.draw.rect(self.Screen, self.bl_ck.Player_Color, self.bl_ck.Player)
            for enemy_block in self.bl_ck.Enemies:
                pygame.draw.rect(self.Screen, self.bl_ck.Rect_Colors, enemy_block)
            for enemy in self.bl_ck.Enemies:
                if self.bl_ck.Player.colliderect(enemy):
                    self.hb.CurrentHealth -= self.bl_ck.EnemyDamage
            for enemy in self.bl_ck.Enemies:
                enemy.y += randbelow(21)
                if enemy.y >= self.HEIGHT:
                    enemy.y = 10
                    enemy.x = randbelow(self.WIDTH-self.bl_ck.Rect_width)
                    self.Score += 10
            if self.Score >= 100:
                self.bl_ck.EnemyDamage += .001
            self.bl_ck.clock.tick(self.bl_ck.FPS)
            if self.hb.CurrentHealth < 30:
                self.hb.Foreground = (255,0,0)
            if self.hb.CurrentHealth > 60:
                self.hb.Foreground = (0,255,255)
            if 30 < self.hb.CurrentHealth < 60:
                self.hb.Foreground = (100,100,100)
            if self.Score >= 500:
                for rect in self.hbb:
                    pygame.draw.rect(self.Screen, (255,0,255), rect)
            if self.Score >= 3_000:
                for rect in self.hbb_:
                    pygame.draw.rect(self.Screen, (255,0,255), rect)
            if self.Score >= 5_000:
                for rect in self._hbb_:
                    pygame.draw.rect(self.Screen, (255,0,255), rect)
            if self.Score >= 7_500:
                for rect in self.hbb2:
                    pygame.draw.rect(self.Screen, (255,0,255), rect)
            if self.Score >= 9_500:
                for rect in self.hbb3:
                    pygame.draw.rect(self.Screen, (255,0,255), rect)
            if self.Score >= 15_000:
                for rect in self.hbb4:
                    pygame.draw.rect(self.Screen, (255,0,255), rect)
            if self.bl_ck.Player.colliderect(self.bl_ck.HeavenyBlock):
                if self.HeavenlyBlocksCollected == 0:
                    self.HeavenlyBlocksCollected = 1
                self.hb.CurrentHealth = 100
                for rect in self.hbb:
                    self.hbb.remove(rect)
            elif self.bl_ck.Player.colliderect(self.bl_ck.HeavenyBlock2):
                if self.HeavenlyBlocksCollected == 1:
                    self.HeavenlyBlocksCollected = 2
                self.hb.CurrentHealth = 200
                self.hb.MaxHealth = 200
                self.bl_ck.EnemyDamage += .01
                for rect in self.hbb_:
                    self.hbb_.remove(rect)
            elif self.bl_ck.Player.colliderect(self.bl_ck.HeavenyBlock3):
                if self.HeavenlyBlocksCollected == 2:
                    self.HeavenlyBlocksCollected = 3
                self.hb.CurrentHealth = 300
                self.hb.MaxHealth = 300
                self.Score += .03
                self.bl_ck.EnemyDamage += .02
                for rect in self._hbb_:
                    self._hbb_.remove(rect)
            elif self.bl_ck.Player.colliderect(self.bl_ck.HeavenyBlock4):
                if self.HeavenlyBlocksCollected == 3:
                    self.HeavenlyBlocksCollected = 4
                self.hb.CurrentHealth = 350
                self.hb.MaxHealth = 350
                self.Score += 120
                self.bl_ck.EnemyDamage += .03
                for rect in self.hbb2:
                    self.hbb2.remove(rect)
            elif self.bl_ck.Player.colliderect(self.bl_ck.HeavenyBlock5):
                if self.HeavenlyBlocksCollected == 4:
                    self.HeavenlyBlocksCollected = 5
                self.hb.CurrentHealth = 350
                self.hb.MaxHealth = 350
                self.Score += .09
                self.bl_ck.EnemyDamage += .04
                for rect in self.hbb3:
                    self.hbb3.remove(rect)
            elif self.bl_ck.Player.colliderect(self.bl_ck.HeavenyBlock6):
                if self.HeavenlyBlocksCollected == 5:
                    self.HeavenlyBlocksCollected = 6
                self.hb.CurrentHealth = 350
                self.hb.MaxHealth = 350
                self.Score += .33
                self.bl_ck.EnemyDamage += .05
                for rect in self.hbb4:
                    self.hbb4.remove(rect)
            self.Score += 0.1
            if self.HeavenlyBlocksCollected == 5:
                self.txtColor = (0,255,0)
            if self.Score > 15_000:
                self.txt = self.font.render("Score 20,000 points to win.", True, (255,255,255))
                self.txtrct = self.txt.get_rect(bottomright=(300, self.HEIGHT-10))
                self.Screen.blit(self.txt, self.txtrct)
            if self.Score >= 20_000:
                self.Running = False
                exit()
            pygame.display.update()
if __name__ == '__main__':
    game = BlockWars("Block Wars")
    game.Run()