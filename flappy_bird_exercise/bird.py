#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  2 21:33:36 2020

@author: daniel
"""

from neuralnets import NeuralNet
import numpy as np

class Bird:
    def __init__(self, pos = 100, x_pos = 200, g = 1, upforce = -10, max_speed = 10, size = 5, nn = None):
        
        self.pos = pos
        self.x_pos = x_pos
        self.g = g
        self.upforce = upforce
        self.size = size
        self.acceleration = 0
        self.velocity = 0
        self.max_speed = max_speed        
        self.frames = 0
        if nn == None:
            self.nn = NeuralNet()
        
        self.started = False
        
    def update(self, obstacles):
        if self.started:            
            self.acceleration += self.g
            self.velocity += self.acceleration
            self.velocity = min(self.velocity, self.max_speed)
            self.velocity = max(self.velocity, -self.max_speed)
            self.pos += self.velocity
            self.acceleration *= 0
            self.frames += 1
            closest_obstacle = [obstacle for obstacle in obstacles if obstacle.pos > self.x_pos][0]
            self.perceive(closest_obstacle)
#            if self.frames % 15 == 0:
#                self.flap()
    def perceive(self, obstacle):
        
        dist_to_obstacle = obstacle.pos - self.x_pos
        edge = obstacle.lower_edge
        
        world = [[dist_to_obstacle, edge, self.pos, self.velocity, self.acceleration]]
        
        if self.nn.model.predict(world)[0][0] > 0.5:
            self.flap()
                
    def flap(self):
        if not self.started:
            self.started = True
        if self.velocity > 0:
            self.velocity *= 0
        self.acceleration += self.upforce