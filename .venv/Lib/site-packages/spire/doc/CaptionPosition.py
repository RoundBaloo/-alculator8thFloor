from enum import Enum
from plum import dispatch
from typing import TypeVar, Union, Generic, List, Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class CaptionPosition(Enum):
    """
    Enum class representing the position of Image Caption Numbering.
    
    """
    AboveImage = 0
    AfterImage = 1
    AboveItem = 0
    BelowItem = 1
