from enum import Enum
from plum import dispatch
from typing import TypeVar, Union, Generic, List, Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class TableCollection (  DocumentSubsetCollection, ITableCollection) :
    """
    Represents a collection of <see cref="!:Spire.Doc.ITable" /> objects.
    """

    def get_Item(self ,index:int)->'ITable':
        """
        Retrieves the table at the specified index.

        Args:
            index: The index of the table.

        Returns:
            The table at the specified index.
        """
        
        GetDllLibDoc().TableCollection_get_Item.argtypes=[c_void_p ,c_int]
        GetDllLibDoc().TableCollection_get_Item.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().TableCollection_get_Item,self.Ptr, index)
        #ret = None if intPtr==None else ITable(intPtr)
        ret = None if intPtr==None else Table(intPtr)
        return ret



    def Add(self ,table:'ITable')->int:
        """
        Adds a table to the end of the text body.

        Args:
            table: The table to be added.

        Returns:
            The index of the added table.
        """
        intPtrtable:c_void_p = table.Ptr

        GetDllLibDoc().TableCollection_Add.argtypes=[c_void_p ,c_void_p]
        GetDllLibDoc().TableCollection_Add.restype=c_int
        ret = CallCFunction(GetDllLibDoc().TableCollection_Add,self.Ptr, intPtrtable)
        return ret


    def Contains(self ,table:'ITable')->bool:
        """
        Determines whether the collection contains a specific table.

        Args:
            table: The table to be checked.

        Returns:
            True if the table is found in the collection, False otherwise.
        """
        intPtrtable:c_void_p = table.Ptr

        GetDllLibDoc().TableCollection_Contains.argtypes=[c_void_p ,c_void_p]
        GetDllLibDoc().TableCollection_Contains.restype=c_bool
        ret = CallCFunction(GetDllLibDoc().TableCollection_Contains,self.Ptr, intPtrtable)
        return ret


    def IndexOf(self ,table:'ITable')->int:
        """
        Determines the index of a specific table in the collection.

        Args:
            table: The table to find the index of.

        Returns:
            The index of the table in the collection.
        """
        intPtrtable:c_void_p = table.Ptr

        GetDllLibDoc().TableCollection_IndexOf.argtypes=[c_void_p ,c_void_p]
        GetDllLibDoc().TableCollection_IndexOf.restype=c_int
        ret = CallCFunction(GetDllLibDoc().TableCollection_IndexOf,self.Ptr, intPtrtable)
        return ret


    def Insert(self ,index:int,table:'ITable')->int:
        """
        Inserts a table into the collection at the specified index.

        Args:
            index: The index at which to insert the table.
            table: The table to be inserted.

        Returns:
            The index of the inserted table.
        """
        intPtrtable:c_void_p = table.Ptr

        GetDllLibDoc().TableCollection_Insert.argtypes=[c_void_p ,c_int,c_void_p]
        GetDllLibDoc().TableCollection_Insert.restype=c_int
        ret = CallCFunction(GetDllLibDoc().TableCollection_Insert,self.Ptr, index,intPtrtable)
        return ret


    def Remove(self ,table:'ITable'):
        """
        Removes the specified table from the collection.

        Args:
            table: The table to be removed.
        """
        intPtrtable:c_void_p = table.Ptr

        GetDllLibDoc().TableCollection_Remove.argtypes=[c_void_p ,c_void_p]
        CallCFunction(GetDllLibDoc().TableCollection_Remove,self.Ptr, intPtrtable)


    def RemoveAt(self ,index:int):
        """
        Removes the table at the specified index from the collection.

        Args:
            index: The index of the table to be removed.
        """
        
        GetDllLibDoc().TableCollection_RemoveAt.argtypes=[c_void_p ,c_int]
        CallCFunction(GetDllLibDoc().TableCollection_RemoveAt,self.Ptr, index)

