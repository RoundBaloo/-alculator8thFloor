from enum import Enum
from plum import dispatch
from typing import TypeVar, Union, Generic, List, Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class WrapMode(Enum):
    """
    Enum class that specifies the wrap mode.
    
    Attributes:
        Square: Wrap mode for square wrapping.
        ByPoints: Wrap mode for wrapping by points.
        none: Wrap mode for no wrapping.
        TopBottom: Wrap mode for top-bottom wrapping.
        Through: Wrap mode for through wrapping.
        Inline: Wrap mode for inline wrapping.
    """
    Square = 0
    ByPoints = 1
    none = 2
    TopBottom = 3
    Through = 4
    Inline = 5
