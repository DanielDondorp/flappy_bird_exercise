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
        
        pygame.init()
        pygame.font.init()
        self.running = False
        self.game_over = False
        self.width = 800
        self.height = 600
        self.gap_size = 100
        self.distance_between_obstacles = 250
        self.bird_x_pos = 200
        self.display = pygame.display.set_mode([self.width, self.height])
        self.clock = pygame.time.Clock()
         
        self.game_number = 0
        self.high_score = 0
        self.score = 0
        self.make_world()
        self.make_game_over_screen()
        
        
    def make_world(self):
        self.bird = Bird(pos = self.height//2, size = 10)
        self.obstacles = [Barrier(pos = self.width)]
        self.high_score = self.score
        self.score = 0
        self.game_number += 1
        
        
    def run(self):
        self.running = True
        while self.running:
            if not self.game_over:
                #update the position of the bird
                self.bird.update()
                self.update_obstacles()
                
                self.make_score_text()

                #handle pygame events/keypresses
                for event in pygame.event.get():
                    #if spacebar is pressed, flap the bird.
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE:
                            self.bird.flap()
                    
                    elif event.type == pygame.QUIT:
                        self.running  = False
                        pygame.quit()

            else:
                for event in pygame.event.get():
                    #if spacebar is pressed, restart the game
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE:
                            self.game_over = False
                            self.make_world()
                            self.run()
                    
                    elif event.type == pygame.QUIT:
                        self.running  = False
                        pygame.quit()
                    
            #draw all objects
            self.draw()
            #advance the frame, limit to 30 fps
            self.clock.tick(30)
        
    def draw(self):
        if not self.game_over:
            self.display.fill([0,0,0])
            pygame.draw.circle(self.display, (255,255,255), [self.bird_x_pos, int(self.bird.pos)], self.bird.size)
            
            for obstacle in self.obstacles:
                pygame.draw.line(self.display, (255,255,255), [int(obstacle.pos), 0],
                                                              [int(obstacle.pos), obstacle.lower_edge], obstacle.width)
                pygame.draw.line(self.display, (255,255,255), [int(obstacle.pos), obstacle.lower_edge + self.gap_size],
                                                              [int(obstacle.pos), self.height], obstacle.width)
            self.display.blit(self.score_text, self.score_text_rect)
        else:
            self.display.blit(self.game_over_text, self.textRect)            
        pygame.display.update()
        
        
    def update_obstacles(self):
        if self.bird.pos > self.height-10 or self.bird.pos < 10:
            self.game_over = True
        else:
            for obstacle in self.obstacles:
                #check if bird hits obstacle
                if obstacle.pos <= self.bird_x_pos + (2*self.bird.size)-1 and obstacle.pos + obstacle.width >= self.bird_x_pos - (2*self.bird.size)-1:
                    #check if bird through gap
                    if self.bird.pos - (self.bird.size//2)  <= obstacle.lower_edge or self.bird.pos + (self.bird.size+2) >= obstacle.lower_edge+self.gap_size:
                        self.game_over = True
                #if passed, score point
                if obstacle.pos + obstacle.width < self.bird_x_pos and not obstacle.passed:
                        obstacle.passed = True
                        self.score += 1
                obstacle.update()
            #Add new obstacles if needed
            if self.obstacles[-1].pos <= self.width:
                self.obstacles.append(Barrier(pos = self.width + self.distance_between_obstacles))
            
            #Remove old obstacles if needed
            if self.obstacles[0].pos + self.obstacles[0].width <= -50:
                self.obstacles.remove(self.obstacles[0])

            
    def make_game_over_screen(self):
        self.font = pygame.font.SysFont(None, 38)
        self.game_over_text = self.font.render("Game Over!", True, (255,255,255), (0,0,0))
        self.textRect = self.game_over_text.get_rect()
        self.textRect.center = (self.width//2, self.height//2)

    def make_score_text(self):
        self.font = pygame.font.SysFont(None, 18)
        self.score_text = self.font.render(f"Game: {self.game_number} High score: {self.high_score} score: {self.score}", True, (255,255,255), (0,0,0))
        self.score_text_rect = self.score_text.get_rect()
        self.score_text_rect.topright = (self.width, 0)
        

        

if __name__ == "__main__":
    game = Game()
    game.run()