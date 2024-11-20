from enum import Enum
from plum import dispatch
from typing import TypeVar, Union, Generic, List, Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class Doc_PropertyType(Enum):
    """
    Enumeration of property types.
    """
    Bool = 11
    Int = 22
    Int32 = 3
    Int16 = 2
    UInt32 = 19
    String = 31
    AsciiString = 30
    DateTime = 64
    Blob = 65
    Vector = 4096
    Object = 12
    Double = 5
    Empty = 0
    Null = 1
    ClipboardData = 71
    AsciiStringArray = 4126
    StringArray = 4127
    ObjectArray = 4108
