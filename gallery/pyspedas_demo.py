# coding: utf-8
"""
====================================
pyspedas Demo
====================================

Written by Nick Hatzigeorgiu. 

The purpose of this demo is to demonstrate some of the capabilities of the pyspedas package.
"""

####################################################################################
# The pySPEDAS package contains functions for downloading data from NASA missions 
# and tools for data analysis and data plotting. It works together with the 
# pytplot and the cdflib packages.
#
# pySPEDAS is a python implementation of the SPEDAS software which is written 
# in the IDL programming language. For more information on SPEDAS, 
# see: http://spedas.org/wiki/
import pyspedas
#import pytplot
from pyspedas import clean_spikes, version
from pytplot import del_data, get_data, store_data, tplot_options, tplot_names, tplot

####################################################################################
# Load and plot THEMIS data
####################################################################################

####################################################################################
# Note: pySPEDAS uses an environment variable SPEDAS_DATA_DIR to determine the 
# local path for saving data files. SPEDAS_DATA_DIR acts as a root data directory 
# for all missions, but mission-specific data directories 
# (e.g., MMS_DATA_DIR for MMS, THM_DATA_DIR for THEMIS) can also be set, 
# and these will override SPEDAS_DATA_DIR.
#
# We can find the version of the installed pyspedas package using `version()`.  
version()

####################################################################################
# Delete any existing pytplot variables.
del_data()

####################################################################################
# Define a time range. Here, we pick a time range that spans one day.
time_range = ['2015-10-16', '2015-10-17']

####################################################################################
# You can load data into tplot variables by calling `pyspedas.mission.instrument()`. 
# E.g., to load and plot our one day of THEMIS FGM data for probe 'd':
#
# (This following function downloads all the necessary files, loads data, 
# and time-clips data to the specified time range.)
thm_fgm = pyspedas.themis.fgm(trange=time_range, probe='d')

####################################################################################
# Mission-specific information and examples can be found in the READMEs of each 
# mission directory in the pySPEDAS GitHub repo. E.g., THEMIS: 
# https://github.com/spedas/pyspedas/tree/master/pyspedas/themis
#
# Get data from pytplot object into python variables. 
# This is useful when we want to work on the data using standard python libraries.
all_data = get_data("thd_fgs_gse")
time = all_data[0]
data = all_data[1]

####################################################################################
# After working with the data, we can store a new pytplot variable. 
# We can store any data in the pytplot object. 
store_data("new_thd_fgs_gse", data={'x': time, 'y': data})

####################################################################################
# We plot the data using the pyqtgraph library (the default). 
# Another option is to plot using the bokeh library.
#tplot(['thd_fgs_gse', 'thd_fgs_gsm'])

####################################################################################
# Load and plot MMS data
####################################################################################

####################################################################################
# Delete any existing pytplot variables, and define a time range.  
del_data()
time_range = ['2015-10-16/13:05:30', '2015-10-16/13:07:30']

####################################################################################
# Load and plot two minutes of MMS burst mode FGM data:
#
# (Note that it prompts you for an SDC username before the download. 
# You can submit a blank username.)
mms_fgm = pyspedas.mms.fgm(trange=['2015-10-16/13:05:30', '2015-10-16/13:07:30'], data_rate='brst')

####################################################################################
# The names of the loaded tplot variables are printed. You can print the names of 
# all currently-loaded tplot variables at any time using `pyspedas.tnames()`:
pyspedas.tnames()

####################################################################################
# pySPEDAS has a number of helpful analysis routines under `pyspedas.analysis`. 
# E.g., if we want to clean spikes from the data:
clean_spikes(['mms1_fgm_b_gse_brst_l2', 'mms1_fgm_b_gsm_brst_l2'])

####################################################################################
# Plot the (despiked) MMS data. 
# Use the bokeh library — the plots will appear in the web browser.
#
# Note how we use pytplot options to set the line colors. See the full list of 
# options at: https://pytplot.readthedocs.io/en/latest/_modules/pytplot/options.html
pytplot.options('mms1_fgm_b_gse_brst_l2-despike', 'color', 'red')
pytplot.options('mms1_fgm_b_gsm_brst_l2-despike', 'color', 'blue')
#tplot(['mms1_fgm_b_gse_brst_l2-despike', 'mms1_fgm_b_gsm_brst_l2-despike'], bokeh=True)

####################################################################################
# Note: The HTML web page for this example may be missing the plots but this is a 
# limitation of the platform for this particular gallery — if you run the 
# python code locally, the plots will appear. 
