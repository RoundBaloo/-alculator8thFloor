from enum import Enum
from plum import dispatch
from typing import TypeVar, Union, Generic, List, Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class ImportOptions(Enum):
    """
    Enum class for import options.
    """
    KeepSourceFormatting = 0
    MergeFormatting = 1
    KeepTextOnly = 2
    UseDestinationStyles = 3

