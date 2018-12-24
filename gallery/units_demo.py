# coding: utf-8
"""
================================
Quantities, Units, and Constants
================================

The purpose of this demo is to demonstrate the capabilities of astropy
`~astropy.units.Unit`, `~astropy.units.Quantity`, and `~astropy.units.Constant`.
"""

##############################################################################
# The astropy `~astropy.units.Quantity` object
# handles defining, converting between, and performing arithmetic
# with physical quantities, such as meters, seconds, Hz, etc.
from astropy import units as u
import numpy as np

##############################################################################
# You can define a `~astropy.units.Quantity`
# (a number with a unit) in a number of different ways.
42.0 * u.meter
[1., 2., 3.] * u.s
np.arange(10) * u.Hz

##############################################################################
# These objects work as you would expect with most Python operators or numpy
# functions
np.power(2 * u.s, 3)
(2 * u.s) ** 2

##############################################################################
# If needed you can get the value as well as the unit
q = 42.0 * u.meter
print("The value is {0} and the unit is {1}".format(q.value, q.unit))

##############################################################################
# Using the `~astropy.units.Quantity.to` function we can easily converted to
# another unit.
print(q.to('parsec'))

##############################################################################
# and imperial units as also supported
from astropy.units import imperial
print(q.to(imperial.mile))

##############################################################################
# Units that “cancel out” become a special unit called the “dimensionless unit”:
u.m / u.m

##############################################################################
# More complex conversions are also supported using
# `~astropy.units.equivalencies`.
# For example, we can convert the GOES wavelength range to Hz or keV easily using
# the `~astropy.units.equivalencies.spectral`.
print(([0.5, 4.0] * u.angstrom).to('Hz', u.spectral()))

print(([0.5, 4.0] * u.angstrom).to('keV', u.spectral()))

##############################################################################
# Astropy provides a number of reference constants
from astropy import constants as astropy_const

##############################################################################
# SunPy also provides a number of relevant solar reference constants.
from sunpy.sun import constants as sunpy_const

##############################################################################
# `~astropy.units.Constant` are simply quantities but they also provide an uncertainty
# and a reference
M_earth = astropy_const.M_earth
print("The mass of the Earth is {0} +/- {1} {2} [ref {3}].".format(M_earth.value, M_earth.uncertainty, M_earth.unit, M_earth.reference))

##############################################################################
# The light travel time in minutes from the Sun to the Earth can be calculated
print((sunpy_const.au / astropy_const.c).to('min'))

##############################################################################
# Let's define a function to calculate the plasma beta, with quantities we
# don't have to worry about much beyond getting the equation correct
def plasma_beta(n, T, B):
    return (2 * n * astropy_const.k_B * T) / (B ** 2 / (2 * astropy_const.mu0))

##############################################################################
# The plasma beta for the solar corona using appropriate parameters is given
# by the following. The decompose function works to simplify the units.
print(plasma_beta(1e9 * u.cm**-3, 3e6 * u.Kelvin, 10 * u.Gauss).decompose())

##############################################################################
# If the input is given in the wrong units then an error may occur but a better
# way is to inforce the units on input. Let's consider a simpler example here
# to calculate velocity. We use a function annotation to specify the units
# (this is a Python 3.5+ feature, see the `quantity_input <http://docs.astropy.org/en/stable/api/astropy.units.quantity_input.html#astropy.units.quantity_input>`_
# documentation for more details and Python 2 instructions):

@u.quantity_input
def speed(length: u.m, time: u.s):
    return length / time
