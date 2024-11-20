from enum import Enum
from plum import dispatch
from typing import TypeVar, Union, Generic, List, Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class SectionBreakType(Enum):
    """
    Specifies type of the section break code.
    """
    NoBreak = 0
    NewColumn = 1
    NewPage = 2
    EvenPage = 3
    Oddpage = 4

