from enum import Enum
from plum import dispatch
from typing import TypeVar, Union, Generic, List, Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class DocumentContainer(DocumentBase):
    """
    A class representing a document container.
    """
    @property
    def Count(self)->int:
        """
        Gets the count of child objects.

        Returns:
            int: The count of child objects.
        """
        GetDllLibDoc().DocumentContainer_get_Count.argtypes=[c_void_p]
        GetDllLibDoc().DocumentContainer_get_Count.restype=c_int
        ret = CallCFunction(GetDllLibDoc().DocumentContainer_get_Count,self.Ptr)
        return ret


    def GetIndex(self ,entity:'IDocumentObject')->int:
        """
        Gets the index of a document object.

        Args:
            entity (IDocumentObject): The document object.

        Returns:
            int: The index of the document object.
        """
        intPtrentity:c_void_p = entity.Ptr

        GetDllLibDoc().DocumentContainer_GetIndex.argtypes=[c_void_p ,c_void_p]
        GetDllLibDoc().DocumentContainer_GetIndex.restype=c_int
        ret = CallCFunction(GetDllLibDoc().DocumentContainer_GetIndex,self.Ptr, intPtrentity)
        return ret
