from enum import Enum
from plum import dispatch
from typing import TypeVar, Union, Generic, List, Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class ShapeHorizontalAlignment(Enum):
    """
    Specifies horizontal alignment of a floating shape.
    """
    none = 0
    Left = 1
    Center = 2
    Right = 3
    Inside = 4
    Outside = 5
    Default = 0
