from enum import Enum
from plum import dispatch
from typing import TypeVar, Union, Generic, List, Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class FontClipPrecision(Enum):
    """
    Enum class for font clip precision options.
    """

    CLIP_DEFAULT_PRECIS = 0
    CLIP_CHARACTER_PRECIS = 1
    CLIP_STROKE_PRECIS = 2
    CLIP_MASK = 15
    CLIP_LH_ANGLES = 16
    CLIP_TT_ALWAYS = 32
    CLIP_DFA_DISABLE = 64
    CLIP_EMBEDDED = 128
