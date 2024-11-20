from enum import Enum
from plum import dispatch
from typing import TypeVar, Union, Generic, List, Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class SdtType(Enum):
    """
    Specifies the type of a structured document tag (SDT) Element.
    """
    none = 0
    RichText = 1
    Bibliography = 2
    Citation = 3
    ComboBox = 4
    DropDownList = 5
    Picture = 6
    Text = 7
    Equation = 8
    DatePicker = 9
    BuildingBlockGallery = 10
    DocPartObj = 11
    Group = 12
    CheckBox = 13
    RepeatingSection = 14
    EntityPicker = 15
