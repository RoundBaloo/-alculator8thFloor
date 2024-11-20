from enum import Enum
from plum import dispatch
from typing import TypeVar, Union, Generic, List, Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class ShapeLineStyle(Enum):
    """
    Enum class for shape line styles.
    """
    Single = 0
    Double = 1
    ThickThin = 2
    ThinThick = 3
    Triple = 4
    Default = 0

