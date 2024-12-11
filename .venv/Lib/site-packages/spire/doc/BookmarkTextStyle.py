from enum import Enum
from plum import dispatch
from typing import TypeVar, Union, Generic, List, Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class BookmarkTextStyle(Enum):
    """
    Enum class for choosing outline text style.

    Attributes:
        Regular: Regular text style.
        Italic: Italic text style.
        Bold: Bold text style.
    """
    Regular = 0
    Italic = 1
    Bold = 2
