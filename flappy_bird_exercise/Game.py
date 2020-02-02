#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  2 21:27:43 2020

@author: daniel
"""

import pygame
import numpy as np
from Bird import Bird

class Game:
    def __init__(self):
        
        self.running = False
        self.width = 800
        self.height = 600
        self.display = pygame.display.set_mode([self.width, self.height])
        self.clock = pygame.time.Clock()
        
        self.bird = Bird(pos = self.height//2)
        
    def run(self):
        self.running = True
        while self.running:
            
            self.bird.update()
            self.draw()
            self.clock.tick(30)
            
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.bird.flap()
                
                elif event.type == pygame.QUIT:
                    self.running  = False
        
        print("Done")
        pygame.quit()
        
    def draw(self):
        self.display.fill([0,0,0])
        pygame.draw.circle(self.display, (255,255,255), [200, int(self.bird.pos)], 5)
        
        pygame.display.update()

if __name__ == "__main__":
    game = Game()
    game.run()