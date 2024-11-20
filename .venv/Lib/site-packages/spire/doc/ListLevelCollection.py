from enum import Enum
from plum import dispatch
from typing import TypeVar, Union, Generic, List, Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class ListLevelCollection (  DocumentSerializableCollection) :
    """
    Represents a collection of list formatting for each level in a list.
    """

    def get_Item(self ,index:int)->'ListLevel':
        """
        Gets the ListLevel at the specified index.

        Args:
            index (int): The index of the ListLevel.

        Returns:
            ListLevel: The ListLevel at the specified index.
        """
        
        GetDllLibDoc().ListLevelCollection_get_Item.argtypes=[c_void_p ,c_int]
        GetDllLibDoc().ListLevelCollection_get_Item.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().ListLevelCollection_get_Item,self.Ptr, index)
        ret = None if intPtr==None else ListLevel(intPtr)
        return ret
