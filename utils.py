#!/usr/bin/env python3

"""
Utility functions to use with imshowpair().
"""

import skimage

def blend(a, b, alpha=0.5):
    """
    Alpha blend two images.

    Parameters
    ----------
    a, b : numpy.ndarray
        Images to blend.
    alpha : float
        Blending factor.

    Returns
    -------
    result : numpy.ndarray
        Blended image.
    """

    a = skimage.img_as_float(a)
    b = skimage.img_as_float(b)
    return a*alpha+(1-alpha)*b

