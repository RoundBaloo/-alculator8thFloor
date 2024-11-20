from enum import Enum
from plum import dispatch
from typing import TypeVar, Union, Generic, List, Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class TextBoxLineStyle(Enum):
    """
    Enum class to specify the line style of a TextBox object.
    
    """
    Simple = 0
    Double = 1
    ThickThin = 2
    ThinThick = 3
    Triple = 4
