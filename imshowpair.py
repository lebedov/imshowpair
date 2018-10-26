#!/usr/bin/env python3

# Copyright (c) 2018, Lev E. Givon
# All rights reserved.
# Distributed under the terms of the BSD license:
# http://www.opensource.org/licenses/bsd-license

import matplotlib.pyplot as plt
import numpy as np

def blend(a, b, cmap=plt.cm.gray, alpha=0.5, interpolation='nearest'):
    raise NotImplementedError

def imshowpair(a, b, method=None, show_all=True, *args, **kwargs):
    """
    Compare images.

    Parameters
    ----------
    a, b : numpy.ndarray
        Images to compare.
    method : callable
        Callable to apply to images. Must support at least two arguments;
        additional specified arguments are passed to `method`.
        If None, both images are displayed side by side.
    show_all : bool
        If True and `method` is defined, display original images
        alongside `method(a, b)`.
    """

    def int_axes(ax, shape):
        ax.axes.set_xticks(np.arange(shape[1], dtype=int))
        ax.axes.set_yticks(np.arange(shape[0], dtype=int))

    a = np.asarray(a)
    b = np.asarray(b)
    a_shape = a.shape
    b_shape = b.shape

    if method == None:
        ax = plt.subplot(121)
        plt.imshow(a, origin='upper')
        int_axes(ax, a_shape)
        ax = plt.subplot(122)
        plt.imshow(b, origin='upper')
        int_axes(ax, b_shape)
        if a_shape == b_shape:
            ax.axes.yaxis.set_visible(False)
        plt.subplots_adjust()
    elif callable(method):
        c = method(a, b, *args, **kwargs)
        c_shape = c.shape
        if show_all:
            ax = plt.subplot(131)
            plt.imshow(a, origin='upper')
            int_axes(ax, a_shape)
            ax = plt.subplot(132)
            plt.imshow(b, origin='upper')
            int_axes(ax, b_shape)
            if a_shape == b_shape:
                ax.axes.yaxis.set_visible(False)
            ax = plt.subplot(133)
            plt.imshow(c, origin='upper')
            int_axes(ax, c_shape)
            plt.subplots_adjust()
            if c_shape == b_shape:
                ax.axes.yaxis.set_visible(False)
        else:
            plt.imshow(c, origin='upper')
            int_axes(ax, c_shape)
            if c_shape == b_shape:
                ax.axes.yaxis.set_visible(False)
    else:
        NotImplementedError
