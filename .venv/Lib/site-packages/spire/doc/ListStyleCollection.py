from enum import Enum
from plum import dispatch
from typing import TypeVar, Union, Generic, List, Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class ListStyleCollection (  DocumentSerializableCollection) :
    """
    Represents a collection of list style
    """

    def get_Item(self ,index:int)->'ListStyle':
        """
        Gets the ListStyle at the specified index.

        Args:
            index: The index of the ListStyle.

        Returns:
            The ListStyle at the specified index.
        """
        
        GetDllLibDoc().ListStyleCollection_get_Item.argtypes=[c_void_p ,c_int]
        GetDllLibDoc().ListStyleCollection_get_Item.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().ListStyleCollection_get_Item,self.Ptr, index)
        ret = None if intPtr==None else ListStyle(intPtr)
        return ret



    def Add(self ,style:'ListStyle')->int:
        """
        Adds the list style into collection.

        Args:
            style: The ListStyle to be added.

        Returns:
            The index of the added ListStyle.
        """
        intPtrstyle:c_void_p = style.Ptr

        GetDllLibDoc().ListStyleCollection_Add.argtypes=[c_void_p ,c_void_p]
        GetDllLibDoc().ListStyleCollection_Add.restype=c_int
        ret = CallCFunction(GetDllLibDoc().ListStyleCollection_Add,self.Ptr, intPtrstyle)
        return ret


    def FindByName(self ,name:str)->'ListStyle':
        """
        Finds list style by name.

        Args:
            name: The name of the ListStyle.

        Returns:
            The ListStyle with the specified name.
        """
        namePtr = StrToPtr(name)
        GetDllLibDoc().ListStyleCollection_FindByName.argtypes=[c_void_p ,c_char_p]
        GetDllLibDoc().ListStyleCollection_FindByName.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().ListStyleCollection_FindByName,self.Ptr, namePtr)
        ret = None if intPtr==None else ListStyle(intPtr)
        return ret


