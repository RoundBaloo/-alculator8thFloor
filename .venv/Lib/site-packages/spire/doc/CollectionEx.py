from enum import Enum
from plum import dispatch
from typing import TypeVar,Union,Generic,List,Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class CollectionEx (  OwnerHolder, IEnumerable) :
    """
    Represents a collection with extended functionality.
    """
    @property
    def Count(self)->int:
        """
        Gets the number of items in the collection.

        Returns:
            The count of items in the collection.
        """
        GetDllLibDoc().CollectionEx_get_Count.argtypes=[c_void_p]
        GetDllLibDoc().CollectionEx_get_Count.restype=c_int
        ret = CallCFunction(GetDllLibDoc().CollectionEx_get_Count,self.Ptr)
        return ret


    def GetEnumerator(self)->'IEnumerator':
        """
        Returns an enumerator that iterates through a collection.

        Returns:
            An IEnumerator object that can be used to iterate through the collection.
        """
        GetDllLibDoc().CollectionEx_GetEnumerator.argtypes=[c_void_p]
        GetDllLibDoc().CollectionEx_GetEnumerator.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().CollectionEx_GetEnumerator,self.Ptr)
        ret = None if intPtr==None else IEnumerator(intPtr)
        return ret
