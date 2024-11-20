from enum import Enum
from plum import dispatch
from typing import TypeVar, Union, Generic, List, Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class GroupedShapeOrigin(Enum):
    """
    Enum to specify the vertical/horizontal origin of an object in the GroupedShape.
    
    """
    UpperLeftCorner = 0
    Center = 1
