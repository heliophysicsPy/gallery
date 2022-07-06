# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.14.0
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# # Using PlasmaPy Particles

# [plasmapy.particles]: ../../particles/index.rst
#
# The [plasmapy.particles] subpackage contains functions to access basic particle data and classes to represent particles.

from plasmapy.particles import *

# ## Contents
#
# 1. [Particle properties](#Particle-properties)
# 2. [Particle objects](#Particle-objects)
# 3. [Custom particles](#Custom-particles)
# 4. [Molecules](#Molecules)
# 5. [Particle lists](#Particle-lists)
# 6. [Dimensionless particles](#Dimensionless-particles)
# 7. [Nuclear reactions](#Nuclear-reactions)

# ## Particle properties

# [representation of a particle]: https://docs.plasmapy.org/en/stable/api/plasmapy.particles.ParticleLike.html#particlelike
#
# There are several functions that provide information about different particles that might be present in a plasma. The input of these functions is a [representation of a particle], such as a string for the atomic symbol or the element name.

atomic_number("Fe")

# [atomic number]: https://en.wikipedia.org/wiki/Atomic_number
#
# We can provide a number that represents the [atomic number].

element_name(26)

# We can also provide standard symbols or the names of particles.

is_stable("e-")

charge_number("proton")

# [alpha particle]: https://en.wikipedia.org/wiki/Alpha_particle
#
# The symbols for many particles can even be used directly, such as for an [alpha particle]. To create an "α" in a Jupyter notebook, type `\alpha` and press tab.

particle_mass("α")

# [mass number]: https://en.wikipedia.org/wiki/Mass_number
# [half_life]: ../../api/plasmapy.particles.atomic.half_life.rst
# [Quantity]: https://docs.astropy.org/en/stable/units/quantity.html#quantity
# [astropy.units]: https://docs.astropy.org/en/stable/units/index.html
#
# We can represent isotopes with the atomic symbol followed by a hyphen and the [mass number]. In this example, [half_life] returns the time in seconds as a [Quantity] from [astropy.units].

half_life("C-14")

# We typically represent an ion in a string by putting together the atomic symbol or isotope symbol, a space, the charge number, and the sign of the charge.

charge_number("Fe-56 13+")

# [plasmapy.particles]: ../../particles/index.rst
# [Particle]: ../../api/plasmapy.particles.particle_class.Particle.rst
# [particle-like]: https://docs.plasmapy.org/en/latest/glossary.html#term-particle-like
#
# Functions in [plasmapy.particles] are quite flexible in terms of string inputs representing particles. An input is [particle-like] if it can be transformed into a [Particle].  

particle_mass("iron-56 +13")

particle_mass("iron-56+++++++++++++")

# Most of these functions take additional arguments, with `Z` representing the charge number of an ion and `mass_numb` representing the mass number of an isotope. These arguments are often [keyword-only](https://docs.plasmapy.org/en/latest/glossary.html#term-keyword-only) to avoid ambiguity.

particle_mass("Fe", Z=13, mass_numb=56)

# ## Particle objects

# [Particle]: ../../api/plasmapy.particles.particle_class.Particle.rst
#
# Up until now, we have been using functions that accept representations of particles and then return particle properties. With the [Particle] class, we can create objects that represent physical particles.

proton = Particle("p+")
electron = Particle("electron")
iron56_nuclide = Particle("Fe", Z=26, mass_numb=56)

# [Particle]: ../../api/plasmapy.particles.particle_class.Particle.rst
#
# Particle properties can be accessed via attributes of the [Particle] class.

proton.mass

electron.charge

electron.charge_number

iron56_nuclide.binding_energy

# ### Antiparticles
#
# [Particle]: ../../api/plasmapy.particles.particle_class.Particle.rst
#
# We can get antiparticles of fundamental particles by using the `antiparticle` attribute of a [Particle].

electron.antiparticle

# [Particle]: ../../api/plasmapy.particles.particle_class.Particle.rst
#
# We can also use the tilde operator on a [Particle] to get its antiparticle.

~proton

# ### Ionization and recombination
#
# [Particle]: ../../api/plasmapy.particles.particle_class.Particle.rst
#
# The `recombine` and `ionize` methods of a [Particle] representing an ion or neutral atom will return a different [Particle] with fewer or more electrons.

deuterium = Particle("D 0+")
deuterium.ionize()

# When provided with a number, these methods tell how many bound electrons to add or remove.

alpha = Particle("alpha")
alpha.recombine(2)

# [Particle]: ../../api/plasmapy.particles.particle_class.Particle.rst
#
# If the ``inplace`` keyword is set to `True`, then the [Particle] will be replaced with the new particle.

argon = Particle("Ar 0+")
argon.ionize(inplace=True)
print(argon)

# ## Custom particles

# [CustomParticle]: ../../api/plasmapy.particles.particle_class.CustomParticle.rst
#
# Sometimes we want to use a particle with custom properties.  For example, we might want to represent an average ion in a multi-species plasma.  For that we can use [CustomParticle].

# +
from astropy import constants as const
from astropy import units as u

custom_particle = CustomParticle(9.27e-26 * u.kg, 13.6 * const.e.si, symbol="Fe 13.6+")
# -

# [CustomParticle]: ../../api/plasmapy.particles.particle_class.CustomParticle.rst
# [Particle]: ../../api/plasmapy.particles.particle_class.Particle.rst
#
# Many of the attributes of [CustomParticle] are the same as in [Particle].

custom_particle.mass

custom_particle.charge

custom_particle.symbol

# [nan]: https://numpy.org/doc/stable/reference/constants.html#numpy.nan
#
# If we do not include one of the physical quantities, it gets set to [nan] (not a number) in the appropriate units.

