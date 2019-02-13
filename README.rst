.. -*- rst -*-

Compare Two Images with Matplotlib
==================================

Package Description
-------------------
Utility function for comparing two images. Inspired by MATLAB's
`imshowpair <https://www.mathworks.com/help/images/ref/imshowpair.html>`_ 
function.

.. .. image:: https://img.shields.io/pypi/v/imshowpair.svg
..    :target: https://pypi.python.org/pypi/imshowpair
..    :alt: Latest Version

Installation
------------
`imshowpair` requires `matplotlib <https://matplotlib.org>`_. To install, 
download the source and run ::

    python setup.py install

Usage
-----
Sample usage: ::

    import imshowpair
    a = .. # load first image
    b = .. # load second image
    imshowpair.imshowpair(a, b)

Functions to use when comparing images (alpha blending, etc.) are 
implemented in `imshowpair.utils`. These may require additional dependencies 
such as `scikit-image <https://scikit-image.org>`_: ::

    import imshowpair
    import imshowpair.utils as utils
    a = .. # load first image
    b = .. # load second image
    imshowpair.imshowpair(a, b, utils.blend)

Development
-----------
The latest source code can be obtained from
`GitHub <https://github.com/lebedov/imshowpair/>`_.

Authors
-------
See the included `AUTHORS.rst 
<https://github.com/lebedov/imshowpair/blob/master/AUTHORS.rst>`_ file for 
more information.

License
-------
This software is licensed under the `BSD License 
<http://www.opensource.org/licenses/bsd-license>`_.
See the included `LICENSE.rst 
<https://github.com/lebedov/imshowpair/blob/master/LICENSE.rst>`_ file for 
more information.
