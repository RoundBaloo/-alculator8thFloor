from enum import Enum
from plum import dispatch
from typing import TypeVar, Union, Generic, List, Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class OutlineLevel(Enum):
    """
    Enum defining paragraph format's outline level.
    
    """
    Level1 = 0
    Level2 = 1
    Level3 = 2
    Level4 = 3
    Level5 = 4
    Level6 = 5
    Level7 = 6
    Level8 = 7
    Level9 = 8
    Body = 9
