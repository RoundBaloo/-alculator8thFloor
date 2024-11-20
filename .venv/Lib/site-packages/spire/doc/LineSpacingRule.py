from enum import Enum
from plum import dispatch
from typing import TypeVar, Union, Generic, List, Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class LineSpacingRule(Enum):
    """
    Enum for paragraph line spacing rule.

    """
    AtLeast = 0
    Exactly = 1
    Multiple = 2
