from enum import Enum
from plum import dispatch
from typing import TypeVar, Union, Generic, List, Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class CheckBoxSizeType(Enum):
    """
    Enum class that defines the size types for a checkbox.
    """

    Auto = 0
    Exactly = 1
