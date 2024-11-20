from enum import Enum
from plum import dispatch
from typing import TypeVar, Union, Generic, List, Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class WatermarkType(Enum):
    """
    Enum class that specifies the watermark type.

    Attributes:
        NoWatermark: Represents no watermark.
        PictureWatermark: Represents a picture watermark.
        TextWatermark: Represents a text watermark.
    """
    NoWatermark = 0
    PictureWatermark = 1
    TextWatermark = 2
