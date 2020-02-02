#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  2 21:33:36 2020

@author: daniel
"""


class Bird:
    def __init__(self, pos = 100, g = 1, upforce = -10, max_speed = 10):
        
        self.pos = pos
        self.g = g
        self.upforce = upforce
        
        self.acceleration = 0
        self.velocity = 0
        self.max_speed = max_speed
        
        self.started = False
        
    def update(self):
        if self.started:
            self.acceleration += self.g
            self.velocity += self.acceleration
            self.velocity = min(self.velocity, self.max_speed)
            self.pos += self.velocity
            
            self.acceleration *= 0
        
    def flap(self):
        if not self.started:
            self.started = True
        if self.velocity > 0:
            self.velocity *= 0
        self.acceleration += self.upforce