from enum import Enum
from plum import dispatch
from typing import TypeVar, Union, Generic, List, Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class ProtectionType(Enum):
    """
    Enum class representing the type of protection in the document.

    """
    AllowOnlyComments = 1
    AllowOnlyFormFields = 2
    AllowOnlyReading = 3
    AllowOnlyRevisions = 0
    NoProtection = -1

