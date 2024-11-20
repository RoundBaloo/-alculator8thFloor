from enum import Enum
from plum import dispatch
from typing import TypeVar, Union, Generic, List, Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class BorderStyle(Enum):
    """
    Specifies style of the border line.
    """
    none = 0
    Single = 1
    Thick = 2
    Double = 3
    Hairline = 5
    Dot = 6
    DashLargeGap = 7
    DotDash = 8
    DotDotDash = 9
    Triple = 10
    ThinThickSmallGap = 11
    ThickThinSmallGap = 12
    ThinThinSmallGap = 12
    ThinThickThinSmallGap = 13
    ThinThickMediumGap = 14
    ThickThinMediumGap = 15
    ThinThickThinMediumGap = 16
    ThickThickThinMediumGap = 16
    ThinThickLargeGap = 17
    ThickThinLargeGap = 18
    ThinThickThinLargeGap = 19
    Wave = 20
    DoubleWave = 21
    DashSmallGap = 22
    DashDotStroker = 23
    Emboss3D = 24
    Engrave3D = 25
    Outset = 26
    Inset = 27
    TwistedLines1 = 214
    Cleared = 255
