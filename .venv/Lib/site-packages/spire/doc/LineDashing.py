from enum import Enum
from plum import dispatch
from typing import TypeVar, Union, Generic, List, Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class LineDashing(Enum):
    """
    Enum class representing different line dashing styles.

    """
    Solid = 0
    Dash = 1
    Dot = 2
    DashDot = 3
    DashDotDot = 4
    DotGEL = 5
    DashGEL = 6
    LongDashGEL = 7
    DashDotGEL = 8
    LongDashDotGEL = 9
    LongDashDotDotGEL = 10
    Default = 0
