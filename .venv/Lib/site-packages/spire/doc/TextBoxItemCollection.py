from enum import Enum
from plum import dispatch
from typing import TypeVar,Union,Generic,List,Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class TextBoxItemCollection (  DocumentObjectCollection, ITextBoxItemCollection) :
    """
    Represents a collection of TextBox objects.
    """

    def get_Item(self ,index:int)->'ITextBox':
        """
        Retrieves the TextBox at the specified index.
        
        Args:
            index: The index of the TextBox to retrieve.
        
        Returns:
            The TextBox at the specified index.
        """
        
        GetDllLibDoc().TextBoxItemCollection_get_Item.argtypes=[c_void_p ,c_int]
        GetDllLibDoc().TextBoxItemCollection_get_Item.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().TextBoxItemCollection_get_Item,self.Ptr, index)
        ret = None if intPtr==None else ITextBox(intPtr)
        return ret



    def Add(self ,textBox:'ITextBox')->int:
        """
        Adds a TextBox to the collection.
        
        Args:
            textBox: The TextBox to add.
        
        Returns:
            The index at which the TextBox was added.
        """
        intPtrtextBox:c_void_p = textBox.Ptr

        GetDllLibDoc().TextBoxItemCollection_Add.argtypes=[c_void_p ,c_void_p]
        GetDllLibDoc().TextBoxItemCollection_Add.restype=c_int
        ret = CallCFunction(GetDllLibDoc().TextBoxItemCollection_Add,self.Ptr, intPtrtextBox)
        return ret

