"""
=========================================================================
Downloading and Compressing a FITS file using SunPy, aiapy, and Astropy
=========================================================================

Written by Matt Wentzel-Long. The purpose of this demo is to demonstrate:
1) SunPy's ability to retrieve a Level 1 AIA data, 2) convert this to Level
1.5 AIA data using aiapy, 3) deconvolve the FITS file using aiapy, and 4)
demonstrate the compression ability of Astropy when saving the file.
"""

##############################################################################
# First import the packages
import astropy
import astropy.units as u
from astropy.io.fits import CompImageHDU

from sunpy.net import Fido, attrs as a
import sunpy.map

import aiapy.psf as psf_
from aiapy.calibrate import register, update_pointing

import os

##############################################################################
# Use the SunPy tool `Fido <https://docs.sunpy.org/en/v3.0.1/guide/acquiring_data/fido.html>`_ to find and download level 1 AIA data. 
q = Fido.search(a.Time('2011-06-07T06:52:00', '2011-06-07T06:52:10'),
                a.Instrument('AIA'),
                a.Wavelength(wavemin=171*u.angstrom, wavemax=171*u.angstrom))
aia_map = sunpy.map.Map(Fido.fetch(q))

##############################################################################
# Convert to level 1.5 AIA data. See the `registering and aligning level 1 data <https://aiapy.readthedocs.io/en/latest/generated/gallery/prepping_level_1_data.html>`_
# example in aiapy documentation for more details. 
m_updated_pointing = update_pointing(aia_map)
m_registered = register(m_updated_pointing)
m_normalized = sunpy.map.Map(
    m_registered.data/m_registered.exposure_time.to(u.s).value,
    m_registered.meta)

##############################################################################
# Compute the point-spread function (PSF) and use it to deconvolve the image.
# Warning: the PSF computation can take over 16 minutes on a CPU. If you have
# an NVIDIA GPU and CuPy installed, then PSF will automatically use it.
# See the `PSF documentation <https://aiapy.readthedocs.io/en/latest/api/aiapy.psf.psf.html>`_ for details.
psf = psf_.psf(m_normalized.wavelength)
map_deconvolved = psf_.deconvolve(m_normalized, psf=psf)

##############################################################################
# Save the deconvolved image as a FITS file without compression using SunPy.
# Note: this resulted in a 128 MB file while testing.
map_deconvolved.save('aia_map_deconv.fits')
print(os.path.getsize('aia_map_deconv.fits'))

# This time pass SunPy the `CompImagHDU <https://docs.astropy.org/en/stable/io/fits/api/images.html#compimagehdu>`_ compression routine from Astropy.
sunpy.io.fits.write('aia_map_deconv_comp.fits', map_deconvolved.data,
                    map_deconvolved.fits_header, hdu_type=CompImageHDU)
print(os.path.getsize('aia_map_deconv_comp.fits'))
=======
# coding: utf-8
"""
=========================================================================
Downloading and Compressing a FITS file using SunPy, aiapy, and Astropy
=========================================================================

Written by Matt Wentzel-Long. The purpose of this demo is to demonstrate:
1) SunPy's ability to retrieve a Level 1 AIA data, 2) convert this to Level
1.5 AIA data using aiapy, 3) deconvolve the FITS file using aiapy, and 4)
demonstrate the compression ability of Astropy when saving the file.
"""

##############################################################################
# First import the packages
import astropy
import astropy.units as u
from astropy.io.fits import CompImageHDU

from sunpy.net import Fido, attrs as a
import sunpy.map

import aiapy.psf as psf_
from aiapy.calibrate import register, update_pointing

import os

##############################################################################
# Use the SunPy tool `Fido <https://docs.sunpy.org/en/v3.0.1/guide/acquiring_data/fido.html>`_ to find and download level 1 AIA data. 
q = Fido.search(a.Time('2011-06-07T06:52:00', '2011-06-07T06:52:10'),
                a.Instrument('AIA'),
                a.Wavelength(wavemin=171*u.angstrom, wavemax=171*u.angstrom))
aia_map = sunpy.map.Map(Fido.fetch(q))

##############################################################################
# Convert to level 1.5 AIA data. See the `registering and aligning level 1 data <https://aiapy.readthedocs.io/en/latest/generated/gallery/prepping_level_1_data.html>`_
# example in aiapy documentation for more details. 
m_updated_pointing = update_pointing(aia_map)
m_registered = register(m_updated_pointing)
m_normalized = sunpy.map.Map(
    m_registered.data/m_registered.exposure_time.to(u.s).value,
    m_registered.meta)

##############################################################################
# Compute the point-spread function (PSF) and use it to deconvolve the image.
# Warning: the PSF computation can take over 16 minutes on a CPU. If you have
# an NVIDIA GPU and CuPy installed, then PSF will automatically use it.
# See the `PSF documentation <https://aiapy.readthedocs.io/en/latest/api/aiapy.psf.psf.html>`_ for details.
psf = psf_.psf(m_normalized.wavelength)
map_deconvolved = psf_.deconvolve(m_normalized, psf=psf)

##############################################################################
# Save the deconvolved image as a FITS file without compression using SunPy.
# Note: this resulted in a 128 MB file while testing.
map_deconvolved.save('aia_map_deconv.fits')
print(os.path.getsize('aia_map_deconv.fits'))

# This time pass SunPy the `CompImagHDU <https://docs.astropy.org/en/stable/io/fits/api/images.html#compimagehdu>`_ compression routine from Astropy.
sunpy.io.fits.write('aia_map_deconv_comp.fits', map_deconvolved.data,
                    map_deconvolved.fits_header, hdu_type=CompImageHDU)
print(os.path.getsize('aia_map_deconv_comp.fits'))
