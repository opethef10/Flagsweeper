import pygame as pg
from resourceLoader import loadFont
from settings import VERSION

class Scene:
    """Superclass for Scene objects"""
    
    BGCOLOR = pg.Color("gray")
    DEFAULT_TEXT_COLOR = pg.Color("black")
    
    def __init__(self):
        self.screen = pg.display.get_surface()
        self.fonts = loadFont
        self.quitted = False
        self.changeFlag = False
        self.nextSceneArgs = None
    
    def drawText(self, surface, pos, text, font, align, color = DEFAULT_TEXT_COLOR, background = None, antialias = True):
        textSurf = font.render(text, antialias, color, background)
        textRect = textSurf.get_rect(**{align: pos})
        surface.blit(textSurf,textRect)
        
    def handleEvents(self):
        if pg.event.get(pg.QUIT):
            self.quitted = True
        events = pg.event.get()
        for button in self.buttonDict.values():
            button.handle(events)
    
    def setNextScene(self, *args):
        self.changeFlag = True
        self.nextSceneArgs = args
    
    def deactivate(self): 
        """Cleanup the scene before a scene change"""
        self.changeFlag = False
        self.nextSceneArgs = None
    
    def activate(self, *args):
        """To be extended by subclasses"""
        
    def update(self, delta):
        """To be extended by subclasses"""
        
    def render(self):
        self.screen.fill(self.BGCOLOR)
        # self.drawText(self.screen, (375,620), f"Mouse pos: {pg.mouse.get_pos()}", self.fonts(12), "topleft")
        self.drawText(self.screen, (40,620), f"Version: {VERSION}", self.fonts(12), "topleft")
        self.buttons.draw(self.screen) 