# coding: utf-8
"""
====================================
pyspedas Demo
====================================

Written by Nick Hatzigeorgiu. 

The purpose of this demo is to demonstrate some of the capabilities of the pyspedas package.
"""

####################################################################################
# The pyspedas package contains functions for downloading data from NASA missions 
# and tools for data analysis and data plotting. It works together with 
# the pytplot and the cdflib packages.
#
# Pyspedas is a python implementation of the SPEDAS software which is written 
# in the IDL programming language. For more information on SPEDAS, 
# see: http://spedas.org/wiki/
from pyspedas import load_data, gmag_list, subtract_average, version
from pytplot import del_data, get_data, store_data, ylim, tplot, options, tplot_options, tplot_names

####################################################################################
# Load and plot THEMIS data
####################################################################################

####################################################################################
# Pyspedas uses a preferences file (spd_prefs_txt.py) which contains the variables
# that determine the local path for saving cdf files. The user can change this
# path, if he wants to. We can find the location of the pyspedas preferences file
# and the version of the installed pyspedas package, using the function version(). 
version()

####################################################################################
# Delete any existing pytplot variables
del_data()

####################################################################################
# Define a time range. Here, we pick a time range that spans one and a half day.
time_range = ['2015-12-31 00:00:00', '2016-01-01 12:00:00']

####################################################################################
# Download THEMIS state data and store it into the pytplot object.
# This following function downloads all the necessary files, loads data, 
# and time-clips data to the specified time range. 
load_data('themis', time_range, ['tha'], 'state', 'l1')

####################################################################################
# Get data from pytplot object into python variables. 
# This is useful when we want to work on the data using standard python libraries.
alldata = get_data("tha_vel")
time = alldata[0]
data = alldata[1]

####################################################################################
# After working with the data, we can store a new pytplot variable. 
# We can also store our own data in the pytplot object.
store_data("tha_new_vel", data={'x': time, 'y': data})

####################################################################################
# Preparing for the plots, we define the y-axis limits for the two panels.
ylim('tha_pos', -23000.0, 81000.0)
ylim('tha_new_vel', -8.0, 12.0)

####################################################################################
# We give a title to the plot and labels for the y-axis panels.
tplot_options('title', 'THEMIS tha position and velocity, 2015-12-31')
options('tha_pos','ytitle','Position')
options('tha_new_vel','ytitle','Velocity')

####################################################################################
# We plot the position and the velocity using the pyqtgraph library (the default). 
tplot(["tha_pos", "tha_new_vel"])

####################################################################################
# A new window will open, containing the following plot:
#
# .. image:: http://themis.ssl.berkeley.edu/images/pyspedas_demo1.png
#    :alt: Themis tha position and velocity
#


####################################################################################
# Load and plot GMAG data
####################################################################################

####################################################################################
# Delete any existing pytplot variables, and define a time range.  
del_data()
time_range = ['2015-12-31 00:00:00', '2015-12-31 23:59:59']

####################################################################################
# GMAG stations are organized in groups. For a list of all available GMAG groups 
# and all GMAG stations, see: http://themis.ssl.berkeley.edu/gmag/gmag_list.php
#
# Get a list of the GMAG stations that belong to the EPO group.
# Internally, this function uses a web service to get a list of the names.
sites = gmag_list(group='epo')

####################################################################################
# Download cdf files for all EPO GMAG stations and load data into pytplot variables.
#
# Some GMAG stations may not have any data files for the specified time interval. 
# In that case, we will get an error message that the remote file does not exist
# for that GMAG station.  
load_data('gmag', time_range, sites, '', '')

####################################################################################
# Print the names of the loaded GMAG sites. 
sites_loaded = tplot_names()

####################################################################################
# Subtract the average values for these sites.
subtract_average(sites_loaded, '')

####################################################################################
# Download AE index data.
load_data('gmag', time_range, ['idx'], '', '')

####################################################################################
# Get a list of all the loaded GMAG sites plus the AE index data. 
sites_loaded = tplot_names()

####################################################################################
# Plot GMAG and AE index data, using the bokeh library.
tplot_options('title', 'EPO GMAG 2015-12-31')
tplot(sites_loaded, bokeh=True)

####################################################################################
# The output will appear in the default web browser:
#
# .. image:: http://themis.ssl.berkeley.edu/images/pyspedas_demo2.png
#    :alt: EPO GMAG plot
#
