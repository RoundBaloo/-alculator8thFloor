from enum import Enum
from plum import dispatch
from typing import TypeVar, Union, Generic, List, Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class TextFormFieldType(Enum):
    """
    Specifies the type of a text form field.
    """
    RegularText = 0
    NumberText = 1
    DateText = 2
    CurrentDate = 3
    CurrentTime = 4
    Calculation = 5
