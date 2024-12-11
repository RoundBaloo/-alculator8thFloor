from enum import Enum
from plum import dispatch
from typing import TypeVar, Union, Generic, List, Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class CellMerge(Enum):
    """
    Specifies the way of cell merging.
    """
    none = 0
    Start = 1
    Continue = 2
