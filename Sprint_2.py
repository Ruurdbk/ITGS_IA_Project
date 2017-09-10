# -*- coding: utf-8 -*-
"""
Created on Tue Jun 27 15:07:58 2017

@author: Ruurd
"""
#Import libraries
from timeit import default_timer as timer
import os

#Set efficiency statistics to True or False for slow or fast execution
efficiency_statistics = True


#Def functions:
def convertNed2Xyz( name, in_file, out_file):
    "coverts NED to XYZ"
    global soundings_number
    #open input file
    in_file_obj = open(in_file+name,"r")
    #create output file
    name=name[:-3]+'xyz'
    out_file_obj = open(out_file+name, "w")
    
    for line in in_file_obj:
        ned_sounding = line.split(in_delimiter)
        xyz_sounding = ned_sounding[E]+out_delimiter+ned_sounding[N]+out_delimiter+"-"+ned_sounding[D]
        out_file_obj.write(xyz_sounding)
        if efficiency_statistics:
            soundings_number = soundings_number + 1
    
    #close files
    in_file_obj.close()
    out_file_obj.close()
    return

#Def functions:
def find_ned( in_path ):
    "This finds the .NED files in the directory"
    files = os.listdir( in_path )
    ned = []
    for file in files:
        if file.endswith(".NED"):
            ned.append(file)
    return ned

#Def functions:
def effstat():
    "calculate and print eff stats"
    print("Efficiency statistics is", efficiency_statistics)
    end = timer()
    used_time = end - start
    #Show efficiency statistcs
    sounding_per_second = round(soundings_number/used_time)
    print("Total number of depth soundings:", soundings_number)
    print("Total time: {0:.2f}".format(used_time), "seconds")
    print("Soundings per second:", sounding_per_second)

# set input file name and directory

# "D3470_grid05_geo" for testing, "D4073_grid05_geo" for large file testing 
#in_path = "C:\\Users\\ruurd\\Documents\\IB1\\ITGS\\Python_Project_data\\data\\in\\"
in_path = "C:\\Users\\ruurd\\Documents\\IB1\\ITGS\\Python_Project_data\\data\\in\\"


# set output file name and directory
#out_path = "C:\\Users\\ruurd\\Documents\\IB1\\ITGS\\Python_Project_data\\data\\out\\"
out_path = "C:\\Users\\ruurd\\Documents\\IB1\\ITGS\\Python_Project_data\\data\\out\\"
out_delimiter =";"

# set input file delimiter and columns
# values used here represent the .NED format used internally by the NHS 
in_delimiter = " "
N=0 # first column is North in decimal degrees
E=1 # second column is Easting in decimal degrees
D=2 # third and last column is depth, in meters and centimeters

#=============
#Start Program
#=============

# start timer
if efficiency_statistics:
    start = timer()
    soundings_number = 0 
    
#Search directory for NED files
nedfiles = find_ned( in_path )

#For each NED file in directory, convert to xyz file.
for nedfile in nedfiles:
    convertNed2Xyz (nedfile, in_path, out_path)
    print (nedfile + " converted to xyz")

#Show efficiency statistics:
if efficiency_statistics:
    effstat()
    
#=============
#End Program
#=============
