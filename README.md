# Heliopython Gallery
A Gallery of Examples and Tutorials for the Python in Heliophysics Community.

The gallery is hosted at the following url [http://heliopython.org/gallery/generated/gallery/index.html](http://heliopython.org/gallery/generated/gallery/index.html).

Contributing
------------
Contributions of new tutorials and examples are encouraged on most any topic
that is relevant to the use of Python in Heliophysics. This includes demonstrating
functionality in existing heliophysics packages or showing off functionality
in general scientific computing packages which may be of use to the community.

To contribute a new tutorial please provide a pull request. All tutorial files
are stored in the `gallery\` directory and must be a python file. The gallery
uses the [sphinx gallery](https://sphinx-gallery.readthedocs.io/en/latest/)
plugin and all output including plots are generated automatically. You can see
an example gallery [here](https://sphinx-gallery.readthedocs.io/en/latest/auto_examples/index.html).
The [SunPy gallery](http://docs.sunpy.org/en/stable/generated/gallery/index.html) is also a good example.
For the required syntax see the
[sphinx gallery syntax](https://sphinx-gallery.readthedocs.io/en/latest/syntax.html)
documentation. Since the syntax is fairly straightforward you may also just
refer to an existing tutorial file.

Building
--------
If you'd like to build the gallery on your local machine you'll need to install
sphinx as well as sphinx-gallery with the following commands

pip install sphinx
pip install sphinx-gallery

To build the gallery run the following command in the root directory.

make html

The generated output can then be found in `_build/html/index.html` and can
be viewed with any web browser.
