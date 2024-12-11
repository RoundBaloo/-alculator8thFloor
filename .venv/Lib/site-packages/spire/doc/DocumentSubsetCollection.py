from enum import Enum
from plum import dispatch
from typing import TypeVar, Union, Generic, List, Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class DocumentSubsetCollection(OwnerHolder, IDocumentObjectCollection, ICollectionBase, IEnumerable):
    """
    Represents a subset from collection of specified type entities.
    """
    @property

    def Document(self)->'Document':
        """
        Gets the document.
        """
        GetDllLibDoc().DocumentSubsetCollection_get_Document.argtypes=[c_void_p]
        GetDllLibDoc().DocumentSubsetCollection_get_Document.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().DocumentSubsetCollection_get_Document,self.Ptr)
        ret = None if intPtr==None else Document(intPtr)
        return ret

    @property
    def Owner(self) -> 'DocumentObject':
        """
        Gets the owner.
        """
        GetDllLibDoc().DocumentSubsetCollection_get_Owner.argtypes=[c_void_p]
        GetDllLibDoc().DocumentSubsetCollection_get_Owner.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().DocumentSubsetCollection_get_Owner,self.Ptr)
        ret = None if intPtr==None else DocumentObject(intPtr)
        return ret

    @property
    def Count(self) -> int:
        """
        Gets the count.
        """
        GetDllLibDoc().DocumentSubsetCollection_get_Count.argtypes=[c_void_p]
        GetDllLibDoc().DocumentSubsetCollection_get_Count.restype=c_int
        ret = CallCFunction(GetDllLibDoc().DocumentSubsetCollection_get_Count,self.Ptr)
        return ret


    def get_Item(self ,index:int)->'DocumentObject':
        """
        Gets the documentObject at the specified index.
        """
        
        GetDllLibDoc().DocumentSubsetCollection_get_Item.argtypes=[c_void_p ,c_int]
        GetDllLibDoc().DocumentSubsetCollection_get_Item.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().DocumentSubsetCollection_get_Item,self.Ptr, index)
        ret = None if intPtr==None else DocumentObject(intPtr)
        return ret

    def Clear(self):
        """
        Removes all entities 
        """
        GetDllLibDoc().DocumentSubsetCollection_Clear.argtypes=[c_void_p]
        CallCFunction(GetDllLibDoc().DocumentSubsetCollection_Clear,self.Ptr)


    def GetEnumerator(self)->'IEnumerator':
        """
        Returns an enumerator that iterates through a collection.
        """
        GetDllLibDoc().DocumentSubsetCollection_GetEnumerator.argtypes=[c_void_p]
        GetDllLibDoc().DocumentSubsetCollection_GetEnumerator.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().DocumentSubsetCollection_GetEnumerator,self.Ptr)
        ret = None if intPtr==None else IEnumerator(intPtr)
        return ret
