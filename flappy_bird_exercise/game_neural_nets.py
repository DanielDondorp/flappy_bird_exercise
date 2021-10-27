#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 10:43:40 2020

@author: daniel
"""

# !/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  2 21:27:43 2020

@author: daniel
"""

import pygame
from bird import Bird
from barrier import Barrier

import numpy as np


class Game:
    def __init__(self):

        # pygame.init()
        # pygame.font.init()
        self.running = False
        self.game_over = False
        self.width = 800
        self.height = 600
        self.gap_size = 100
        self.distance_between_obstacles = 250
        self.bird_x_pos = 200
        # self.display = pygame.display.set_mode([self.width, self.height])
        # self.clock = pygame.time.Clock()

        self.game_number = 0
        self.high_score = 0
        self.score = 0
        self.make_world()
        # self.make_game_over_screen()

    def make_world(self):
        self.birds = [Bird(y_pos=self.height // 2, size=15, upforce=-10) for _ in range(10)]
        self.dead_birds = []
        for bird in self.birds:
            bird.started = True
        self.obstacles = [Barrier(pos=self.width, width=50)]
        self.high_score = np.max([self.score, self.high_score])
        self.score = 0
        self.game_number += 1

    def run(self):
        self.running = True
        while self.running:
            if not self.game_over:
                # update the position of the bird
                if len(self.birds) > 0:
                    for bird in self.birds:
                        if bird.alive:
                            bird.update(self.obstacles)
                            self.update_obstacles()
                        else:
                            bird.alive = False
                            self.dead_birds.append(bird)
                            self.birds.remove(bird)
                else:
                    self.game_over = True
                    print([bird.frames for bird in self.dead_birds])
                    self.running == False
                    break
                self.update_obstacles()
        print("Done")

    def update_obstacles(self):
        for obstacle in self.obstacles:
            obstacle.update()
            # Add new obstacles if needed
        if self.obstacles[-1].pos <= self.width:
            self.obstacles.append(Barrier(pos=self.width + self.distance_between_obstacles, width=50))

        # Remove old obstacles if needed
        if self.obstacles[0].pos + self.obstacles[0].width <= -50:
            self.obstacles.remove(self.obstacles[0])

if __name__ == "__main__":
    game = Game()
    game.run()
