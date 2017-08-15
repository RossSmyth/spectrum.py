# -*- coding: utf-8 -*-

"""
Spectrum API Wrapper
~~~~~~~~~~~~~~~~~~~
A wrapper for the Spectrum API.
:copyright: (c) 2017 treefroog
:license: MIT, see LICENSE for more details.
"""

__title__ = 'spectrum'
__author__ = 'treefroog'
__license__ = 'MIT'
__copyright__ = 'Copyright 2017 treefroog'
__version__ = '0.01'

from .object import Object
from .community import Community
from .message import Message
from .lobby import Lobby
from collections import namedtuple

VersionInfo = namedtuple('VersionInfo', 'major minor micro releaselevel serial')

version_info = VersionInfo(major=0, minor=0, micro=1, releaselevel='alpha', serial=0)
