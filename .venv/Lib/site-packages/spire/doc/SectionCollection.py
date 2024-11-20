from enum import Enum
from plum import dispatch
from typing import TypeVar, Union, Generic, List, Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class SectionCollection (  DocumentObjectCollection, IWSectionCollection) :
    """
    A collection of sections in a document.
    """

    def get_Item(self ,index:int)->'Section':
        """
        Retrieves the section at the specified index.
        
        Args:
            index: The index of the section.
        
        Returns:
            The section at the specified index.
        """
        
        GetDllLibDoc().SectionCollection_get_Item.argtypes=[c_void_p ,c_int]
        GetDllLibDoc().SectionCollection_get_Item.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().SectionCollection_get_Item,self.Ptr, index)
        ret = None if intPtr==None else Section(intPtr)
        return ret



    def Add(self ,section:'ISection')->int:
        """
        Adds a section to the end of the document.
        
        Args:
            section: The section to be added.
        
        Returns:
            The index of the added section.
        """
        intPtrsection:c_void_p = section.Ptr

        GetDllLibDoc().SectionCollection_Add.argtypes=[c_void_p ,c_void_p]
        GetDllLibDoc().SectionCollection_Add.restype=c_int
        ret = CallCFunction(GetDllLibDoc().SectionCollection_Add,self.Ptr, intPtrsection)
        return ret


    def IndexOf(self ,section:'ISection')->int:
        """
        Returns the zero-based index of the specified section.
        
        Args:
            section: The section to find the index of.
        
        Returns:
            The index of the specified section.
        """
        intPtrsection:c_void_p = section.Ptr

        GetDllLibDoc().SectionCollection_IndexOf.argtypes=[c_void_p ,c_void_p]
        GetDllLibDoc().SectionCollection_IndexOf.restype=c_int
        ret = CallCFunction(GetDllLibDoc().SectionCollection_IndexOf,self.Ptr, intPtrsection)
        return ret

