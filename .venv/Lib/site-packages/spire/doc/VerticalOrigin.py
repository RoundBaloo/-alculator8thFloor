from enum import Enum
from plum import dispatch
from typing import TypeVar, Union, Generic, List, Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class VerticalOrigin(Enum):
    """
    Enum class for specifying the vertical origin of an object.
    
    Attributes:
        Margin: The object is aligned with the margin.
        Page: The object is aligned with the page.
        Paragraph: The object is aligned with the paragraph.
        Line: The object is aligned with the line.
        TopMarginArea: The object is aligned with the top margin area.
        BottomMarginArea: The object is aligned with the bottom margin area.
        InnerMarginArea: The object is aligned with the inner margin area.
        OuterMarginArea: The object is aligned with the outer margin area.
        TextFrameDefault: The object is aligned with the default text frame.
    """
    Margin = 0
    Page = 1
    Paragraph = 2
    Line = 3
    TopMarginArea = 4
    BottomMarginArea = 5
    InnerMarginArea = 6
    OuterMarginArea = 7
    TextFrameDefault = 2

