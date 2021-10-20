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
from pytplot import del_data, get_data, store_data, ylim, tplot, tplot_options, tplot_names

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
# We can store any data in the pytplot object. 
store_data("tha_new_vel", data={'x': time, 'y': data})

####################################################################################
# Preparing for the plots, we define the y-axis limits.
ylim('tha_pos', -23000.0, 81000.0)
ylim('tha_new_vel', -8.0, 12.0)

####################################################################################
# We plot the position and the velocity using the pyqtgraph library (the default). 
# Another option is to plot using the bokeh library.
tplot(["tha_pos", "tha_new_vel"])


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
# load_data('gmag', time_range, ['idx'], '', '')

# ####################################################################################
# # Get a list of all the loaded GMAG sites plus the AE index data. 
# sites_loaded = tplot_names()

# ####################################################################################
# # Plot GMAG and AE index data.
# # Use the bokeh library - the plots will appear in the web browser.
# tplot_options('title', 'EPO GMAG 2015-12-31')
# tplot(sites_loaded, bokeh=True)

# ####################################################################################
# # Note: The HTML web page for this example may be missing the plots but this is a 
# # limitation of the platform for this particular gallery - 
# # if you run the python code locally, the plots will appear. 
