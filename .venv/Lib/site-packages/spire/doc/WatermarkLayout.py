from enum import Enum
from plum import dispatch
from typing import TypeVar, Union, Generic, List, Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class WatermarkLayout(Enum):
    """
    Enum class that specifies the layout of a watermark.
    """

    Diagonal = 0
    Horizontal = 1
