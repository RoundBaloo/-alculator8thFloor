from enum import Enum
from plum import dispatch
from typing import TypeVar, Union, Generic, List, Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class RowCollection (  DocumentObjectCollection) :
    """
    A collection of table rows.
    """

    def get_Item(self ,index:int)->'TableRow':
        """
        Retrieves a table row from the collection by index.
        :param index: The index of the row.
        :return: The table row.
        """
        
        GetDllLibDoc().RowCollection_get_Item.argtypes=[c_void_p ,c_int]
        GetDllLibDoc().RowCollection_get_Item.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().RowCollection_get_Item,self.Ptr, index)
        ret = None if intPtr==None else TableRow(intPtr)
        return ret



    def Add(self ,row:'TableRow')->int:
        """
        Adds a table row to the collection.
        :param row: The row to add.
        :return: The index of the added row.
        """
        intPtrrow:c_void_p = row.Ptr

        GetDllLibDoc().RowCollection_Add.argtypes=[c_void_p ,c_void_p]
        GetDllLibDoc().RowCollection_Add.restype=c_int
        ret = CallCFunction(GetDllLibDoc().RowCollection_Add,self.Ptr, intPtrrow)
        return ret


    def Insert(self ,index:int,row:'TableRow'):
        """
        Inserts a table row into the collection at the specified index.
        :param index: The index at which to insert the row.
        :param row: The row to insert.
        """
        intPtrrow:c_void_p = row.Ptr

        GetDllLibDoc().RowCollection_Insert.argtypes=[c_void_p ,c_int,c_void_p]
        CallCFunction(GetDllLibDoc().RowCollection_Insert,self.Ptr, index,intPtrrow)


    def IndexOf(self ,row:'TableRow')->int:
        """
        Returns the index of a specified row in the collection.
        :param row: The row to find the index of.
        :return: The index of the row.
        """
        intPtrrow:c_void_p = row.Ptr

        GetDllLibDoc().RowCollection_IndexOf.argtypes=[c_void_p ,c_void_p]
        GetDllLibDoc().RowCollection_IndexOf.restype=c_int
        ret = CallCFunction(GetDllLibDoc().RowCollection_IndexOf,self.Ptr, intPtrrow)
        return ret


    def Remove(self ,row:'TableRow'):
        """
        Removes a specified row from the collection.
        :param row: The row to remove.
        """
        intPtrrow:c_void_p = row.Ptr

        GetDllLibDoc().RowCollection_Remove.argtypes=[c_void_p ,c_void_p]
        CallCFunction(GetDllLibDoc().RowCollection_Remove,self.Ptr, intPtrrow)

