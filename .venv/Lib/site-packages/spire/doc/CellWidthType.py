from enum import Enum
from plum import dispatch
from typing import TypeVar, Union, Generic, List, Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class CellWidthType(Enum):
    """
    Specifies preferred width type
    """
    Auto = 1
    Percentage = 2
    Point = 3
