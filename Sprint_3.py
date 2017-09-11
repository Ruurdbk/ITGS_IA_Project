# -*- coding: utf-8 -*-
"""
Created on Sun Sep 10 16:15:00 2017

@author: Ruurd
"""
#Import libraries
from timeit import default_timer as timer
from datetime import datetime
import os

#Set efficiency statistics to True or False for slow or fast execution
efficiency_statistics = True
metadata_logging = True


#Def functions:
def convertNed2Xyz( name, in_file, out_file):
    "coverts NED to XYZ"
    sounding_local = 0
    global soundings_number
    #open input file
    in_file_obj = open(in_file+name,"r")
    #create output file
    name=name[:-3]+'xyz'
    out_file_obj = open(out_file+name, "w")

    #Convert every line in files:   
    for line in in_file_obj:
        ned_sounding = line.split(in_delimiter)
        xyz_sounding = ned_sounding[E]+out_delimiter+ned_sounding[N]+out_delimiter+"-"+ned_sounding[D]
        out_file_obj.write(xyz_sounding)

        #Include efficiency statistics
        if efficiency_statistics:
            soundings_number = soundings_number + 1

        #Include metadata logging
        if metadata_logging:
            sounding_local = sounding_local + 1
            x = float(ned_sounding[E])
            y = float(ned_sounding[N])
            z = float(ned_sounding[D]) * -1

            #Find min and max range of X, Y, Z
            if sounding_local == 1:
                max_x = x
                min_x = x
                max_y = y
                min_y = y
                max_z = z
                min_z = z
            else:
                if x > max_x:
                    max_x = x
                elif x < min_x:
                    min_x = x
                if y > max_y:
                    max_y = y
                elif y < min_y:
                    min_y = y
                if z > max_z:
                    max_z = z
                elif z < min_z:
                    min_z = z

#Print metadata loggin in both program and log file    
    if metadata_logging:
        log_file_obj = open(out_file+log_file, "a")
        print()
        print("Metadata for NED file: ", name[:-3])
        log_file_obj.write("Metadata for NED file: "+ name[:-3] + "\n")
        print("Number of soundings: ", sounding_local)
        log_file_obj.write("Number of soundings: "+ str(sounding_local) + "\n")
        print("X min: ", min_x, " X max: ", max_x)
        log_file_obj.write("X min: "+ str( min_x) + " X max: " + str( max_x) + "\n")
        print("Y min: ", min_y, "Y max: ", max_y)
        log_file_obj.write("Y min: " + str( min_y) + " Y max: " + str( max_y) + "\n")
        print("Z min: ", min_z, "Z max: ", max_z)
        log_file_obj.write("Z min: " + str(min_z) + " Z max: " + str( max_z) + "\n\n")
        
        # Close file
        log_file_obj.close()
        print("Metadata written to logfile...")
        print()       
    
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
def effstat(out_file):
    "calculate and print eff stats"
    print("Efficiency statistics is", efficiency_statistics)
    end = timer()
    used_time = end - start
    
    #Show efficiency statistcs
    sounding_per_second = round(soundings_number/used_time)
    print("Total number of depth soundings:", soundings_number)
    print("Total time: {0:.2f}".format(used_time), "seconds")
    print("Soundings per second:", sounding_per_second)
    
    #Show efficiency statistics in log file
    if metadata_logging:
        log_file_obj = open(out_file+log_file, "a")
        log_file_obj.write("\nEfficiency of conversion:\n")
        log_file_obj.write("Total number of soundings: " + str(soundings_number) + "\n")
        log_file_obj.write("Total time: {0:.2f}".format(used_time) + "seconds\n")
        log_file_obj.write("Soundings per second: " + str( sounding_per_second) + "\n")
        log_file_obj.close()
        print("Efficiency data written to logfile...")
        print()         

# set input file name and directory
#in_path = "C:\\Users\\ruurd\\Documents\\IB1\\ITGS\\Python_Project_data\\data\\in\\"
in_path = "C:\\Users\\ruurd\\Documents\\IB1\\ITGS\\Python_Project_data\\data\\in\\"


# set output file name and directory
#out_path = "C:\\Users\\ruurd\\Documents\\IB1\\ITGS\\Python_Project_data\\data\\out\\"
out_path = "C:\\Users\\ruurd\\Documents\\IB1\\ITGS\\Python_Project_data\\data\\out\\"

# set input file delimiter and columns
# values used here represent the .NED format used internally by the NHS 
in_delimiter = " "
out_delimiter = " "
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

#Log time and date in log file    
if metadata_logging:
    log_file = datetime.now().strftime("%Y%m%d_%H%M%S.log")
    
#Search directory for NED files
    nedfiles = find_ned( in_path )
        
#For each NED file in directory, convert to xyz file.
for nedfile in nedfiles:
        convertNed2Xyz (nedfile, in_path, out_path)
        print (nedfile + " converted to xyz")
        print("Error during conversion of:", nedfile)
        if metadata_logging:
            log_file_obj = open(out_path+log_file, "a")
            log_file_obj.write("Error during conversion of " + nedfile + "\n\n")
            log_file_obj.close()      

#Show efficiency statistics:
if efficiency_statistics:
    effstat(out_path)
    
#=============
#End Program
#=============