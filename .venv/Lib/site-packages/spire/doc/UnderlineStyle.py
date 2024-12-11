from enum import Enum
from plum import dispatch
from typing import TypeVar, Union, Generic, List, Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class UnderlineStyle(Enum):
    """
    Enum class that specifies the style of the underline.
    
    """
    none = 0
    Single = 1
    Words = 2
    Double = 3
    Dotted = 4
    DotDot = 4
    Thick = 6
    Dash = 7
    DotDash = 9
    DotDotDash = 10
    Wavy = 11
    DottedHeavy = 20
    DashHeavy = 23
    DotDashHeavy = 25
    DotDotDashHeavy = 26
    WavyHeavy = 27
    DashLong = 39
    WavyDouble = 43
    DashLongHeavy = 55
