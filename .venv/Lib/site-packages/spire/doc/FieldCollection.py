from enum import Enum
from plum import dispatch
from typing import TypeVar, Union, Generic, List, Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class FieldCollection (  CollectionEx) :
    """
    A collection of fields.
    """

    def get_Item(self ,index:int)->'Field':
        """
        Gets the field at the specified index.

        Args:
            index (int): The index of the field.

        Returns:
            Field: The field at the specified index.
        """
        
        GetDllLibDoc().FieldCollection_get_Item.argtypes=[c_void_p ,c_int]
        GetDllLibDoc().FieldCollection_get_Item.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().FieldCollection_get_Item,self.Ptr, index)
        ret = None if intPtr==None else Field(intPtr)
        return ret
