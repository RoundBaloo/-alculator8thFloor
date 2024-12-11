from enum import Enum
from plum import dispatch
from typing import TypeVar, Union, Generic, List, Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class XHTMLValidationType(Enum):
    """
    Enum class representing the type of XHTML validation.

    Attributes:
        Strict: Represents strict XHTML validation.
        Transitional: Represents transitional XHTML validation.
        none: Represents no XHTML validation.
    """
    Strict = 0
    Transitional = 1
    none = 2

