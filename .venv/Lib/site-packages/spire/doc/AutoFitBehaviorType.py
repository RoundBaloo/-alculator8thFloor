from enum import Enum
from plum import dispatch
from typing import TypeVar, Union, Generic, List, Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class AutoFitBehaviorType(Enum):
    """
    Specifies how Microsoft Word resizes a table when the AutoFit feature is used.
    """
    AutoFitToContents = 1
    AutoFitToWindow = 2
    FixedColumnWidths = 0
