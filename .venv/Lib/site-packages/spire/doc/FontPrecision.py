from enum import Enum
from plum import dispatch
from typing import TypeVar, Union, Generic, List, Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class FontPrecision(Enum):
    """
    Enum class representing font precision options.
    """

    OUT_DEFAULT_PRECIS = 0
    OUT_STRING_PRECIS = 1
    OUT_CHARACTER_PRECIS = 2
    OUT_STROKE_PRECIS = 3
    OUT_TT_PRECIS = 4
    OUT_DEVICE_PRECIS = 5
    OUT_RASTER_PRECIS = 6
    OUT_TT_ONLY_PRECIS = 7
    OUT_OUTLINE_PRECIS = 8
    OUT_SCREEN_OUTLINE_PRECIS = 9
    OUT_PS_ONLY_PRECIS = 10
