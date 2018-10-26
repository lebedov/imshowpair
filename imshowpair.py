#!/usr/bin/env python3

# Copyright (c) 2018, Lev E. Givon
# All rights reserved.
# Distributed under the terms of the BSD license:
# http://www.opensource.org/licenses/bsd-license

import matplotlib.pyplot as plt
import numpy as np

def blend(a, b, cmap=plt.cm.gray, alpha=0.5, interpolation='nearest'):
    raise NotImplementedError

def imshowpair(a, b, method=None, show_all=True, axes_visible=False, cmap=None,
            *args, **kwargs):
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
    axes_visible : bool
        Show axes if True.
    cmap : matplotlib.colors.Colormap
        Color map to use when displaying images.
    """

    def int_axes(ax, shape):
        ax.axes.set_xticks(np.arange(shape[1], dtype=int))
        ax.axes.set_yticks(np.arange(shape[0], dtype=int))

    a = np.asarray(a)
    b = np.asarray(b)
    a_shape = a.shape
    b_shape = b.shape

    ax_list = []
    if method == None:
        ax0 = ax = plt.subplot(121)
        plt.imshow(a, origin='upper', cmap=cmap)
        int_axes(ax, a_shape)
        ax_list.append(ax)
        ax = plt.subplot(122, sharex=ax0, sharey=ax0)
        plt.imshow(b, origin='upper', cmap=cmap)
        int_axes(ax, b_shape)
        if a_shape == b_shape:
            ax.axes.yaxis.set_visible(False)
        ax_list.append(ax)
        plt.subplots_adjust()
    elif callable(method):
        c = method(a, b, *args, **kwargs)
        c_shape = c.shape
        if show_all:
            ax0 = ax = plt.subplot(131)
            plt.imshow(a, origin='upper', cmap=cmap)
            int_axes(ax, a_shape)
            ax_list.append(ax)
            ax = plt.subplot(132, sharex=ax0, sharey=ax0)
            plt.imshow(b, origin='upper', cmap=cmap)
            int_axes(ax, b_shape)
            if a_shape == b_shape:
                ax.axes.yaxis.set_visible(False)
            ax_list.append(ax)
            ax = plt.subplot(133, sharex=ax0, sharey=ax0)
            plt.imshow(c, origin='upper', cmap=cmap)
            int_axes(ax, c_shape)
            plt.subplots_adjust()
            if c_shape == b_shape:
                ax.axes.yaxis.set_visible(False)
            ax_list.append(ax)
        else:
            plt.imshow(c, origin='upper', cmap=cmap)
            int_axes(ax, c_shape)
            if c_shape == b_shape:
                ax.axes.yaxis.set_visible(False)
            ax_list.append(ax)
    else:
        NotImplementedError
    if not axes_visible:
        for ax in ax_list:
            ax.axes.xaxis.set_visible(False)
            ax.axes.yaxis.set_visible(False)

