from enum import Enum
from plum import dispatch
from typing import TypeVar, Union, Generic, List, Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class VerticalRelation(Enum):
    """
    The enum defines the vertical relation.

    Attributes:
        Margin (int): Represents the margin vertical relation.
        Page (int): Represents the page vertical relation.
        Paragraph (int): Represents the paragraph vertical relation.
    """
    Margin = 0
    Page = 1
    Paragraph = 2

