from enum import Enum
from plum import dispatch
from typing import TypeVar, Union, Generic, List, Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class ShapeVerticalAlignment(Enum):
    """
    Specifies vertical alignment of a floating shape.
    """
    Inline = -1
    none = 0
    Top = 1
    Center = 2
    Bottom = 3
    Inside = 4
    Outside = 5
    Default = 0
