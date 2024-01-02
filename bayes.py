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
        
    def sailor_final_location(self, num_search_areas):
        """Return the actual x,y location of the missing sailor."""
        # Find sailor coordinates with respect to any Search Area subarray. Since they are all the same size, using sa1 is okay
        self.sailor_actual[0] = np.random.choice(self.sa1.shape[1], 1) # choose 1 item from the coloumns
        self.sailor_actual[1] = np.random.choice(self.sa1.shape[0], 1) # choose 1 item from the rows
        
        area = int(random.triangular(1, num_search_areas + 1)) # use a local variable here, area, instead of self.area since no other function/method needs it globally

        if area == 1:
            x = self.sailor_actual[0] + SA1_CORNERS[0]
            y = self.sailor_actual[1] + SA1_CORNERS[1]
            self.area_actual = 1
        elif area == 2:
            x = self.sailor_actual[0] + SA1_CORNERS[0]
            y = self.sailor_actual[1] + SA1_CORNERS[1]
            self.area_actual = 2
        elif area == 3:
            x = self.sailor_actual[0] + SA1_CORNERS[0]
            y = self.sailor_actual[1] + SA1_CORNERS[1]
            self.area_actual = 3
        return x, y

    def calc_search_effectiveness(self):
        """Set decimal search effectiveness value per search area."""
        self.sep1 = random.uniform(0.2, 0.9)
        self.sep2 = random.uniform(0.2, 0.9)
        self.sep3 = random.uniform(0.2, 0.9)
        
    def conduct_search(self, area_num, area_array, effectiveness_prob):
        """Return search results and list of searched coordinates."""
        local_y_range = range(area_array.shape[0])
        local_x_range = range(area_array.shape[1])
        coords = list(itertools.product(local_x_range, local_y_range)) # create a list of all possible combos
        random.shuffle(coords) # shuffle the list so that the same x,y isn't always searched
        coords = coords[:int((len(coords)*effectiveness_prob))]
        loc_actual = (self.sailor_actual[0], self.sailor_actual[1])
        if area_num ++ self.area_actual and loc_actual in coords: # compare the search area with the coords of the actual sailor's x,y pos
            return 'Found in Area {}.'.format(area_num), coords
        else:
            return 'Not Found', coords
        
    def revise_target_probs(self):
        """Update area target probabilities based on search effectiveness."""
        denom = self.p1 * (1 - self.sep1) + self.p2 * (1 - self.sep2) + self.p3 * (1 - self.sep3)
        self.p1 = self.p1 * (1 - self.sep1) / denom
        self.p2 = self.p2 * (1 - self.sep2) / denom
        self.p3 = self.p3 * (1 - self.sep3) / denom
    
    def draw_menu(search_num):
        """Print menu of choices for conducting area searches."""
        print('\nSearch {}'.format(search_num))
        print(
            """
            Choose next areas to search:
            
            0 - Quit    
            1 - Search Area 1 twice
            2 - Search Area 2 twice
            3 - Search Area 3 twice
            4 - Search Areas 1 & 2
            5 - Search Areas 1 & 3
            6 - Search Areas 2 & 3
            7 - Start Over
            """
            )
        

        
        
        
        