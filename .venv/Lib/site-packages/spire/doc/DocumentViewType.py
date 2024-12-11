from enum import Enum
from plum import dispatch
from typing import TypeVar, Union, Generic, List, Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class DocumentViewType(Enum):
    """
    Enum class that specifies view mode in Microsoft Word.

    """
    none = 0
    PrintLayout = 1
    OutlineLayout = 3
    NormalLayout = 4
    WebLayout = 5
