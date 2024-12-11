from enum import Enum
from plum import dispatch
from typing import TypeVar, Union, Generic, List, Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class RtfTokenType(Enum):
    """
    Enum class representing the types of RTF tokens.
    """
    GroupStart = 0
    GroupEnd = 1
    ControlWord = 2
    Text = 3
    TableEntry = 4
    Unknown = 5
