class Magic_pict:
    def __init__(self, name,spec_dmg, dmg,pict,x,y):
        self.name = name
        self.damage = dmg
        self.pict = pict
        self.x=x
        self.y=y
        self.sd=spec_dmg
    def special_attack(self,surf,x,y):
        if self.x-x>=7:
            self.x-=5
        else:
            self.x+=5
        if self.y-y>=7:
            self.y-=5
        else:
            self.y+=5
        surf.blit(*self.pict,(self.x,self.y))