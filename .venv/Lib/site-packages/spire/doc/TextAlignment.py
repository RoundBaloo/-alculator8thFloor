from enum import Enum
from plum import dispatch
from typing import TypeVar, Union, Generic, List, Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class TextAlignment(Enum):
    """
    Enum class for specifying vertical font alignment for East Asian languages.

    """
    Top = 0
    Center = 1
    Baseline = 2
    Bottom = 3
    Auto = 4
