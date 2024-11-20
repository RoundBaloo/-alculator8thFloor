from enum import Enum
from plum import dispatch
from typing import TypeVar, Union, Generic, List, Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class DropDownFormField (  FormField, IDocumentObject) :
    """
    Represents a drop-down form field in a document.
    """
    @dispatch
    def __init__(self, doc:IDocument):
        intPdoc:c_void_p = doc.Ptr

        GetDllLibDoc().DropDownFormField_CreateDropDownFormFieldD.argtypes=[c_void_p]
        GetDllLibDoc().DropDownFormField_CreateDropDownFormFieldD.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().DropDownFormField_CreateDropDownFormFieldD,intPdoc)
        super(DropDownFormField, self).__init__(intPtr)
    @property

    def DocumentObjectType(self)->'DocumentObjectType':
        """
        Gets the type of the document object.
        
        Returns:
            The type of the document object.
        """
        GetDllLibDoc().DropDownFormField_get_DocumentObjectType.argtypes=[c_void_p]
        GetDllLibDoc().DropDownFormField_get_DocumentObjectType.restype=c_int
        ret = CallCFunction(GetDllLibDoc().DropDownFormField_get_DocumentObjectType,self.Ptr)
        objwraped = DocumentObjectType(ret)
        return objwraped

    @property
    def DropDownSelectedIndex(self)->int:
        """
        Gets or sets the selected drop-down index.
        
        Returns:
            The selected drop-down index.
        """
        GetDllLibDoc().DropDownFormField_get_DropDownSelectedIndex.argtypes=[c_void_p]
        GetDllLibDoc().DropDownFormField_get_DropDownSelectedIndex.restype=c_int
        ret = CallCFunction(GetDllLibDoc().DropDownFormField_get_DropDownSelectedIndex,self.Ptr)
        return ret

    @DropDownSelectedIndex.setter
    def DropDownSelectedIndex(self, value:int):
        """
        Sets the selected drop-down index.
        
        Args:
            value: The selected drop-down index.
        """
        GetDllLibDoc().DropDownFormField_set_DropDownSelectedIndex.argtypes=[c_void_p, c_int]
        CallCFunction(GetDllLibDoc().DropDownFormField_set_DropDownSelectedIndex,self.Ptr, value)

    @property

    def DropDownItems(self)->'DropDownCollection':
        """
        Gets the drop-down items.
        
        Returns:
            The drop-down items.
        """
        GetDllLibDoc().DropDownFormField_get_DropDownItems.argtypes=[c_void_p]
        GetDllLibDoc().DropDownFormField_get_DropDownItems.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().DropDownFormField_get_DropDownItems,self.Ptr)
        ret = None if intPtr==None else DropDownCollection(intPtr)
        return ret
