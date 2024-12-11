from enum import Enum
from plum import dispatch
from typing import TypeVar, Union, Generic, List, Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class TextWrappingType(Enum):
    """
    Enum class to specify text wrapping type for textbox.

    """
    Both = 0
    Left = 1
    Right = 2
    Largest = 3

