from enum import Enum
from plum import dispatch
from typing import TypeVar, Union, Generic, List, Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class HorizontalAlignment(Enum):
    """
    Specifies the type of horizontal alignment.
    
    """
    Left = 0
    Center = 1
    Right = 2
    Justify = 3
    Distribute = 4
    ThaiDistribute = 5
    HightKashida = 6
    LowKashida = 7
    MediumKashida = 8
