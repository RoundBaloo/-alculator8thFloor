from enum import Enum
from plum import dispatch
from typing import TypeVar, Union, Generic, List, Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class HyperlinkType(Enum):
    """
    Enum class that specifies the type of the hyperlink.

    """
    none = 0
    FileLink = 1
    WebLink = 2
    EMailLink = 3
    Bookmark = 4
