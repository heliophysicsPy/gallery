# coding: utf-8
"""
==================================
Astropy Coordinates and SunPy Demo
==================================

Written by Steven Christe and presented at the Heliopython meeting on
November 13-15, 2018. The purpose of this demo is to show off the AstroPy coordinates
framework as well as show how SunPy extends it to add solar coordinate systems. 
"""

##############################################################################
# The astropy coordinates package provides classes for representing a variety
# of celestial/spatial coordinates and their velocity components, as well as
# tools for converting between common coordinate systems in a uniform way.
from astropy import units as u
from astropy.coordinates import SkyCoord, AltAz
from astropy.time import Time

##############################################################################
# SkyCoord
# As an example of creating a SkyCoord to represent an ICRS (Right ascension
# [RA], Declination [Dec]) sky position:
c = SkyCoord(ra=10.625*u.degree, dec=41.2*u.degree, frame='icrs')
##############################################################################
# It can also handle arrays (many ways to instantiate a SkyCoord)
c = SkyCoord(ra=[10, 11, 12, 13]*u.degree, dec=[41, -5, 42, 0]*u.degree)

##############################################################################
# SkyCoord can also handle 3D positions, just add a distance
c = SkyCoord(ra=10.68458*u.degree, dec=41.26917*u.degree, distance=770*u.kpc)

##############################################################################
# So now cartesian coordinates are available
print('r = ({0}, {1}, {2})'.format(c.cartesian.x, c.cartesian.y, c.cartesian.z))

##############################################################################
# Positions of objects
# Can also register positions of objects or do object lookups
crab = SkyCoord.from_name("Crab")
print(crab)

##############################################################################
# let's consider now consider a position in the sky from a specific location
# on the Earth.
from astropy.coordinates import EarthLocation

##############################################################################
# Many positions are already availabe such as that of the VLA.
vla_coord = EarthLocation.of_site('vla')
print(vla_coord)

##############################################################################
# Using a position on the Earth we can calculate Alt/Az, since dkist is missing
# from the library, let's add it as a position
dkist = EarthLocation(lat=20.70818*u.deg, lon=-156.2569*u.deg, height=3084*u.m)
utcoffset = -10 * u.hour
midnight = Time('2018-11-14 00:00:00') - utcoffset

##############################################################################
# We can now get the position of the Crab in the sky as observed from DKIST
crab_altaz = crab.transform_to(AltAz(obstime=midnight,location=dkist))
print(crab_altaz)
print("Crab's Altitude = {0.alt:}".format(crab_altaz))

##############################################################################
# Let's now move on to showing how SunPy extends AstroPy coordinates by
# adding solar coordinate systems.
from sunpy.coordinates import frames, get_sunearth_distance

##############################################################################
# SunPy defines HeliographicStonyhurst, HeliographicCarrington, Heliocentric,
# and Helioprojective. Let's define the center of the Sun
sun = SkyCoord(0 * u.arcsec, 0 * u.arcsec, obstime=midnight, frame=frames.Helioprojective)

##############################################################################
# The position in the sky from the DKIST site is
sun_altaz = sun.transform_to(AltAz(obstime=midnight,location=dkist))
print('Altitude is {0} and Azimuth is {1}'.format(sun_altaz.T.alt, sun_altaz.T.az))

##############################################################################
# As expected the Sun is below the horizon! Let's consider noon now.
noon = Time('2018-11-14 12:00:00') - utcoffset
sun_altaz = sun.transform_to(AltAz(obstime=noon,location=dkist))
print('Altitude is {0} and Azimuth is {1}'.format(sun_altaz.T.alt, sun_altaz.T.az))

##############################################################################
# Next let’s check this calculation by converting it back to helioprojective.
# We should get our original input which was the center of the Sun.
# To go from Altitude/Azimuth to Helioprojective, you will need the distance
# to the Sun. solar distance. Define distance with SunPy’s almanac.
distance = get_sunearth_distance(noon)
b = SkyCoord(az=sun_altaz.T.az, alt=sun_altaz.T.alt, distance=distance, frame=AltAz(obstime=noon,location=dkist))
sun_helioproj = b.transform_to(frames.Helioprojective)
print('The helioprojective point is {0}, {1}'.format(sun_helioproj.T.Tx, sun_helioproj.T.Ty))

##############################################################################
# Let's now show off how we can convert between Solar coordinates Coordinates.
# Transform to HeliographicStonyhurst
sun.transform_to(frames.HeliographicStonyhurst)

##############################################################################
# Transform to Heliocentric
sun.transform_to(frames.Heliocentric)

##############################################################################
# Transform to HeliographicCarrington
sun.transform_to(frames.HeliographicCarrington)
