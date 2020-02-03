#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  2 21:27:43 2020

@author: daniel
"""

import pygame
from bird import Bird
from barrier import Barrier

class Game:
    def __init__(self):
        
        self.running = False
        self.width = 800
        self.height = 600
        self.display = pygame.display.set_mode([self.width, self.height])
        self.clock = pygame.time.Clock()
        
        self.bird = Bird(pos = self.height//2)
        
        self.obstacles = [Barrier(pos = self.width+300)]
        
    def run(self):
        self.running = True
        while self.running:
            
            self.bird.update()
            
            for obstacle in self.obstacles:
                obstacle.update()
            
            if self.obstacles[-1].pos <= self.width:
                self.obstacles.append(Barrier(pos = self.width+300))
            
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
        
        for obstacle in self.obstacles:
            pygame.draw.line(self.display, (255,255,255), [int(obstacle.pos), 0],
                                                          [int(obstacle.pos), obstacle.lower_edge], 20)
            pygame.draw.line(self.display, (255,255,255), [int(obstacle.pos), obstacle.lower_edge+50],
                                                          [int(obstacle.pos), self.height], 20)
        
        pygame.display.update()

if __name__ == "__main__":
    game = Game()
    game.run()