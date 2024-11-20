from enum import Enum
from plum import dispatch
from typing import TypeVar, Union, Generic, List, Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class FontQuality(Enum):
    """
    Enum class representing different font qualities.
    """
    DEFAULT_QUALITY = 0
    DRAFT_QUALITY = 1
    PROOF_QUALITY = 2
    NONANTIALIASED_QUALITY = 3
    ANTIALIASED_QUALITY = 4
    CLEARTYPE_QUALITY = 5
    CLEARTYPE_NATURAL_QUALITY = 6

