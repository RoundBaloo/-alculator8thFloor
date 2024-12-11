from enum import Enum
from plum import dispatch
from typing import TypeVar, Union, Generic, List, Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class SubSuperScript(Enum):
    """
    Specifies the type of the SubSuperScript.
    """
    none = 0
    SuperScript = 1
    SubScript = 2
    BaseLine = 0
