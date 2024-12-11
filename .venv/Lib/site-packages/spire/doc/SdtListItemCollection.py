from enum import Enum
from plum import dispatch
from typing import TypeVar, Union, Generic, List, Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class SdtListItemCollection (  IEnumerable) :
    """
    Represents a collection of SdtListItem objects.
    """

    def GetEnumerator(self)->'IEnumerator':
        """
        Returns an enumerator that iterates through the collection.
        """
        GetDllLibDoc().SdtListItemCollection_GetEnumerator.argtypes=[c_void_p]
        GetDllLibDoc().SdtListItemCollection_GetEnumerator.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().SdtListItemCollection_GetEnumerator,self.Ptr)
        ret = None if intPtr==None else IEnumerator(intPtr)
        return ret



    def Add(self ,item:'SdtListItem'):
        """
        Adds an item to the collection.
        """
        intPtritem:c_void_p = item.Ptr

        GetDllLibDoc().SdtListItemCollection_Add.argtypes=[c_void_p ,c_void_p]
        CallCFunction(GetDllLibDoc().SdtListItemCollection_Add,self.Ptr, intPtritem)


    def RemoveAt(self ,index:int):
        """
        Removes the item at the specified index.
        """
        
        GetDllLibDoc().SdtListItemCollection_RemoveAt.argtypes=[c_void_p ,c_int]
        CallCFunction(GetDllLibDoc().SdtListItemCollection_RemoveAt,self.Ptr, index)

    def Clear(self):
        """
        Removes all items from the collection.
        """
        GetDllLibDoc().SdtListItemCollection_Clear.argtypes=[c_void_p]
        CallCFunction(GetDllLibDoc().SdtListItemCollection_Clear,self.Ptr)

    @property

    def SelectedValue(self)->'SdtListItem':
        """
        Gets or sets the selected value from the collection.
        """
        GetDllLibDoc().SdtListItemCollection_get_SelectedValue.argtypes=[c_void_p]
        GetDllLibDoc().SdtListItemCollection_get_SelectedValue.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().SdtListItemCollection_get_SelectedValue,self.Ptr)
        ret = None if intPtr==None else SdtListItem(intPtr)
        return ret


    @SelectedValue.setter
    def SelectedValue(self, value:'SdtListItem'):
        """
        Sets the selected value in the collection.
        """
        GetDllLibDoc().SdtListItemCollection_set_SelectedValue.argtypes=[c_void_p, c_void_p]
        CallCFunction(GetDllLibDoc().SdtListItemCollection_set_SelectedValue,self.Ptr, value.Ptr)


    def get_Item(self ,index:int)->'SdtListItem':
        """
        Gets the item at the specified index.
        """
        
        GetDllLibDoc().SdtListItemCollection_get_Item.argtypes=[c_void_p ,c_int]
        GetDllLibDoc().SdtListItemCollection_get_Item.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().SdtListItemCollection_get_Item,self.Ptr, index)
        ret = None if intPtr==None else SdtListItem(intPtr)
        return ret


    @property
    def Count(self)->int:
        """
        Gets the number of items in the collection.
        """
        GetDllLibDoc().SdtListItemCollection_get_Count.argtypes=[c_void_p]
        GetDllLibDoc().SdtListItemCollection_get_Count.restype=c_int
        ret = CallCFunction(GetDllLibDoc().SdtListItemCollection_get_Count,self.Ptr)
        return ret

