import time
from random import randrange
from itertools import cycle
import pygame as pg
from tile import Tile

class Player:
    def __init__(self, index, name):
        self.index = index 
        self.name = name
        self.color = pg.Color(name.lower())
        self.score = 0
        self.lastCoord = None

class Board:
    WIDTH = 500
    HEIGHT = 500
    OFFSET_X = 25
    OFFSET_Y = 100
    
    def __init__(self,size,flags):        
        self.size = size
        self.flags = flags
        self.tileMatrix = [[Tile(self.boardToPixelCoord(r,c)) for c in range(self.size)] for r in range(self.size)]
        self.initFlags()
        self.initNumbers()
        self.finished = False
        self.clicked = False
        self.hoveredTileCoord = None
        self.totalTime = 0
        self.found = 0
        self.winScore = self.flags//2 + 1
        self.gameID = self.gameIdEncode(time.time())
        
        self.players = [Player(index,name) for index, name in enumerate(("RED", "BLUE"))]
        self.playerIterator = cycle(self.players)
        self.currentPlayer = next(self.playerIterator)

    def restart(self):
        self.__init__(self.size,self.flags)
    
    def initFlags(self):
        for _ in range(self.flags):
            while True:
                r,c=(randrange(self.size),randrange(self.size))
                if not self.tileMatrix[r][c].flag:
                    self.tileMatrix[r][c].flag = True
                    break
    
    def initNumbers(self):
        for r, row in enumerate(self.tileMatrix):
            for c, tile in enumerate(row):
                if not tile.flag:
                    tile.number = sum(self.tileMatrix[rn][cn].flag for rn,cn in self.getNeighbors(r, c))

    def getNeighbors(self, r, c):
        for i in (-1, 0, 1):
            for j in (-1, 0, 1):
                if (i,j)!=(0,0) and (r + i) in range(self.size) and (c + j) in range(self.size):
                    yield (r + i, c + j)
    
    def pixelToBoardCoord(self,mousePos):
        mx,my = mousePos
        w = round(self.WIDTH / self.size)
        h = round(self.HEIGHT / self.size)
        r = (my - self.OFFSET_Y) // h
        c = (mx - self.OFFSET_X) // w
        
        if r in range(self.size) and c in range(self.size):
            if not self.tileMatrix[r][c].visible:
                return r,c
    
    def boardToPixelCoord(self,r,c):
        w = round(self.WIDTH / self.size)
        h = round(self.HEIGHT / self.size)
        x = c * w + self.OFFSET_X
        y = r * h + self.OFFSET_Y
        return x,y,w,h 
    
    def gameIdEncode(self,timestamp,base=62):
        alphabet= '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ-_'
        number = int(timestamp * 1000)
        result = ''
        while number:
            number, i = divmod(number, base)
            result += alphabet[i]
        return result
        #originalTimestamp = sum(alphabet.index(digit) * base**i for i,digit in enumerate(result)) / 1000
    
    def floodFill(self,r,c):
        tile=self.tileMatrix[r][c]
        if not tile.visible:
            tile.show()
            if tile.number == 0:
                for rn,cn in self.getNeighbors(r, c):
                    self.floodFill(rn,cn)
    
    def handle(self,events):
        if not self.finished:
            self.hoveredTileCoord = self.pixelToBoardCoord(pg.mouse.get_pos())
            self.clicked = False
            for event in events:
                if event.type == pg.MOUSEBUTTONUP and event.button == 1 and self.hoveredTileCoord:
                    self.clicked = True
    
    def update(self,delta):
        if not self.finished:
            self.totalTime += delta
            if self.clicked:
                r,c = self.currentPlayer.lastCoord = self.hoveredTileCoord
                tile=self.tileMatrix[r][c]
                if tile.flag:
                    tile.flagColorKey = self.currentPlayer.name
                    self.currentPlayer.score += 1
                    self.found += 1
                    if self.currentPlayer.score >= self.winScore:
                        self.finished = True
                        tile.show()
                        self.showAll()
                else:
                    self.currentPlayer = next(self.playerIterator)
                self.floodFill(r,c)
    
    @property
    def timeString(self):
        return time.strftime("X%#Hh X%#Mm %#Ss", 
                    time.gmtime(int(self.totalTime//1000))) \
                    .replace("X0h ","").replace("X0m ","").replace("X","")
    
    def showAll(self):
        for row in self.tileMatrix:
            for tile in row:
                if not tile.visible:
                    tile.show(finished = True)
    
    def render(self, screen):
        for row in self.tileMatrix:
            for tile in row:
                tile.render(screen)
        
        if not self.finished and self.hoveredTileCoord:
            r,c = self.hoveredTileCoord
            self.tileMatrix[r][c].hover(screen)
        
        for player in self.players:
            if player.lastCoord:
                r,c = player.lastCoord
                self.tileMatrix[r][c].lastPlayedBorder(screen, player.color)