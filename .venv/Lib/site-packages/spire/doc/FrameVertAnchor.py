from enum import Enum
from plum import dispatch
from typing import TypeVar, Union, Generic, List, Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class FrameVertAnchor(Enum):
    """
    Specifies the vertical frame anchor.
    """

    Margin = 0
    Page = 1
    Text = 2
