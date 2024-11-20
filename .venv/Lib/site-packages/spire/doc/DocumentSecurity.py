from enum import Enum
from plum import dispatch
from typing import TypeVar, Union, Generic, List, Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class DocumentSecurity(Enum):
    """
    Enum class representing different document security options.
    """
    none = 0
    PasswordProtected = 1
    ReadOnlyRecommended = 2
    ReadOnlyEnforced = 4
    ReadOnlyExceptAnnotations = 8
