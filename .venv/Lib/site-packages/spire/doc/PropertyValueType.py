from enum import Enum
from plum import dispatch
from typing import TypeVar, Union, Generic, List, Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class PropertyValueType(Enum):
    """
    Enum class that specifies the possible property value types.
    
    """
    Boolean = 0
    Date = 1
    Float = 2
    Double = 3
    Int = 4
    Int32 = 5
    String = 6
    ByteArray = 7
    StringArray = 8
    ObjectArray = 9
    ClipData = 10
    AsciiString = 11
    Other = 12
