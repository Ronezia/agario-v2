import core
from creep import Creep
from avatar import Avatar
from pygame.math import Vector2

def setup():
    print("Setup START----------")

    core.fps = 30
    core.WINDOW_SIZE = [1400, 850]
def run ():
    core.cleanScreen()
    print(core.getkeyPressValue())

core.main(setup, run)