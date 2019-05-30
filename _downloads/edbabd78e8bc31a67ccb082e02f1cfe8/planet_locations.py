# coding: utf-8
"""
====================================
Planet Positions in the Solar System
====================================

The purpose of this demo is to demonstrate the ability of sunpy
to get the position of planetary bodies im the solar system.
"""

##############################################################################
# First the imports
from astropy.coordinates import SkyCoord
from sunpy.coordinates import get_body_heliographic_stonyhurst
from astropy.time import Time
import matplotlib.pyplot as plt
import numpy as np

##############################################################################
# Lets grab the positions of each of the planets in stonyhurt coordinates.
obstime = Time('2014-05-15T07:54:00.005')
planet_list = ['earth', 'venus', 'mars', 'mercury', 'jupiter', 'neptune', 'uranus']
planet_coord = [get_body_heliographic_stonyhurst(this_planet, time=obstime) for this_planet in planet_list]

##############################################################################
# Now lets make a plot.
fig = plt.figure()
ax1 = plt.subplot(1, 1, 1, projection='polar')
for this_planet, this_coord in zip(planet_list, planet_coord):
    plt.polar(np.deg2rad(this_coord.lon), this_coord.radius, 'o', label=this_planet)
plt.legend()
plt.show()
