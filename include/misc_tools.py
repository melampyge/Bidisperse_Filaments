
""" A set of commonly used general helper functions"""

### 

##############################################################################

import numpy as np
import math

##############################################################################

def nearbyint(x):
    """ Round to the nearby integer"""
    
    if x >= 0:
        return math.floor(x+0.5)
    else:
        return math.floor(x-0.5)

##############################################################################
    
def min_img_dist(x1, x2, lx):
    """ compute the minimum image distance between two positions"""
    
    dx = x2 - x1 
    return dx-nearbyint(dx/lx)*lx

##############################################################################

def coords_per_pols(x, y, nbpp):
    """ get the coordinates of beads in terms of polymers"""
    
    splitter = np.cumsum(nbpp)[:-1]
    x_per_pol = np.split(x, splitter, axis=1)
    y_per_pol = np.split(y, splitter, axis=1)
    
    return x_per_pol, y_per_pol
        
##############################################################################

def calc_velocities(x, d, dt):
    """ calculate the velocities"""
    
    return (x[d:, :, :] - x[:-d, :, :])/dt
    
##############################################################################

def get_img_pos(x, lx):
    """ get the image position in the central box 
    -- can be numpy array or single pos"""

    return x-np.floor(x/lx)*lx
    
##############################################################################
    