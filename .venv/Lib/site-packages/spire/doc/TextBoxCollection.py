from enum import Enum
from plum import dispatch
from typing import TypeVar, Union, Generic, List, Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class TextBoxCollection (  CollectionEx) :
    """
    A collection of text boxes.
    """

    def get_Item(self ,index:int)->'TextBox':
        """
        Gets the textbox at the specified index.

        Args:
            index: The index of the textbox.

        Returns:
            The textbox at the specified index.
        """
        
        GetDllLibDoc().TextBoxCollection_get_Item.argtypes=[c_void_p ,c_int]
        GetDllLibDoc().TextBoxCollection_get_Item.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().TextBoxCollection_get_Item,self.Ptr, index)
        ret = None if intPtr==None else TextBox(intPtr)
        return ret



    def RemoveAt(self ,index:int):
        """
        Removes a textbox at the specified index.

        Args:
            index: The index of the textbox.
        """
        
        GetDllLibDoc().TextBoxCollection_RemoveAt.argtypes=[c_void_p ,c_int]
        CallCFunction(GetDllLibDoc().TextBoxCollection_RemoveAt,self.Ptr, index)

    def Clear(self):
        """
        Removes all textboxes from the document.
        """
        GetDllLibDoc().TextBoxCollection_Clear.argtypes=[c_void_p]
        CallCFunction(GetDllLibDoc().TextBoxCollection_Clear,self.Ptr)

