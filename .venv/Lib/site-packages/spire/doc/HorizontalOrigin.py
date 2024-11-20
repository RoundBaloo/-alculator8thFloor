from enum import Enum
from plum import dispatch
from typing import TypeVar, Union, Generic, List, Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class HorizontalOrigin(Enum):
    """
    Enum class for specifying object's horizontal origin.
    
    """
    Column = 2
    Margin = 0
    Page = 1
    Character = 3
    LeftMarginArea = 4
    RightMarginArea = 5
    InnerMarginArea = 6
    OuterMarginArea = 7
    Default = 2
