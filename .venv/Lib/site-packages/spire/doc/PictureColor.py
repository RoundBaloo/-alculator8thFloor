from enum import Enum
from plum import dispatch
from typing import TypeVar, Union, Generic, List, Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class PictureColor(Enum):
    """
    Enum class representing different types of picture colors.

    """
    Automatic = 0
    Grayscale = 1
    BlackAndWhite = 2
    Washout = 3
