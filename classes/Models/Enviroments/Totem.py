import pygame

from file_for_images import totem_picture


class Totem():
    def __init__(self,x,y):
        self.hp=100
        self.anim=totem_picture
        self.x=x
        self.y=y
        self.flag_spawn=True
    def spawn(self,surf):
        surf.blit(*self.anim,(self.x,self.y))
    def draw(self,surf):
        label = pygame.font.Font("fonts/RobotoMono-VariableFont_wght.ttf", 25)
        heal_point = label.render("Hp: " + str(self.hp), False, "green")
        surf.blit(heal_point,(self.x,self.y-30))
    def Protect(self, dmg):
        b = dmg
        self.hp = self.hp - dmg