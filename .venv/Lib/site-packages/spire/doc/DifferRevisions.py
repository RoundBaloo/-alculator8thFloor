from enum import Enum
from plum import dispatch
from typing import TypeVar, Union, Generic, List, Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class DifferRevisions(SpireObject):
    """
    Class for different revisions.
    """
    def __init__(self, doc:'Document'):
        """
        Initializes a new instance of the DifferRevisions.

        Args:
            document (Document): The document.
        Returns:
            None
        """
        intPdoc:c_void_p = doc.Ptr

        GetDllLibDoc().DifferRevisions_CreateDifferRevisionsD.argtypes=[c_void_p]
        GetDllLibDoc().DifferRevisions_CreateDifferRevisionsD.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().DifferRevisions_CreateDifferRevisionsD,intPdoc)
        super(DifferRevisions, self).__init__(intPtr)
    def Dispose(self):
        """
        Dispose the object.
        """
        GetDllLibDoc().DifferRevisions_Dispose.argtypes=[c_void_p]
        CallCFunction(GetDllLibDoc().DifferRevisions_Dispose,self.Ptr)

    @property

    def DeleteRevisions(self)->List['DocumentObject']:
        """
        Gets the delete revisions.
        """
        GetDllLibDoc().DifferRevisions_get_DeleteRevisions.argtypes=[c_void_p]
        GetDllLibDoc().DifferRevisions_get_DeleteRevisions.restype=IntPtrArray
        intPtrArray = CallCFunction(GetDllLibDoc().DifferRevisions_get_DeleteRevisions,self.Ptr)
        ret = GetObjVectorFromArray(intPtrArray,DocumentObject)
        return ret



    @property

    def InsertRevisions(self)->List['DocumentObject']:
        """
        Gets the insert revisions.
        """
        GetDllLibDoc().DifferRevisions_get_InsertRevisions.argtypes=[c_void_p]
        GetDllLibDoc().DifferRevisions_get_InsertRevisions.restype=IntPtrArray
        intPtrArray = CallCFunction(GetDllLibDoc().DifferRevisions_get_InsertRevisions,self.Ptr)
        ret = GetObjVectorFromArray(intPtrArray,DocumentObject)
        return ret



