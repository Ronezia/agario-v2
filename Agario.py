import pygame

import core
from creep import Creep
from avatar import Avatar
from pygame.math import Vector2

def setup():
    print("Setup START----------")

    core.fps = 30
    core.WINDOW_SIZE = [1200, 800]
    core.memory("c",Creep())
    core.memory("a",Avatar())
    core.memory("listCreep",[])
    core.memory("nbrCreep",100)


    for i in range(0,core.memory("nbrCreep")):
        core.memory("listCreep").append(Creep())
    print("Setup END----------")


def edge():
'''''
    if core.memory("a").position.y+ core.memory("a").rayon > core.WINDOW_SIZE[1]:
        core.memory("a").position =  Vector2(core.memory("a").position.x,core.WINDOW_SIZE[1]-core.memory("a").rayon)
        core.memory("a").position = Vector2(core.memory("a").position.y,core.WINDOW_SIZE[1]-core.memory("a").rayon)

    if core.memory("a").position.y- core.memory("a").rayon > core.WINDOW_SIZE[1]:
        core.memory("a").position =  Vector2(core.memory("a").position.x,core.WINDOW_SIZE[1]-core.memory("a").rayon)
        core.memory("a").position = Vector2(core.memory("a").position.y,core.WINDOW_SIZE[1]-core.memory("a").rayon)

    if core.memory("a").position.x+ core.memory("a").rayon > core.WINDOW_SIZE[1]:
        core.memory("a").position =  Vector2(core.memory("a").position.x,core.WINDOW_SIZE[1]-core.memory("a").rayon)
        core.memory("a").position = Vector2(core.memory("a").position.y,core.WINDOW_SIZE[1]-core.memory("a").rayon)

    if core.memory("a").position.x- core.memory("a").rayon > core.WINDOW_SIZE[1]:
        core.memory("a").position =  Vector2(core.memory("a").position.x,core.WINDOW_SIZE[1]-core.memory("a").rayon)
        core.memory("a").position = Vector2(core.memory("a").position.y,core.WINDOW_SIZE[1]-core.memory("a").rayon)
'''



def run ():
    core.cleanScreen()



    for moncreep in core.memory("listCreep"):
        moncreep.show(core.screen)

    core.memory("a").moov(core.getMouseLeftClick())
    edge()
    core.memory("a").show()


core.main(setup, run)
