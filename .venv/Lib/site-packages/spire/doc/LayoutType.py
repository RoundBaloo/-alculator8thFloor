from enum import Enum
from plum import dispatch
from typing import TypeVar, Union, Generic, List, Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class LayoutType(Enum):
    """
    Enum class that defines the possible types of layout algorithms
    that can be used to layout a table within a WordprocessingML document.
    """

    Fixed = 0
    AutoFit = 1
