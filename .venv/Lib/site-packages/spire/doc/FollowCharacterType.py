from enum import Enum
from plum import dispatch
from typing import TypeVar, Union, Generic, List, Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class FollowCharacterType(Enum):
    """
    The type of character following the number text for the paragraph
    """
    Tab = 0
    Space = 1
    Nothing = 2
