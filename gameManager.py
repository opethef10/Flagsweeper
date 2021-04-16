import os
import pygame as pg
from settings import TITLE, WINDOW_SIZE, FPS
from resourceLoader import ICON
from scenes import MainMenu, CustomMenu, Playing

class GameManager:
    """The class which is responsible for management of the game"""
    
    def __init__(self):
        """Initialize screen and scenes"""
        os.environ['SDL_VIDEO_CENTERED'] = "True"
        pg.init()
        pg.display.set_caption(TITLE)
        pg.display.set_icon(ICON)
        pg.display.set_mode(WINDOW_SIZE)
        self.clock = pg.time.Clock()
        self.FPS = FPS
        self.sceneDict = {
            "MAIN":    MainMenu(),
            "CUSTOM":  CustomMenu(),
            "PLAYING": Playing()
        }
        self.scene = self.sceneDict["MAIN"]
        
    def changeScene(self):
        """Deactivate the previous scene and activate the next scene"""
        nextSceneName, *args = self.scene.nextSceneArgs
        self.scene.deactivate()
        self.scene = self.sceneDict[nextSceneName]
        self.scene.activate(*args)
    
    def loop(self):
        """Game loop function"""
        delta = self.clock.tick(self.FPS)
        self.scene.handleEvents()
        self.scene.update(delta)
        self.scene.render()
        pg.display.update()
        if self.scene.changeFlag:
            self.changeScene()

    def over(self):
        return self.scene.quitted
    
    def quit(self):
        pg.quit()