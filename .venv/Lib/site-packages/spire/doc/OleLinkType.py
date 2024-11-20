from enum import Enum
from plum import dispatch
from typing import TypeVar, Union, Generic, List, Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class OleLinkType(Enum):
    """
    Enum class that defines types of the ole object field.
    """

    Embed = 0
    Link = 1
