# -*- coding: utf-8 -*-
"""
Created on Fri Dec 29 10:39:34 2023

@author: space
"""

import sys
import random
import itertools
import numpy as np
import cv2 as cv

MAP_FILE = 'D:/42_Amie Projects/Python/Real World Python/chap1/cape_python.png'

SA1_CORNERS = (130, 265, 180, 315)  # (UL-X, UL-Y, LR-X, LR-Y) SA reps search area
SA2_CORNERS = (80, 255, 130, 305)  # (UL-X, UL-Y, LR-X, LR-Y) SA reps search area
SA3_CORNERS = (105, 205, 155, 255)  # (UL-X, UL-Y, LR-X, LR-Y) SA reps search area

class Search():
    """Bayesian Search & Rescue game with 3 search areas."""
    
    def __init__(self, name):
        self.name = name
        self.img = cv.imread(MAP_FILE, cv.IMREAD_COLOR)
        if self.img is None:
            print('Could not load map file {}'.format(MAP_FILE), file=sys.stderr)
            sys.exit(1)
            
        self.area_actual = 0
        self.sailor_actual = [0, 0] # As 'local' coords within search area
        
        self.sa1 = self.img[SA1_CORNERS[1] : SA1_CORNERS[3], SA1_CORNERS[0] : SA1_CORNERS[2]] # sa upper y, lower y; then upper x, and lower x (notice how these are y first, then x unlike normal cartesian); same for the next to sa's
        
        self.sa2 = self.img[SA2_CORNERS[1] : SA2_CORNERS[3], SA2_CORNERS[0] : SA2_CORNERS[2]]
        
        self.sa3 = self.img[SA3_CORNERS[1] : SA3_CORNERS[3], SA3_CORNERS[0] : SA3_CORNERS[2]]
        
        #the following sets the intial probabilities for finding the sailor in eac of the sa's
        self.p1 = 0.2
        self.p2 = 0.5
        self.p3 = 0.3
        
        #Then set the initial search effectiveness probabilities, SEP
        self.sep1 = 0
        self.sep2 = 0
        self.sep3 = 0

    def draw_map(self, last_known):
        """Display basemap with scale, last known xy location, search areas."""
        # Draw a line for the scale
        cv.line(self.img, (20, 370), (70, 370), (0, 0, 0), 2) # args: a pair of x,y coords, color tuple, line width
        cv.putText(self.img, '0', (8, 370), cv.FONT_HERSHEY_PLAIN, 1, (0, 0, 0)) # map scale label
        cv.putText(self.img, '50 Nautical Miles', (71, 370), cv.FONT_HERSHEY_PLAIN, 1, (0, 0, 0)) #map scale label
        
        # draw rectangles for each of the three search areas along with a numbered label for each SA
        cv.rectangle(self.img, (SA1_CORNERS[0], SA1_CORNERS[1]), (SA1_CORNERS[2], SA1_CORNERS[3]), (0, 0, 0), 1)
        cv.putText(self.img, '1', (SA1_CORNERS[0] + 3, SA1_CORNERS[1] + 15), cv.FONT_HERSHEY_PLAIN, 1, 0)
        cv.rectangle(self.img, (SA2_CORNERS[0], SA2_CORNERS[1]), (SA2_CORNERS[2], SA2_CORNERS[3]), (0, 0, 0), 1)
        cv.putText(self.img, '2', (SA2_CORNERS[0] + 3, SA2_CORNERS[1] + 15), cv.FONT_HERSHEY_PLAIN, 1, 0)
        cv.rectangle(self.img, (SA3_CORNERS[0], SA3_CORNERS[1]), (SA3_CORNERS[2], SA3_CORNERS[3]), (0, 0, 0), 1)
        cv.putText(self.img, '3', (SA3_CORNERS[0] + 3, SA3_CORNERS[1] + 15), cv.FONT_HERSHEY_PLAIN, 1, 0)
        
        # indicate last know position
        cv.putText(self.img, '+', (last_known), cv.FONT_HERSHEY_PLAIN, 1, (0, 0, 255))
        cv.putText(self.img, '+ = Last Known Position', (274, 355), cv.FONT_HERSHEY_PLAIN, 1, (0, 0, 255))
        cv.putText(self.img, '* = Actual Position', (275, 370), cv.FONT_HERSHEY_PLAIN, 1, (255, 0, 0))
        
        # Show the base map and move it, wait .5 sec before the next action (in this case showing the menu)
        cv.imshow('Search Area', self.img) # show the base map and call it Search Area
        cv.moveWindow("Search Area", 750, 10)
        cv.waitKey(500)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        

        
        
        
        
        
        
        
        
        
        
        
        
        
        