from enum import Enum
from plum import dispatch
from typing import TypeVar, Union, Generic, List, Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class SdtDropDownListBase (  SdtControlProperties) :
    """
    Represents a base class for drop-down list content controls in a Word document.
    """
    @property

    def ListItems(self)->'SdtListItemCollection':
        """
        Provides access to all list items of this drop-down list content control.
        Returns:
            An instance of SdtListItemCollection representing the list items.
        """
        GetDllLibDoc().SdtDropDownListBase_get_ListItems.argtypes=[c_void_p]
        GetDllLibDoc().SdtDropDownListBase_get_ListItems.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().SdtDropDownListBase_get_ListItems,self.Ptr)
        from spire.doc import SdtListItemCollection
        ret = None if intPtr==None else SdtListItemCollection(intPtr)
        return ret


    @property

    def LastValue(self)->str:
        """
        Gets or sets the last selected value of the drop-down list content control.
        Returns:
            A string representing the last selected value.
        """
        GetDllLibDoc().SdtDropDownListBase_get_LastValue.argtypes=[c_void_p]
        GetDllLibDoc().SdtDropDownListBase_get_LastValue.restype=c_void_p
        ret = PtrToStr(CallCFunction(GetDllLibDoc().SdtDropDownListBase_get_LastValue,self.Ptr))
        return ret


    @LastValue.setter
    def LastValue(self, value:str):
        """
        Sets the last selected value of the drop-down list content control.
        Args:
            value: A string representing the last selected value.
        """
        valuePtr = StrToPtr(value)
        GetDllLibDoc().SdtDropDownListBase_set_LastValue.argtypes=[c_void_p, c_char_p]
        CallCFunction(GetDllLibDoc().SdtDropDownListBase_set_LastValue,self.Ptr, valuePtr)

