from enum import Enum
from plum import dispatch
from typing import TypeVar, Union, Generic, List, Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class FootnoteType(Enum):
    """
    Specifies the Type of the FootNote.
    """
    Footnote = 0
    Endnote = 1
