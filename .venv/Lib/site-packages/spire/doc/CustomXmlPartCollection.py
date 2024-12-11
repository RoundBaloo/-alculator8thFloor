from enum import Enum
from plum import dispatch
from typing import TypeVar, Union, Generic, List, Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class CustomXmlPartCollection (  IEnumerable) :
    """
    Represents a collection of custom XML parts.
    """

    @property
    def Count(self) -> int:
        """
        Gets the number of custom XML parts in the collection.
        """
        GetDllLibDoc().CustomXmlPartCollection_get_Count.argtypes=[c_void_p]
        GetDllLibDoc().CustomXmlPartCollection_get_Count.restype=c_int
        ret = CallCFunction(GetDllLibDoc().CustomXmlPartCollection_get_Count,self.Ptr)
        return ret


    def get_Item(self ,index:int)->'CustomXmlPart':
        """
        Gets the custom XML part at the specified index.

        Args:
            index: The index of the custom XML part to get.

        Returns:
            The custom XML part at the specified index.
        """
        
        GetDllLibDoc().CustomXmlPartCollection_get_Item.argtypes=[c_void_p ,c_int]
        GetDllLibDoc().CustomXmlPartCollection_get_Item.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().CustomXmlPartCollection_get_Item,self.Ptr, index)
        ret = None if intPtr==None else CustomXmlPart(intPtr)
        return ret

    def set_Item(self, index: int, value: 'CustomXmlPart'):
        """
        Sets the custom XML part at the specified index.

        Args:
            index: The index of the custom XML part to set.
            value: The custom XML part to set.
        """
        intPtrvalue:c_void_p = value.Ptr

        GetDllLibDoc().CustomXmlPartCollection_set_Item.argtypes=[c_void_p ,c_int,c_void_p]
        CallCFunction(GetDllLibDoc().CustomXmlPartCollection_set_Item,self.Ptr, index,intPtrvalue)


    def GetEnumerator(self)->'IEnumerator':
        """
        Returns an enumerator that iterates through the collection.

        Returns:
            An enumerator that can be used to iterate through the collection.
        """
        GetDllLibDoc().CustomXmlPartCollection_GetEnumerator.argtypes=[c_void_p]
        GetDllLibDoc().CustomXmlPartCollection_GetEnumerator.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().CustomXmlPartCollection_GetEnumerator,self.Ptr)
        ret = None if intPtr==None else IEnumerator(intPtr)
        return ret



    def Add(self ,part:'CustomXmlPart'):
        """
        Adds a custom XML part to the collection.

        Args:
            part: The custom XML part to add.
        """
        intPtrpart:c_void_p = part.Ptr

        GetDllLibDoc().CustomXmlPartCollection_Add.argtypes=[c_void_p ,c_void_p]
        CallCFunction(GetDllLibDoc().CustomXmlPartCollection_Add,self.Ptr, intPtrpart)


    def RemoveAt(self ,index:int):
        """
        Removes the custom XML part at the specified index.

        Args:
            index: The index of the custom XML part to remove.
        """
        GetDllLibDoc().CustomXmlPartCollection_RemoveAt.argtypes = [c_void_p, c_int]
        GetDllLibDoc().CustomXmlPartCollection_RemoveAt(self.Ptr, index)

    def Clear(self):
        """
        Removes all custom XML parts from the collection.
        """
        GetDllLibDoc().CustomXmlPartCollection_Clear.argtypes=[c_void_p]
        CallCFunction(GetDllLibDoc().CustomXmlPartCollection_Clear,self.Ptr)


    def GetById(self ,id:str)->'CustomXmlPart':
        """
        Gets the custom XML part with the specified ID.

        Args:
            id: The ID of the custom XML part to get.

        Returns:
            The custom XML part with the specified ID.
        """
        idPtr = StrToPtr(id)
        GetDllLibDoc().CustomXmlPartCollection_GetById.argtypes=[c_void_p ,c_char_p]
        GetDllLibDoc().CustomXmlPartCollection_GetById.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().CustomXmlPartCollection_GetById,self.Ptr, idPtr)
        ret = None if intPtr==None else CustomXmlPart(intPtr)
        return ret



    def Clone(self)->'CustomXmlPartCollection':
        """
        Creates a new collection that is a copy of the current collection.

        Returns:
            A new collection that is a copy of the current collection.
        """
        GetDllLibDoc().CustomXmlPartCollection_Clone.argtypes=[c_void_p]
        GetDllLibDoc().CustomXmlPartCollection_Clone.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().CustomXmlPartCollection_Clone,self.Ptr)
        ret = None if intPtr==None else CustomXmlPartCollection(intPtr)
        return ret
