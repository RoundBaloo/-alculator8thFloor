from enum import Enum
from plum import dispatch
from typing import TypeVar, Union, Generic, List, Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class SdtDropDownList (  SdtDropDownListBase) :
    """
    Represents a drop-down list in a document.
    """
    @dispatch
    def __init__(self):
        """
        Initializes a new instance of the SdtDropDownList class.
        """
        GetDllLibDoc().SdtDropDownList_CreateSdtDropDownList.restype = c_void_p
        intPtr = CallCFunction(GetDllLibDoc().SdtDropDownList_CreateSdtDropDownList,)
        super(SdtDropDownList, self).__init__(intPtr)
