from enum import Enum
from plum import dispatch
from typing import TypeVar, Union, Generic, List, Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class VerticalPosition(Enum):
    """
    Enum class for specifying the absolute vertical position.
    
    Attributes:
        none (int): Represents no vertical position.
        Top (int): Represents the top vertical position.
        Center (int): Represents the center vertical position.
        Bottom (int): Represents the bottom vertical position.
        Inside (int): Represents the inside vertical position.
        Outside (int): Represents the outside vertical position.
        Inline (int): Represents the inline vertical position.
        Default (int): Represents the default vertical position.
    """
    none = 0
    Top = 1
    Center = 2
    Bottom = 3
    Inside = 4
    Outside = 5
    Inline = -1
    Default = 0

