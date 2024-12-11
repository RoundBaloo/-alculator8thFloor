from enum import Enum
from plum import dispatch
from typing import TypeVar, Union, Generic, List, Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class WidthType(Enum):
    """
    The TableWidthType enum specifies how the preferred width for a table,
    table indent, table cell, cell margin, or cell spacing is defined.
    """
    none = 0
    Auto = 1
    Percentage = 2
    Twip = 3

