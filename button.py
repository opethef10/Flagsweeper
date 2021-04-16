import pygame as pg
from resourceLoader import loadFont

class Button(pg.sprite.Sprite):
    FONTSIZE = 15
    BORDER_THICKNESS = 1
    normalColor = pg.Color("red")
    hoverColor = pg.Color("orange")
    pressedColor = pg.Color("darkorange")
    borderColor = pg.Color("gray25")
    textColor = pg.Color("white")
    
    def __init__(self, rect, text):
        super().__init__()
        self.rect = pg.Rect(rect)
        self.image = pg.Surface(self.rect.size)
        self.text = text
        self.textSurf = loadFont(self.FONTSIZE).render(self.text,True,self.textColor)
        self.textRect = self.textSurf.get_rect(center=self.image.get_rect().center)
        self.hovered = False
        self.clicked = False
        self.pressed = False

    def handle(self,events):
        """Handle mouse click events for the button"""
        
        self.clicked = False
        self.hovered = True if self.rect.collidepoint(pg.mouse.get_pos()) else False
        for event in events:     
            if event.type == pg.MOUSEBUTTONDOWN and event.button == 1 and self.hovered:
                self.pressed = True
            elif event.type == pg.MOUSEBUTTONUP and event.button == 1:
                if self.hovered and self.pressed:
                    self.clicked = True
                self.pressed = False
                    
    def update(self):
        """Update the button color after pressing or hovering"""

        self.image.fill(self.pressedColor if self.pressed else (self.hoverColor if self.hovered else self.normalColor))
        self.image.blit(self.textSurf,self.textRect)
        pg.draw.rect(self.image, self.borderColor, self.image.get_rect(), self.BORDER_THICKNESS)