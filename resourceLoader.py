"""Contains functions that are responsible for loading resources."""

import sys
from pathlib import Path
from functools import lru_cache
import pygame as pg

@lru_cache
def loadFlag(color, size):
    surf = _FLAGS[color]
    return pg.transform.smoothscale(surf, size).convert()

@lru_cache
def loadFont(size):
    return pg.font.Font(str(DIR / "Formula1_Display-Regular.otf"), size)
    
DIR = (Path.cwd() / sys.argv[0]).parent / "resources"
ICON = pg.image.load(str(DIR / "icon.png"))
_FLAG_SHEET = pg.image.load(str(DIR / "flags.png"))

_FLAGS = {
    "BLACK": _FLAG_SHEET.subsurface((0, 0, 86, 86)), 
    "RED":   _FLAG_SHEET.subsurface((86, 0, 86, 86)),  
    "BLUE":  _FLAG_SHEET.subsurface((86*2, 0, 86, 86)), 
}
