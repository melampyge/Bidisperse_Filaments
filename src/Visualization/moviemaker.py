#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 10 17:17:15 2017

@author: duman
"""

""" combine snapshots to render a movie with ffmpeg"""

### example command line arguments: 
###    -i=/local/duman/Bidisperse_Filaments/IMAGES/.../ 
###    -s=/usr/users/iff_th2/duman/Bidisperse_Filaments/MOVIES/.../

##############################################################################

import subprocess
import os
import argparse

##############################################################################

def order_files(folder):
    """ order the filenames for ffmpeg to work,
    ordering in the sense that frame numbers should go from 0 onwards"""

    ### change/order the filenames for ffmpeg to work
    
    final_vid = 1
    enum = []
    
    if 1 == final_vid:
    	
      ### go through each file inside the folder
      # get the numeric part inside the filename
      # a filename being something like:
      # frame-00010.png or frame-000100.png
      # make a list of numeric part of the file and filename for each file
      # sort the list according to the value in the numeric part
      
    	for ff in os.listdir(folder):	
    	
         if ".png" == ff[-4:] and "frame" == ff[0:5]:
            if "." == ff[11]:
                num = int(ff[6:11])
            elif "." == ff[12]:
                num = int(ff[6:12])
            elif "." == ff[13]:
                num = int(ff[6:13])
            elif "." == ff[14]:
                num = int(ff[6:14])
            enum.append([num, ff])
    
         enum = sorted(enum, key=lambda x:x[0])
    
      ### rename all the files starting from 0 onwards
      
    	for i in range(0, len(enum)):
    		os.rename(folder+enum[i][1], folder+"frame-"+ "%05d" % i +".png")
      
    return
      
##############################################################################

def gen_video(folder, savefolder):
    """ generate the video with ffmpeg""" 	
    
    ### generate the video 
    
    os.system('mkdir -p ' + savefolder)
    v_name = savefolder + 'detailed.mp4'

    # -r : framerate(fps), -s is resoluation
    # -i is input %04 is to pad with zeros until 4th string pic0001, pic0002, pic0020, ...
    # -crf is quality, the lower the better
    # pix_fmt is the pixel format
    # -y is to force overwrite

#    subprocess.call(['ffmpeg','-r','40','-f','image2','-s','720:720','-i',folder+'frame-%05d.png','-y',
#                     '-vcodec','libx264','-crf','25','-pix_fmt','yuv420p','-vf','scale=720:-1',v_name])
    subprocess.call(['ffmpeg','-f','image2','-s','720:720','-i',folder+'frame-%05d.png','-y',
                     '-vcodec','libx264','-crf','25','-pix_fmt','yuv420p','-vf','scale=720:-1',v_name])  
#    subprocess.call(['ffmpeg','-f','image2','-s','720:720','-i',folder+'frame-%05d.png','-y',
#                     '-vcodec','libx264','-crf','25','-pix_fmt','yuv420p','-vf','scale=720:trunc(ow/a/2)*2',v_name])  

    return

##############################################################################

def main():

    ### get the data folder
    
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--imagefolder", \
                        help="Folder containing images, as in /local/duman/Bidisperse_Filaments/IMAGES/.../")
    parser.add_argument("-s", "--savefolder", \
                        help="Folder to save the movie, as in /usr/users/iff_th2/duman/Bidisperse_Filaments/MOVIES/.../")                        
    args = parser.parse_args()
    
    ### generate the video in the given folder

    order_files(args.imagefolder)
    gen_video(args.imagefolder, args.savefolder)
    
    return
    
##############################################################################

if __name__ == '__main__':
    main()

##############################################################################