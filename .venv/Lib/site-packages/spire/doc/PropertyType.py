from enum import Enum
from plum import dispatch
from typing import TypeVar, Union, Generic, List, Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class PropertyType(Enum):
    """
    Specifies Type of the Property.
    """
    Summary = 0
    DocumentSummary = 1
    Custom = 2

