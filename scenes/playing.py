import pygame as pg
from scene import Scene
from button import Button
from board import Board

class Playing(Scene):
    def __init__(self):
        super().__init__()
        self.buttonDict = {
            "restart":  Button((400,55,125,30),"RESTART"),
            "mainMenu": Button((400,20,125,30),"MAIN MENU")
        }
        self.buttons = pg.sprite.Group(self.buttonDict.values())
        self.board = None
    
    def activate(self,size,flags):
        self.board = Board(size,flags)
    
    def deactivate(self):
        super().deactivate()
        self.board = None
    
    def handleEvents(self):
        if pg.event.get(pg.QUIT):
            self.quitted = True
        events = pg.event.get()
        
        for button in self.buttonDict.values():
            button.handle(events)
            
        self.board.handle(events)
    
    def update(self,delta):
        if self.buttonDict["mainMenu"].clicked:
            self.setNextScene("MAIN")
        
        elif self.buttonDict["restart"].clicked:
            self.board.restart()
        
        else:
            self.buttons.update()
            self.board.update(delta)
           
    def render(self):
        super().render()
        self.board.render(self.screen)
        self.drawText(self.screen, (240, 620), f"TIME: {self.board.timeString}", self.fonts(12), "topleft")
        self.drawText(self.screen, (400,620), f"Game ID: {self.board.gameID}", self.fonts(12), "topleft")

        self.drawText(self.screen, (110, 28 + 34*self.board.currentPlayer.index), "<<<", self.fonts(15), "topleft", self.board.currentPlayer.color)
        for player in self.board.players:
            self.drawText(self.screen, (100, 28 + 34*player.index), f"{player.name}: {player.score}", self.fonts(15), "topright", player.color)
        
        if not self.board.finished:
            self.drawText(self.screen, (185, 28), f"{self.board.found} OF {self.board.flags} FLAGS FOUND", self.fonts(12), "topleft")
            self.drawText(self.screen, (185, 62), f"FIND {self.board.winScore} FLAGS TO WIN", self.fonts(12), "topleft")
                        
        else:
            self.drawText(self.screen, (265, 50), f"WINNER: {self.board.currentPlayer.name}", self.fonts(15), "center", self.board.currentPlayer.color)