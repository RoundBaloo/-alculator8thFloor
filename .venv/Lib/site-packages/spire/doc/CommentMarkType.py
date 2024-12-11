from enum import Enum
from plum import dispatch
from typing import TypeVar, Union, Generic, List, Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class CommentMarkType(Enum):
    """
    Defines types of comment mark.
    """
    CommentStart = 0
    CommentEnd = 1

