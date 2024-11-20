from enum import Enum
from plum import dispatch
from typing import TypeVar, Union, Generic, List, Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class LayoutFlow(Enum):
    """
    Enum class representing the layout flow options.

    """
    Horizontal = 0
    Vertical = 3
    TopToBottom = 5
    BottomToTop = 2
    HorizontalIdeographic = 4
    TopToBottomIdeographic = 1
