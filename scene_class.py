#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  3 20:35:41 2021

@author: matt
"""

class scene: 
    def __init__(self, scene_no = [], int_ext = [], place = None, day_night = None, characters = None, loc = None, stripboard = None):
        self.scene_no = scene_no
        self.int_ext = int_ext
        self.place = place
        self.day_night = day_night
        self.characters = characters
        self.loc = loc
        self.stripboard = stripboard
        