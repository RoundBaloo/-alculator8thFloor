from enum import Enum
from plum import dispatch
from typing import TypeVar, Union, Generic, List, Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class TextWrappingStyle(Enum):
    """
    Enum class to specify text wrapping style for an object.

    """
    Inline = 0
    TopAndBottom = 1
    Square = 2
    InFrontOfText = 3
    Tight = 4
    Through = 5
    Behind = 6
    none = -1

