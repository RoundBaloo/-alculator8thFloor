from enum import Enum
from plum import dispatch
from typing import TypeVar, Union, Generic, List, Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class SdtAppearance(Enum):
    """
    Enum class representing the appearance of an Sdt object.

    """
    BoundingBox = 0
    Tags = 1
    Hidden = 2
    Default = 0
