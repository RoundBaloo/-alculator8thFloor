from enum import Enum
from plum import dispatch
from typing import TypeVar, Union, Generic, List, Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class ColumnCollection (  DocumentSerializableCollection) :
    """
    A collection of Column objects that represent all the columns of text in a section of a document.
    """

    def get_Item(self ,index:int)->'Column':
        """
        Gets the Column at the specified index.
        """
        
        GetDllLibDoc().ColumnCollection_get_Item.argtypes=[c_void_p ,c_int]
        GetDllLibDoc().ColumnCollection_get_Item.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().ColumnCollection_get_Item,self.Ptr, index)
        ret = None if intPtr==None else Column(intPtr)
        return ret



    def Add(self ,column:'Column')->int:
        """
        Adds a Column object to the collection.
        """
        intPtrcolumn:c_void_p = column.Ptr

        GetDllLibDoc().ColumnCollection_Add.argtypes=[c_void_p ,c_void_p]
        GetDllLibDoc().ColumnCollection_Add.restype=c_int
        ret = CallCFunction(GetDllLibDoc().ColumnCollection_Add,self.Ptr, intPtrcolumn)
        return ret


    def Populate(self ,count:int,spacing:float):
        """
        Populates the specified number of columns with specified spacing.
        """
        
        GetDllLibDoc().ColumnCollection_Populate.argtypes=[c_void_p ,c_int,c_float]
        CallCFunction(GetDllLibDoc().ColumnCollection_Populate,self.Ptr, count,spacing)

    def Clear(self):
        """
        Removes all items.
        """
        GetDllLibDoc().ColumnCollection_Clear.argtypes=[c_void_p]
        CallCFunction(GetDllLibDoc().ColumnCollection_Clear,self.Ptr)

