from enum import Enum
from plum import dispatch
from typing import TypeVar, Union, Generic, List, Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class HeaderType(Enum):
    """
    Enum class representing different types of headers and footers.
    """
    InvalidValue = -1
    EvenHeader = 0
    OddHeader = 1
    EvenFooter = 2
    OddFooter = 3
    FirstPageHeader = 4
    FirstPageFooter = 5

