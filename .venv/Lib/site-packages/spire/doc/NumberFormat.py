from enum import Enum
from plum import dispatch
from typing import TypeVar, Union, Generic, List, Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class NumberFormat(Enum):
    """
    Enum class that defines different number formats.
    """
    none = 0
    WholeNumber = 1
    FloatingPoint = 2
    WholeNumberPercent = 3
    FloatingPointPercent = 4
    WholeNumberWithSpace = 5
    FloatingPointWithSpace = 6
    CurrencyFormat = 7
