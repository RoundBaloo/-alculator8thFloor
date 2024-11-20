from enum import Enum
from plum import dispatch
from typing import TypeVar, Union, Generic, List, Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class TextFormat(Enum):
    """
    Enum for defining different text formats.
    
    """
    none = 0
    Uppercase = 1
    Lowercase = 2
    FirstCapital = 3
    Titlecase = 4
