# -*- coding: utf-8 -*-

"""
Created on Tue Dec 26 06:00:55 2017
Version 9 - Sep 17 2020
Based on Python3

@author: M.Reza Ershadi / University of Tübingen
         mohammadreza.ershadi@uni-tuebingen.de 
         (mreza.ershadi6789@gmail.com)
         
Libraries:
1-sys
2-subprocess
3-os
4-winsound (just for windows)
5-numpy
6-pandas
7-scipy
8-matplotlib
9-tkinter
10-openpyxl
"""

import def_weather_stations as dws # import the functions

print("=============================================================================")
print("          EARTHSHAPE CHILE WEATHER STATIONS DATA MANAGEMENT (V9, Sep 2020)   ")
print("=============================================================================")

while True:   
    what = dws.defwhat()    
    if what == "1":
         dws.deffile_info()                  
    elif what == "2":
        plot_for = input("________________________________________ Plot type"
                         "\n1: NORMAL PLOT"
                         "\n2: PLOTTING FOR PUBLICATION \n"
                         "Enter a number >>> ")
        if plot_for == "1":
            dws.defrun_plot_normal()
        elif plot_for == "2":          
            dws.defrun_plot_TODD()
    elif what == "3":      
         dws.defrun_append()       
    elif what == "4":      
         dws.defsat_fill()
    elif what == "5":
         doutput = dws.defexcel()
    elif what == "H":
        try:        
            dws.def_help()
        except:
            input("OOPS, The 'HELP' file is missing \n"
                  "Press any key...")            
            pass                
    elif what == "Q":
        print("========================= BYE BYE ...")
        break