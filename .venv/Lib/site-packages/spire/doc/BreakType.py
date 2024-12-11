from enum import Enum
from plum import dispatch
from typing import TypeVar, Union, Generic, List, Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class BreakType(Enum):
    """
    Enum class representing different types of breaks in a document.
    
    Attributes:
        PageBreak (int): Represents a page break.
        ColumnBreak (int): Represents a column break.
        LineBreak (int): Represents a line break.
    """
    PageBreak = 0
    ColumnBreak = 1
    LineBreak = 2
