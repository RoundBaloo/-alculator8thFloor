from enum import Enum
from plum import dispatch
from typing import TypeVar, Union, Generic, List, Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class LineNumberingRestartMode(Enum):
    """
    Specifies when line numbering is restarted. 

    """
    RestartPage = 0
    RestartSection = 1
    Continuous = 2
    none = 255
