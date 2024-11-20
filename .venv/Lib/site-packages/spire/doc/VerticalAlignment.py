from enum import Enum
from plum import dispatch
from typing import TypeVar, Union, Generic, List, Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class VerticalAlignment(Enum):
    """
    Enum class that specifies the type of vertical alignment.

    Attributes:
        Top: Represents the top alignment.
        Middle: Represents the middle alignment.
        Bottom: Represents the bottom alignment.
    """
    Top = 0
    Middle = 1
    Bottom = 2

