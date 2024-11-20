from enum import Enum
from plum import dispatch
from typing import TypeVar, Union, Generic, List, Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class TextDirection(Enum):
    """
    Enum class that defines the direction of text.

    """
    TopToBottom = 0
    RightToLeft = 3
    LeftToRightRotated = 5
    LeftToRight = 2
    TopToBottomRotated = 4
    RightToLeftRotated = 1
