from enum import Enum
from plum import dispatch
from typing import TypeVar, Union, Generic, List, Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class LockSettingsType(Enum):
    """
    Enum class representing different lock settings types.
    """
    UnLocked = 0
    ContentLocked = 1
    SDTContentLocked = 2
    SDTLocked = 3

