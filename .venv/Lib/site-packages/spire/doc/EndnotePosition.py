from enum import Enum
from plum import dispatch
from typing import TypeVar, Union, Generic, List, Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class EndnotePosition(Enum):
    """
    Enum class representing the endnote position of the Document.

    """
    DisplayEndOfSection = 0
    DisplayEndOfDocument = 3
