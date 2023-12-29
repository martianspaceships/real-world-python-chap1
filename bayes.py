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

MAP_FILE = 'cape_python.png'

SA1_corners = (130, 265, 180, 315)  # (UL-X, UL-Y, LR-X, LR-Y)
SA2_corners = (80, 255, 130, 305)  # (UL-X, UL-Y, LR-X, LR-Y)
SA3_corners = (105, 205, 155, 255)  # (UL-X, UL-Y, LR-X, LR-Y)
