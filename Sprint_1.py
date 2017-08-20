# -*- coding: utf-8 -*-
"""
Created on Tue Jun 27 15:07:58 2017

@author: Ruurd
"""

# set input file name and directory
in_file_ext = ".NED"
in_filename = "D3470_grid05_geo"   # "D3470_grid05_geo" for testing, "D4073_grid05_geo" for large file testing 
in_path = "C:\\Users\\ruurd\\Documents\\IB1\\ITGS\\Python_Project_data\\data\\in\\"
in_file = in_path + in_filename + in_file_ext

# set output file name and directory
out_file_ext = ".xyz"
out_filename = in_filename
out_path = "C:\\Users\\ruurd\\Documents\\IB1\\ITGS\\Python_Project_data\\data\\out\\"
out_file = out_path + out_filename + out_file_ext
out_delimiter =";"

# set input file delimiter and columns
# values used here represent the .NED format used internally by the NHS 
in_delimiter = " "
N=0 # first column is North in digital degrees
E=1 # second column is Easting in digital degrees
D=2 # third and last column is depth, in meters and centimeters

soundings_number = 0

#open input file
in_file_obj = open(in_file,"r")

#open output file
out_file_obj = open(out_file, "w")

print("Converting from NED to xyz...")
print("writing to file:", out_filename + out_file_ext)
print("in location:", out_path)

# read each line
for line in in_file_obj:
    soundings_number = soundings_number +1
    sounding = line.split(in_delimiter)

    # convert string into floats
    x=float(sounding[E])
    y=float(sounding[N])
    z=float(sounding[D])
        
    out_text = sounding[E]+out_delimiter+sounding[N]+out_delimiter+"-"+sounding[D]
    out_file_obj.write(out_text)
    
# close input file 
in_file_obj.close()

# close output file 
out_file_obj.close()