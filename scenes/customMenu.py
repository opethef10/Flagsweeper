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
        self.customSize = 9
        self.customFlags = 15
    
    def update(self,delta):
        """Update custom size and custom flags with each button click"""
        
        if self.buttonDict["start"].clicked:
            self.setNextScene("PLAYING",self.customSize,self.customFlags)
        
        elif self.buttonDict["mainMenu"].clicked:
            self.setNextScene("MAIN")
        
        elif self.buttonDict["size++"].clicked:
            if self.customSize < 20:
                self.customSize += 1
        
        elif self.buttonDict["size--"].clicked:
            if self.customSize > 1 and self.customFlags <= ((self.customSize-1) ** 2):
                self.customSize -= 1
                
        elif self.buttonDict["flag++"].clicked:
            if self.customFlags < 100 and self.customFlags < (self.customSize ** 2):
                self.customFlags += 1
        
        elif self.buttonDict["flag--"].clicked:
            if self.customFlags > 1:
                self.customFlags -= 1
        
        else:
            self.buttons.update()
        
    def render(self):
        super().render()
        self.drawText(self.screen, (275,250), "SIZE: {0}x{0}".format(self.customSize),self.fonts(15),"center")
        self.drawText(self.screen, (275,310), f"FLAGS: {self.customFlags}",self.fonts(15),"center")