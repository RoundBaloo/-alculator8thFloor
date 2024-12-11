from enum import Enum
from plum import dispatch
from typing import TypeVar, Union, Generic, List, Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class DropDownCollection (  DocumentSerializableCollection) :
    """
    Represent a collection of DropDownItem objects.
    """

    def get_Item(self ,index:int)->'DropDownItem':
        """
        Gets the DropDownItem at the specified index.
        """
        
        GetDllLibDoc().DropDownCollection_get_Item.argtypes=[c_void_p ,c_int]
        GetDllLibDoc().DropDownCollection_get_Item.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().DropDownCollection_get_Item,self.Ptr, index)
        ret = None if intPtr==None else DropDownItem(intPtr)
        return ret

    def Add(self, text: str) -> 'DropDownItem':
        """
        Adds the item.
        """
        textPtr = StrToPtr(text)
        GetDllLibDoc().DropDownCollection_Add.argtypes=[c_void_p ,c_char_p]
        GetDllLibDoc().DropDownCollection_Add.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().DropDownCollection_Add,self.Ptr, textPtr)
        from spire.doc import DropDownItem
        ret = None if intPtr==None else DropDownItem(intPtr)
        return ret



    def Remove(self ,index:int):
        """
        Removes DropDownItems by index.
        """
        
        GetDllLibDoc().DropDownCollection_Remove.argtypes=[c_void_p ,c_int]
        CallCFunction(GetDllLibDoc().DropDownCollection_Remove,self.Ptr, index)

    def Clear(self):
        """
        Clears this instance.
        """
        GetDllLibDoc().DropDownCollection_Clear.argtypes=[c_void_p]
        CallCFunction(GetDllLibDoc().DropDownCollection_Clear,self.Ptr)

