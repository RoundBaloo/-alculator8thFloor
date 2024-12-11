from enum import Enum
from plum import dispatch
from typing import TypeVar, Union, Generic, List, Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class DropDownItem (  DocumentSerializable) :
    """
    Represents a drop-down item.
    """
    @property

    def Text(self)->str:
        """
        Gets or sets the text of the drop-down item.
        """
        GetDllLibDoc().DropDownItem_get_Text.argtypes=[c_void_p]
        GetDllLibDoc().DropDownItem_get_Text.restype=c_void_p
        ret = PtrToStr(CallCFunction(GetDllLibDoc().DropDownItem_get_Text,self.Ptr))
        return ret


    @Text.setter
    def Text(self, value:str):
        """
        Sets the text of the drop-down item.
        """
        valuePtr = StrToPtr(value)
        GetDllLibDoc().DropDownItem_set_Text.argtypes=[c_void_p, c_char_p]
        CallCFunction(GetDllLibDoc().DropDownItem_set_Text,self.Ptr, valuePtr)

