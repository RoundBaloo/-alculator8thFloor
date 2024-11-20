from enum import Enum
from plum import dispatch
from typing import TypeVar, Union, Generic, List, Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class SdtListItem (SpireObject) :
    """
    Represents an item in a list.
    """
    @dispatch
    def __init__(self, displayText:str, value:str):
        """
        Initializes a new instance of the SdtListItem class with the specified display text and value.

        Args:
            displayText: The display text of the item.
            value: The value of the item.
        """
        displayTextPtr = StrToPtr(displayText)
        valuePtr = StrToPtr(value)
        GetDllLibDoc().SdtListItem_CreateSdtListItemDV.argtypes=[c_char_p,c_char_p]
        GetDllLibDoc().SdtListItem_CreateSdtListItemDV.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().SdtListItem_CreateSdtListItemDV,displayTextPtr,valuePtr)
        super(SdtListItem, self).__init__(intPtr)

    @dispatch
    def __init__(self, value:str):
        """
        Initializes a new instance of the SdtListItem class with the specified value.

        Args:
            value: The value of the item.
        """
        valuePtr = StrToPtr(value)
        GetDllLibDoc().SdtListItem_CreateSdtListItemV.argtypes=[c_char_p]
        GetDllLibDoc().SdtListItem_CreateSdtListItemV.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().SdtListItem_CreateSdtListItemV,valuePtr)
        super(SdtListItem, self).__init__(intPtr)

    @property

    def DisplayText(self)->str:
        """
        Gets or sets the display text of the item.

        Returns:
            The display text of the item.
        """
        GetDllLibDoc().SdtListItem_get_DisplayText.argtypes=[c_void_p]
        GetDllLibDoc().SdtListItem_get_DisplayText.restype=c_void_p
        ret = PtrToStr(CallCFunction(GetDllLibDoc().SdtListItem_get_DisplayText,self.Ptr))
        return ret


    @DisplayText.setter
    def DisplayText(self, value:str):
        """
        Sets the display text of the item.

        Args:
            value: The display text to set.
        """
        valuePtr = StrToPtr(value)
        GetDllLibDoc().SdtListItem_set_DisplayText.argtypes=[c_void_p, c_char_p]
        CallCFunction(GetDllLibDoc().SdtListItem_set_DisplayText,self.Ptr, valuePtr)

    @property

    def Value(self)->str:
        """
        Gets or sets the value of the item.

        Returns:
            The value of the item.
        """
        GetDllLibDoc().SdtListItem_get_Value.argtypes=[c_void_p]
        GetDllLibDoc().SdtListItem_get_Value.restype=c_void_p
        ret = PtrToStr(CallCFunction(GetDllLibDoc().SdtListItem_get_Value,self.Ptr))
        return ret


    @Value.setter
    def Value(self, value:str):
        """
        Sets the value of the item.

        Args:
            value: The value to set.
        """
        valuePtr = StrToPtr(value)
        GetDllLibDoc().SdtListItem_set_Value.argtypes=[c_void_p, c_char_p]
        CallCFunction(GetDllLibDoc().SdtListItem_set_Value,self.Ptr, valuePtr)

