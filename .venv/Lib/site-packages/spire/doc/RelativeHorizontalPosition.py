from enum import Enum
from plum import dispatch
from typing import TypeVar, Union, Generic, List, Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class RelativeHorizontalPosition(Enum):
    """
    Enum class representing relative horizontal positions.
    """

    Margin = 0
    Page = 1
    Column = 2
    Character = 3
    LeftMargin = 4
    RightMargin = 5
    InsideMargin = 6
    OutsideMargin = 7
    Default = 2
