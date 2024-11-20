from enum import Enum
from plum import dispatch
from typing import TypeVar, Union, Generic, List, Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class HeaderFooter (  Body, IDocumentObject) :
    """
    Represents a header or footer in a document.
    """
    @property

    def DocumentObjectType(self)->'DocumentObjectType':
        """
        Gets the type of the document object.
        """
        GetDllLibDoc().HeaderFooter_get_DocumentObjectType.argtypes=[c_void_p]
        GetDllLibDoc().HeaderFooter_get_DocumentObjectType.restype=c_int
        ret = CallCFunction(GetDllLibDoc().HeaderFooter_get_DocumentObjectType,self.Ptr)
        objwraped = DocumentObjectType(ret)
        return objwraped

    @property
    def LinkToPrevious(self) -> bool:
        """
        Gets a value indicating whether the header or footer is linked to the previous section.
        """
        GetDllLibDoc().HeaderFooter_get_LinkToPrevious.argtypes=[c_void_p]
        GetDllLibDoc().HeaderFooter_get_LinkToPrevious.restype=c_bool
        ret = CallCFunction(GetDllLibDoc().HeaderFooter_get_LinkToPrevious,self.Ptr)
        return ret

    @LinkToPrevious.setter
    def LinkToPrevious(self, value:bool):
        """
        Sets a value indicating whether the header or footer is linked to the previous section.
        """
        GetDllLibDoc().HeaderFooter_set_LinkToPrevious.argtypes=[c_void_p, c_bool]
        CallCFunction(GetDllLibDoc().HeaderFooter_set_LinkToPrevious,self.Ptr, value)

