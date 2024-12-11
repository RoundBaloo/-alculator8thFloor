from enum import Enum
from plum import dispatch
from typing import TypeVar,Union,Generic,List,Tuple
from spire.doc.common import *
from spire.doc.pages import *
from spire.doc import *
from ctypes import *
import abc

class LayoutElementType(Enum):
    """

    """
    none = 0
    Page = 1
    Column = 2
    Row = 8
    Cell = 16
    Line = 32
    Span = 64
    Footnote = 256
    Endnote = 512
    HeaderFooter = 1024
    TextBox = 2048
    Comment = 4096
    NoteSeparator = 8192

