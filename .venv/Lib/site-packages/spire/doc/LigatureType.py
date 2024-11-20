from enum import Enum
from plum import dispatch
from typing import TypeVar, Union, Generic, List, Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class LigatureType(Enum):
    """
    Enum class that specifies the ligature type.

    """
    none = 0
    Standard = 1
    Contextual = 2
    DefaultContextual = 3
    Historical = 4
    DefaultHistorical = 5
    ContextualHistorical = 6
    DefaultContextualHistorical = 7
    Discretional = 8
    DefaultDiscretional = 9
    ContextualDiscretional = 10
    DefaultContextualDiscretional = 11
    HistoricalDiscretional = 12
    DefaultHistoricalDiscretional = 13
    ContextualHistoricalDiscretional = 14
    All = 15
