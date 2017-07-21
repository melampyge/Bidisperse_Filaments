#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 10 16:31:55 2017

@author: duman
"""

""" Data types and functions for plotting"""

### 

##############################################################################

import argparse
import numpy as np
import os
import matplotlib as mpl
mpl.use('Agg', warn=False)
import matplotlib.pyplot as plt
import read_write
import misc_tools 
import data_separator

import seaborn as sns
sns.set(style="white",context='paper',
        font_scale=1.2,font="Open Sans",
        rc={'mathtext.default': 'regular','font.size': 30, 
            'font.family': 'sans',"figure.dpi":300,
            "xtick.major.size": 8, "ytick.major.size": 8,
            'grid.linestyle': '--'})   
        
##############################################################################

class Subplots:
    """ subplots structure"""
    
    totcnt = -1             # Total number of subplots -- static member
    
    def __init__(self, f, l, s, b, t):
        self.fig = f        # Figure axes handle
        self.length = l     # Length of the subplot box 
        self.sep = s        # Separation distance between subplots 
        self.beg = b        # Beginning (offset) in the figure box
        self.tot = t        # Total number of subplots in the x direction
        
        return
        
    def addSubplot(self):
        """ add a subplot in the grid structure"""
        
        ## increase the number of subplots in the figure
        
        self.totcnt += 1
        
        ## get indices of the subplot in the figure
        
        self.nx = self.totcnt%(self.tot)
        self.ny = self.totcnt/(self.tot)
        
        self.xbeg = self.beg + self.nx*self.length + self.nx*self.sep
        self.ybeg = self.beg + self.ny*self.length + self.ny*self.sep
        
        return self.fig.add_axes([self.xbeg,self.ybeg,self.length,self.length])

##############################################################################

class GeneralPlot(Subplots):
    """ general plot structure"""
    
    def __init__(self, num_ticks=5, 
                 ax_len=1.0, ax_b=0.0, 
                 ax_sep=0.0, total_subplots_in_x=1):
    
        self.fig = plt.figure()
        Subplots.__init__(self, self.fig, \
                          ax_len, ax_sep, ax_b, total_subplots_in_x)
        self.ax0 = self.addSubplot()
        
        return
        

    def plot_2d(self, x, y, sims, savebase, analysisname, \
                xlab, ylab, title, legend, param_choice, savepdf):
        """ plot 2D analysis data with 1 control parameter as legend"""
        
        os.system("mkdir -p " + savebase)
        savepath = savebase + analysisname
    
        keys = np.sort(sims.keys())
        for key in keys:
            xp = x[key]
            yp = y[key] 
            print xp
            print yp
            sim = sims[key]
                
            legend, title = data_separator.gen_labels_for_fils(param_choice, sim)
            
            label = legend + "=" + str(key)
            line0 = self.ax0.plot(xp, yp, \
                                 linewidth=2.0, label=label)
            
        ### scales
        
        self.ax0.set_xscale('log')
        self.ax0.set_yscale('log')
        
        ### title
        
        self.ax0.set_title(title, fontsize=30)
        
        ### labels
    
        self.ax0.set_xlabel(xlab, fontsize=40)
        self.ax0.set_ylabel(ylab, fontsize=40)
    
        ### limits
    
        #self.ax0.set_xlim((full_box_downlim, full_box_uplim))
        #self.ax0.set_ylim((full_box_downlim, full_box_uplim))
        
        ### ticks
        
        #self.ax0.xaxis.set_ticks(full_box_ticks)
        #self.ax0.yaxis.set_ticks(full_box_ticks)
        self.ax0.tick_params(axis='both', which='major', labelsize=30)    
    
        ### legend
    
        self.ax0.legend(bbox_to_anchor=(0.005, 0.,0.65, 1.), loc=2, borderaxespad=0., \
            prop={'size': 20}, mode="expand", frameon=False)
            
        ### save 
    
        if savepdf:
            plt.savefig(savepath+".pdf", dpi=300, bbox_inches='tight', pad_inches=0.08)
        else:            
            plt.savefig(savepath+".png", dpi=300, bbox_inches='tight', pad_inches=0.08)
            
        self.fig.clf()
        plt.close()
            
        return
        
##############################################################################
 
       