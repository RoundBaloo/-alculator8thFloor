from enum import Enum
from plum import dispatch
from typing import TypeVar, Union, Generic, List, Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class PageAlignment(Enum):
    """
    Specifies alignment of the text on a page.
    """
    Top = 0
    Middle = 1
    Justified = 2
    Bottom = 3
