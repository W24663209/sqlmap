#!/usr/bin/env python2

"""
Copyright (c) 2006-2019 sqlmap developers (http://sqlmap.org/)
See the file 'LICENSE' for copying permission
"""

from lib.core.exception import SqlmapUnsupportedFeatureException
from plugins.generic.filesystem import Filesystem as GenericFilesystem

class Filesystem(GenericFilesystem):
    def __init__(self):
        GenericFilesystem.__init__(self)

    def readFile(self, rFile):
        errMsg = "on Sybase it is not possible to read files"
        raise SqlmapUnsupportedFeatureException(errMsg)

    def writeFile(self, wFile, dFile, fileType=None, forceCheck=False):
        errMsg = "on Sybase it is not possible to write files"
        raise SqlmapUnsupportedFeatureException(errMsg)
