import random
from turtle import position

import pygame
from pygame.math import Vector2

import core


class Avatar:
    def __init__(self):
        self.position = Vector2(600,400)
        self.rayon = 50
        self.nouriture = 1
        self.couleur = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
        self.masse = 100
        self.vitesse = Vector2(0, 0)
        self.acceleration = Vector2(0, 0)
        self.maxacc = 0.1
        self.l0 = 10
        self.k = 0.001
        self.vitessmin = 0
        self.vitessmax = 5
        self.taillemax = 300
        #self.vecteur = (0, 200)

    def moov(self , destination):
        if destination is not None:
            #F=uk|l-lo|
            l=self.position.distance_to(destination)
            u=destination - self.position
            u=u.normalize()
            self.acceleration=u*self.k*abs(l-self.l0)
            print(self.acceleration)

        #bilan des force


        #attention max force
        if self.acceleration.length() > self.maxacc:
            self.acceleration.scale_to_length(self.maxacc)


        #ajout de F a la vitess
        self.vitesse = self.vitesse + self.acceleration

        #attention max vitess
        if self.vitesse.length()>self.vitessmax:
            self.vitesse.scale_to_length(self.vitessmax)

        #ajout vitesse a position
        self.position = self.position + self.vitesse

        #remise a zero de F
        self.acceleration = Vector2(0,0)


    def show(self):
        core.Draw.circle(self.couleur,self.position,self.rayon)

