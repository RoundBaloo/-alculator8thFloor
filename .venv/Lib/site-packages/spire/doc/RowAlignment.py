from enum import Enum
from plum import dispatch
from typing import TypeVar, Union, Generic, List, Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class RowAlignment(Enum):
    """
    Enum class for specifying the type of horizontal alignment.
    """

    Left = 0
    Center = 1
    Right = 2
