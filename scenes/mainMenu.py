import pygame as pg
from scene import Scene
from button import Button

class MainMenu(Scene):
    """The main menu of the game, first scene after initilization of the game"""
    
    def __init__(self):
        """Initialize from superclass and initialize buttons for this scene"""
        super().__init__()
        self.buttonDict = {
            "easy":   Button((150,250,250,50),"EASY: 9x9, 15 FLAGS"),
            "medium": Button((150,310,250,50),"MEDIUM: 16x16, 51 FLAGS"),
            "hard":   Button((150,370,250,50),"HARD: 18x18, 61 FLAGS"),
            "custom": Button((150,430,250,50),"CUSTOM")
        }
        self.buttons = pg.sprite.Group(self.buttonDict.values())
        
    def update(self,delta):
        """Update the state of buttons"""
        
        if self.buttonDict["easy"].clicked:
            self.setNextScene("PLAYING",9,15)
        
        elif self.buttonDict["medium"].clicked:
            self.setNextScene("PLAYING",16,51)
        
        elif self.buttonDict["hard"].clicked:
            self.setNextScene("PLAYING",18,61)
        
        elif self.buttonDict["custom"].clicked:
            self.setNextScene("CUSTOM")
        
        else:
            self.buttons.update()
        
    def render(self):
        super().render()
        self.drawText(self.screen, (275,120),"FLAGSWEEPER",self.fonts(18),"center")
