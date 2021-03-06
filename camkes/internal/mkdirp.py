#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# Copyright 2015, NICTA
#
# This software may be distributed and modified according to the terms of
# the BSD 2-Clause license. Note that NO WARRANTY is provided.
# See "LICENSE_BSD2.txt" for details.
#
# @TAG(NICTA_BSD)
#

'''
mkdir -p

For some reason, there does not seem to be a simpler way of achieving thread-
safe directory creation in Python.
'''

import errno, os

def mkdirp(path):
    assert not os.path.exists(path) or os.path.isdir(path)
    try:
        os.makedirs(path)
    except OSError as e:
        # Mask any errors that result from the directory existing.
        if e.errno != errno.EEXIST or not os.path.isdir(path):
            raise
