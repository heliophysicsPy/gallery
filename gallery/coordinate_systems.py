# coding: utf-8
"""
============================================================
Transforming Coordinates Between SpacePy, Astropy, and SunPy
============================================================

Written by Matt Wentzel-Long. The purpose of this example is to demonstrate
how to pass coordinates between SpacePy, Astropy, and SunPy, and how to
compute some simple transformations in each package.
"""

##############################################################################
!pip install spacepy
from spacepy.coordinates import Coords
import spacepy.time as spt

import astropy.units as u
from astropy.coordinates import SkyCoord

from sunpy.coordinates import frames

##############################################################################
# First, create a `SpacePy coordinate <https://spacepy.github.io/autosummary/spacepy.coordinates.Coords.html>`_ in the (Cartesian) Geographic  
# Coordinate System (GEO) and attach an observation time to the coordinate.  
# Units are in Earth radii (Re). 
coord = Coords([[1,2,4],[1,2,2]], 'GEO', 'car')
coord.ticks = spt.Ticktock(['2002-02-02T12:00:00', '2002-02-02T12:00:00'],
                           'ISO')
print(coord)

# In SpacePy, the convert method can be used to easily convert coordinates into
# one of the `10 coordinate systems <https://spacepy.github.io/coordinates.html>`_ supported. 
# For example, convert the coordinates to the (Cartesian) Solar Magnetic system.
sm = coord.convert('SM','car')
print(sm)

##############################################################################
# Send the coordinates to an Astropy SkyCoord instance using the SpacePy
# to_skycoord function. Units are converted to meters.
# Note: this must be in the GEO system.
skycoord = coord.to_skycoord()
print(skycoord)

# See the Astropy documentation for `transforming coordinates <https://docs.astropy.org/en/stable/coordinates/transforming.html#astropy-coordinates-transforming>`_. Here is a simple
# example that transforms the skycoord into the FK5 system. 
sky_fk5 = skycoord.transform_to('fk5')
print(sky_fk5)

##############################################################################
# Use the `SunPy frames <https://docs.sunpy.org/en/stable/code_ref/coordinates/index.html>`_ function to transform this coordinate into a
# Heliogaphic Carrington coordinate.
# Note: helioprojective frames require that an observer be defined.
sky_helio = skycoord.transform_to(frames.HeliographicCarrington(observer="earth"))
print(sky_helio)

# See the `Astropy Coordinates and SunPy Demo <https://heliopython.org/gallery/generated/gallery/coordinates_demo.html#sphx-glr-generated-gallery-coordinates-demo-py>`_ for coordinate 
# transformations in SunPy.

##############################################################################
# Now, convert the coordinate back into its original form to demonstrate
# transformations in the other direction, and the loss of precision. First,
# convert this back to GEO coordinates (ITRS in Astropy).
sun_geo = sky_helio.transform_to('itrs')
print(sun_geo)

# Lastly, use the SpacePy from_skycoord function to transform this back into a
# SpacePy coordinate.
coord = Coords.from_skycoord(sun_geo)
print(coord)

# The observation time is now in Astropy time (APT) (see `here <https://spacepy.github.io/autosummary/spacepy.time.Ticktock.html>`_).
print(coord.ticks)

# You can verify that this is the original observation time by converting it to ISO.
print(coord.ticks.getISO())
