from enum import Enum
from plum import dispatch
from typing import TypeVar, Union, Generic, List, Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class TextAnchor(Enum):
    """
    Specifies vertical alignment of a textbox.
    """
    Top = 1
    Center = 2
    Bottom = 3
