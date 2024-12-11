from enum import Enum
from plum import dispatch
from typing import TypeVar, Union, Generic, List, Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class FontTypeHint(Enum):
    """
    Enumeration that defines the font type hint.
    
    """
    Default = 0
    EastAsia = 1
    ComplexScript = 2
