from enum import Enum
from plum import dispatch
from typing import TypeVar, Union, Generic, List, Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class FontPitch(Enum):
    """
    Enum class representing different font pitches.
    """
    Default = 0
    Fixed = 1
    Variable = 2
