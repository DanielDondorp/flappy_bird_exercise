#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  3 08:06:51 2020

@author: daniel
"""

import numpy as np

class Barrier:
    def __init__(self, pos = 500, scroll_speed = 5, gap_range = [100,400], width = 20, gap_size = 100):
        self.scroll_speed = scroll_speed
        self.lower_edge = np.random.randint(gap_range[0], gap_range[1])
        self.pos = pos
        self.width = width
        self.gap_size = gap_size
        
        self.passed = False
        
    def update(self):
        self.pos -= self.scroll_speed
        