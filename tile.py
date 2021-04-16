import pygame as pg
from resourceLoader import loadFlag, loadFont

class Tile:
    """Tile class that is responsible for individual tiles inside the board"""
    
    FONTSIZE = 18
    BORDER_THICKNESS = 1
    SHOWN_BGCOLOR = pg.Color("gray")
    UNSHOWED_COLOR = pg.Color("white")
    BORDER_COLOR = pg.Color("gray50")
    HOVER_COLOR = pg.Color("green")
    NUMBER_COLORS = (None,pg.Color("blue"),pg.Color("green4"),pg.Color("red"),pg.Color("navyblue"),
                     pg.Color("darkred"),pg.Color("darkcyan"),pg.Color("black"),pg.Color("gray50"))

    def __init__(self, rect):
        self.rect = pg.Rect(rect)
        self.image = pg.Surface(self.rect.size)
        self.image.fill(self.UNSHOWED_COLOR)
        self.font = loadFont(self.FONTSIZE)
        
        self.flagColorKey = "BLACK"
        
        self.flag = False
        self.visible = False
        self.number = ...
    
    
    def show(self, finished = False):
        self.visible = True
        
        if self.flag:
            self.image = loadFlag(self.flagColorKey, self.rect.size) #pg.transform.smoothscale(FLAGS[self.flagColorKey],self.rect.size).convert()
        
        else:
            self.image.fill(self.UNSHOWED_COLOR if finished else self.SHOWN_BGCOLOR)
            if self.number > 0:
                textSurf = self.font.render(str(self.number), True, self.NUMBER_COLORS[self.number])
                textRect = textSurf.get_rect(center=self.image.get_rect().center)
                self.image.blit(textSurf,textRect)
    
    def hover(self,screen):
        if not self.visible:
            pg.draw.rect(screen,self.HOVER_COLOR,self.rect.inflate(-2,-2)) 
    
    def lastPlayedBorder(self,screen,color):
        pg.draw.rect(screen,color,self.rect.inflate(-5,-5),self.BORDER_THICKNESS+1)   
    
    def render(self,screen):        
        screen.blit(self.image,self.rect)
        pg.draw.rect(screen,self.BORDER_COLOR,self.rect,self.BORDER_THICKNESS)