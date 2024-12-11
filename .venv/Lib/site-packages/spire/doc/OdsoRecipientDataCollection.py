from enum import Enum
from plum import dispatch
from typing import TypeVar,Union,Generic,List,Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class OdsoRecipientDataCollection (  IEnumerable) :
    """
    Represents a collection of OdsoRecipientData objects.
    """
    @property
    def Count(self)->int:
        """
        Gets the number of elements in the collection.
        """
        GetDllLibDoc().OdsoRecipientDataCollection_get_Count.argtypes=[c_void_p]
        GetDllLibDoc().OdsoRecipientDataCollection_get_Count.restype=c_int
        ret = CallCFunction(GetDllLibDoc().OdsoRecipientDataCollection_get_Count,self.Ptr)
        return ret


    def get_Item(self ,index:int)->'OdsoRecipientData':
        """
        Gets the OdsoRecipientData object at the specified index.

        Args:
            index: The index of the OdsoRecipientData object to get.

        Returns:
            The OdsoRecipientData object at the specified index.
        """
        
        GetDllLibDoc().OdsoRecipientDataCollection_get_Item.argtypes=[c_void_p ,c_int]
        GetDllLibDoc().OdsoRecipientDataCollection_get_Item.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().OdsoRecipientDataCollection_get_Item,self.Ptr, index)
        ret = None if intPtr==None else OdsoRecipientData(intPtr)
        return ret



    def set_Item(self ,index:int,value:'OdsoRecipientData'):
        """
        Sets the OdsoRecipientData object at the specified index.

        Args:
            index: The index at which to set the OdsoRecipientData object.
            value: The OdsoRecipientData object to set.
        """
        intPtrvalue:c_void_p = value.Ptr

        GetDllLibDoc().OdsoRecipientDataCollection_set_Item.argtypes=[c_void_p ,c_int,c_void_p]
        CallCFunction(GetDllLibDoc().OdsoRecipientDataCollection_set_Item,self.Ptr, index,intPtrvalue)


    def GetEnumerator(self)->'IEnumerator':
        """
        Returns an enumerator that iterates through the collection.

        Returns:
            An IEnumerator object that can be used to iterate through the collection.
        """
        GetDllLibDoc().OdsoRecipientDataCollection_GetEnumerator.argtypes=[c_void_p]
        GetDllLibDoc().OdsoRecipientDataCollection_GetEnumerator.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().OdsoRecipientDataCollection_GetEnumerator,self.Ptr)
        ret = None if intPtr==None else IEnumerator(intPtr)
        return ret



    def Add(self ,value:'OdsoRecipientData')->int:
        """
        Adds an OdsoRecipientData object to the end of the collection.

        Args:
            value: The OdsoRecipientData object to add.

        Returns:
            The index at which the OdsoRecipientData object was added.
        """
        intPtrvalue:c_void_p = value.Ptr

        GetDllLibDoc().OdsoRecipientDataCollection_Add.argtypes=[c_void_p ,c_void_p]
        GetDllLibDoc().OdsoRecipientDataCollection_Add.restype=c_int
        ret = CallCFunction(GetDllLibDoc().OdsoRecipientDataCollection_Add,self.Ptr, intPtrvalue)
        return ret

    def Clear(self):
        """
        Removes all elements from the collection.
        """
        GetDllLibDoc().OdsoRecipientDataCollection_Clear.argtypes=[c_void_p]
        CallCFunction(GetDllLibDoc().OdsoRecipientDataCollection_Clear,self.Ptr)


    def RemoveAt(self ,index:int):
        """
        Removes the OdsoRecipientData object at the specified index.

        Args:
            index: The index of the OdsoRecipientData object to remove.
        """
        
        GetDllLibDoc().OdsoRecipientDataCollection_RemoveAt.argtypes=[c_void_p ,c_int]
        CallCFunction(GetDllLibDoc().OdsoRecipientDataCollection_RemoveAt,self.Ptr, index)

