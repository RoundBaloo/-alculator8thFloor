from enum import Enum
from plum import dispatch
from typing import TypeVar, Union, Generic, List, Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class FontPitchAndFamily(Enum):
    """
    Enum class representing font pitch and family options.
    """

    DEFAULT_PITCH = 0
    FIXED_PITCH = 1
    VARIABLE_PITCH = 2
    FF_DONTCARE = 0
    FF_ROMAN = 16
    FF_SWISS = 32
    FF_MODERN = 48
    FF_SCRIPT = 64
    FF_DECORATIVE = 80
