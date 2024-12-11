from enum import Enum
from plum import dispatch
from typing import TypeVar, Union, Generic, List, Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class RelativeVerticalPosition(Enum):
    """
    Enum class representing the relative vertical positions.
    """
    Margin = 0
    Page = 1
    Paragraph = 2
    Line = 3
    TopMargin = 4
    BottomMargin = 5
    InsideMargin = 6
    OutsideMargin = 7
    TableDefault = 0
    TextFrameDefault = 2
