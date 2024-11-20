from enum import Enum
from plum import dispatch
from typing import TypeVar, Union, Generic, List, Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class FieldCharType(Enum):
    """
    Enum class representing the types of field characters.
    """
    Begin = 0
    Seperate = 1
    End = 2
    Unknown = 3
    SimpleField = 4
