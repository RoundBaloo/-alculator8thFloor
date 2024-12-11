from enum import Enum
from plum import dispatch
from typing import TypeVar, Union, Generic, List, Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class DocumentVersion(Enum):
    """
    Enum class that defines document versions.
    """

    Word97 = 0
    Word2000 = 1
    Word2002 = 2
    Word2003 = 3
    Word2007 = 4
