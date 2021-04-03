import pygame as pg
from scene import Scene
from button import Button

class CustomMenu(Scene): 
    def __init__(self):
        super().__init__()
        self.buttonDict = {
            "size++":   Button((335, 230, 25, 19), "+"),
            "size--":   Button((335, 250, 25, 19), "-"),
            "flag++":   Button((335, 290, 25, 19), "+"),
            "flag--":   Button((335, 310, 25, 19), "-"),
            "start":    Button((225, 390, 100, 60), "START"),
            "mainMenu": Button((400, 20, 125, 30), "MAIN MENU")
        }
        self.buttons = pg.sprite.Group(self.buttonDict.values())
        self.cSize = 9
        self.cFlags = 15
    
    def update(self,delta):
        if self.buttonDict["start"].clicked:
            self.setNextScene("PLAYING",self.cSize,self.cFlags)
        
        elif self.buttonDict["mainMenu"].clicked:
            self.setNextScene("MAIN")
        
        elif self.buttonDict["size++"].clicked:
            if self.cSize < 20:
                self.cSize += 1
        
        elif self.buttonDict["size--"].clicked:
            if self.cSize > 1 and self.cFlags <= ((self.cSize-1) ** 2):
                self.cSize -= 1
                
        elif self.buttonDict["flag++"].clicked:
            if self.cFlags < 100 and self.cFlags < (self.cSize ** 2):
                self.cFlags += 1
        
        elif self.buttonDict["flag--"].clicked:
            if self.cFlags > 1:
                self.cFlags -= 1
        
        else:
            self.buttons.update()
        
    def render(self):
        super().render()
        self.drawText(self.screen, (275,250), "SIZE: {0}x{0}".format(self.cSize),self.fonts(15),"center")
        self.drawText(self.screen, (275,310), f"FLAGS: {self.cFlags}",self.fonts(15),"center")