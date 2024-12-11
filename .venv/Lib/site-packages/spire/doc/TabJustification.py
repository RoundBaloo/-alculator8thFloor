from enum import Enum
from plum import dispatch
from typing import TypeVar, Union, Generic, List, Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class TabJustification(Enum):
    """
    Enum class that specifies the tab justification.

    """
    Left = 0
    Centered = 1
    Right = 2
    Decimal = 3
    Bar = 4
    List = 6
    Clear = 7
