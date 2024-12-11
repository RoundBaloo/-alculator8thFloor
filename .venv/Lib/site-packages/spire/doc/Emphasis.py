from enum import Enum
from plum import dispatch
from typing import TypeVar, Union, Generic, List, Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class Emphasis(Enum):
    """
    Specifies the emphasis mark type.

    """
    none = 0
    Dot = 1
    CommaAbove = 2
    CircleAbove = 3
    DotBelow = 4
    Default = 0
