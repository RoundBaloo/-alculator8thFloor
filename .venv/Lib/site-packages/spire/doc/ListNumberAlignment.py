from enum import Enum
from plum import dispatch
from typing import TypeVar, Union, Generic, List, Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class ListNumberAlignment(Enum):
    """
    Enum for number alignments.

    Attributes:
        Left: Represents left alignment.
        Center: Represents center alignment.
        Right: Represents right alignment.
    """
    Left = 0
    Center = 1
    Right = 2

