#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  2 21:33:36 2020

@author: daniel
"""


from neuralnets import NeuralNet
import numpy as np

class Bird:
    def __init__(self, x_pos = 200, y_pos = 100, g = 1, upforce = -10, max_speed = 10, size = 5):
        
        self.y_pos = y_pos
        self.x_pos = x_pos
        self.g = g
        self.upforce = upforce
        self.size = size
        self.acceleration = 0
        self.velocity = 0
        self.max_speed = max_speed
        self.color = (255,255,255)
        self.nn = NeuralNet()
        self.frames = 0
        self.alive = True
        self.started = False
        
    def update(self, obstacles):
        if self.started:
            closest = self.find_closest_obstacle(obstacles)
            self.check_collision(closest)
            self.observe(closest)
            self.acceleration += self.g
            self.velocity += self.acceleration
            self.velocity = min(self.velocity, self.max_speed)
            self.velocity = max(self.velocity, -self.max_speed)
            self.y_pos += self.velocity           
            self.acceleration *= 0
            self.frames += 1
            
    def find_closest_obstacle(self, obstacles):
        return [obstacle for obstacle in obstacles if (obstacle.pos + obstacle.width - self.x_pos >= 0)][0]
    
    def check_collision(self, obstacle):
        if (self.y_pos - self.size <= 20 or self.y_pos + self.size >= 590)\
        or ((self.x_pos + 3*self.size >= obstacle.pos) and (self.x_pos - self.size <= obstacle.pos + obstacle.width))\
        and ((self.y_pos - self.size <= obstacle.lower_edge) or (self.y_pos + self.size >= obstacle.lower_edge + obstacle.gap_size)):
            self.alive = False
            
    def observe(self, obstacle):
        world = np.array([[self.velocity, self.y_pos, obstacle.lower_edge, obstacle.gap_size, obstacle.pos]])
        flap = self.nn.model.predict(world)
        if flap > 0.5:
            self.flap()
               
    def flap(self):
        if not self.started:
            self.started = True
        if self.velocity > 0:
            self.velocity *= 0
        self.acceleration += self.upforce