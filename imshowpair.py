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
               interpolation=None, grid=False, *args, **kwargs):
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
    interpolation : str
        Interpolation method for `imshow` to use.
    grid : bool
        If True, display grid.
    """

    def turn_off_ticks(ax):
        for tic in ax.xaxis.get_major_ticks():
            tic.tick1On = tic.tick2On = False
        for tic in ax.yaxis.get_major_ticks():
            tic.tick1On = tic.tick2On = False

    a = np.asarray(a)
    b = np.asarray(b)
    a_shape = a.shape
    b_shape = b.shape

    ax_list = []
    if method == None:
        ax0 = ax = plt.subplot(121)
        plt.imshow(a, origin='upper', cmap=cmap, interpolation=interpolation)
        plt.grid(grid)
        turn_off_ticks(ax)
        ax_list.append(ax)
        ax = plt.subplot(122, sharex=ax0, sharey=ax0)
        plt.imshow(b, origin='upper', cmap=cmap, interpolation=interpolation)
        plt.grid(grid)
        turn_off_ticks(ax)
        if a_shape == b_shape:
            ax.set_yticklabels([])
        ax_list.append(ax)
        plt.subplots_adjust()
    elif callable(method):
        c = method(a, b, *args, **kwargs)
        c_shape = c.shape
        if show_all:
            ax0 = ax = plt.subplot(131)
            plt.imshow(a, origin='upper', cmap=cmap, interpolation=interpolation)
            plt.grid(grid)
            turn_off_ticks(ax)
            ax_list.append(ax)
            ax = plt.subplot(132, sharex=ax0, sharey=ax0)
            plt.imshow(b, origin='upper', cmap=cmap, interpolation=interpolation)
            plt.grid(grid)
            turn_off_ticks(ax)
            if a_shape == b_shape:
                ax.set_yticklabels([])
            ax_list.append(ax)
            ax = plt.subplot(133, sharex=ax0, sharey=ax0)
            plt.imshow(c, origin='upper', cmap=cmap, interpolation=interpolation)
            plt.grid(grid)
            turn_off_ticks(ax)
            plt.subplots_adjust()
            if c_shape == b_shape:
                ax.set_yticklabels([])
            ax_list.append(ax)
        else:
            ax = plt.subplot(111)
            plt.imshow(c, origin='upper', cmap=cmap, interpolation=interpolation)
            plt.grid(grid)           
            turn_off_ticks(ax)
            if c_shape == b_shape:
                ax.set_yticklabels([])
            ax_list.append(ax)
    else:
        NotImplementedError
    if not axes_visible:
        for ax in ax_list:
            ax.set_xticklabels([])
            ax.set_yticklabels([])