CustomParticle(9.27e-26 * u.kg).charge

# [CustomParticle]: ../../api/plasmapy.particles.particle_class.CustomParticle.rst
# [plasmapy.formulary]: ../../formulary/index.rst
# [plasmapy.particles]: ../../particles/index.rst
#
# [CustomParticle] objects are not yet able to be used by many of the functions in [plasmapy.formulary], but are expected to become compatible with them in a future release of PlasmaPy. Similarly, [CustomParticle] objects are not able to be used by the functions in [plasmapy.particles] that require that the particle be real.

# ## Particle lists

# [ParticleList]: ../../api/plasmapy.particles.particle_collections.ParticleList.rst
# [Particle]: ../../api/plasmapy.particles.particle_class.Particle.rst
# [CustomParticle]: ../../api/plasmapy.particles.particle_class.CustomParticle.rst
#
# The [ParticleList] class is a container for [Particle] and [CustomParticle] objects.

iron_ions = ParticleList(["Fe 12+", "Fe 13+", "Fe 14+"])

# [ParticleList]: ../../api/plasmapy.particles.particle_collections.ParticleList.rst
#
# By using a [ParticleList], we can access the properties of multiple particles at once.

iron_ions.mass

iron_ions.charge

iron_ions.symbols

# [ParticleList]: ../../api/plasmapy.particles.particle_collections.ParticleList.rst
# [Particle]: ../../api/plasmapy.particles.particle_class.Particle.rst
# [CustomParticle]: ../../api/plasmapy.particles.particle_class.CustomParticle.rst
#
# We can also create a [ParticleList] by adding [Particle] and/or [CustomParticle] objects together.

proton + electron + custom_particle

# ## Molecules

# [CustomParticle]: ../../api/plasmapy.particles.particle_class.CustomParticle.rst
# [molecule]: ../../api/plasmapy.particles.particle_class.molecule.rst
#
# We can use [molecule] to create a [CustomParticle] based on a chemical formula. The first argument to [molecule] is a string that represents a chemical formula, except that the subscript numbers are not given as subscripts. For example, water is ``"H2O"``.  

water = molecule("H2O")
water.symbol

# The properties of the molecule are found automatically.

water.mass

acetic_acid_anion = molecule("CH3COOH 1-")
acetic_acid_anion.charge

# ## Particle categorization

# [categories]: ../../api/plasmapy.particles.particle_class.Particle.rst#plasmapy.particles.particle_class.Particle.categories
# [Particle]: ../../api/plasmapy.particles.particle_class.Particle.rst
#
# The [categories] attribute of a [Particle] provides a set of the categories that the [Particle] belongs to.

muon = Particle("muon")
muon.categories

# [is_category()]: ../../api/plasmapy.particles.particle_class.Particle.rst#plasmapy.particles.particle_class.Particle.is_category
# [Particle]: ../../api/plasmapy.particles.particle_class.Particle.rst
#
# The [is_category()] method lets us determine if a [Particle] belongs to one or more categories.

muon.is_category("lepton")

# [Particle]: ../../api/plasmapy.particles.particle_class.Particle.rst
#
# If we need to be more specific, we can use the `require` keyword for categories that a [Particle] must belong to, the `exclude` keyword for categories that the [Particle] cannot belong to, and the `any_of` keyword for categories of which a [Particle] needs to belong to at least one.

electron.is_category(require="lepton", exclude="baryon", any_of={"boson", "fermion"})

# [is_category()]: ../../api/plasmapy.particles.particle_class.Particle.rst#plasmapy.particles.particle_class.Particle.is_category
# [Particle]: ../../api/plasmapy.particles.particle_class.Particle.rst
#
# The `valid_categories` attribute of [is_category()] for any [Particle] gives a set containing all valid categories.

print(electron.is_category.valid_categories)

# [is_category()]: ../../api/plasmapy.particles.particle_class.Particle.rst#plasmapy.particles.particle_class.Particle.is_category
# [ParticleList]: ../../api/plasmapy.particles.particle_collections.ParticleList.rst
#
# The [is_category()] method of [ParticleList] returns a `list` of boolean values which correspond to whether or not each particle in the list meets the categorization criteria.

particles = ParticleList(["e-", "p+", "n"])
particles.is_category(require="lepton")

# ## Dimensionless particles

# [DimensionlessParticle]: ../../api/plasmapy.particles.particle_class.DimensionlessParticle.rst
#
# When we need a dimensionless representation of a particle, we can use the [DimensionlessParticle] class.

dimensionless_particle = DimensionlessParticle(mass=0.000545, charge=-1)

# The properties of dimensionless particles may be accessed by its attributes.

dimensionless_particle.mass

dimensionless_particle.charge

# [DimensionlessParticle]: ../../api/plasmapy.particles.particle_class.DimensionlessParticle.rst
# [ParticleList]: ../../api/plasmapy.particles.particle_collections.ParticleList.rst
#
# Because a [DimensionlessParticle] does not uniquely describe a physical particle, it cannot be contained in a [ParticleList].  

# ## Nuclear reactions

# [plasmapy.particles]: ../../particles/index.rst
#
# We can use [plasmapy.particles] to calculate the energy of a nuclear reaction using the `>` operator.  

deuteron = Particle("D+")
triton = Particle("T+")
alpha = Particle("α")
neutron = Particle("n")

energy = deuteron + triton > alpha + neutron

energy.to("MeV")

# If the nuclear reaction is invalid, then an exception is raised that states the reason why.

# + nbsphinx="hidden"
# %xmode minimal

# + tags=["raises-exception"]
deuteron + triton > alpha + 3 * neutron
