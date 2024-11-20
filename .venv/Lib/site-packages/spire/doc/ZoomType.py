from enum import Enum
from plum import dispatch
from typing import TypeVar, Union, Generic, List, Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class ZoomType(Enum):
    """
    Specifies zooming type in Microsoft Word.

    Attributes:
        none (int): No zooming.
        FullPage (int): Zoom to full page.
        PageWidth (int): Zoom to page width.
        TextFit (int): Zoom to fit text.
    """
    none = 0
    FullPage = 1
    PageWidth = 2
    TextFit = 3
