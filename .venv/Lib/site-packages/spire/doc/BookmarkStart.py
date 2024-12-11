from enum import Enum
from plum import dispatch
from typing import TypeVar, Union, Generic, List, Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class BookmarkStart (  ParagraphBase, IDocumentObject) :
    """
    Represents a bookmark start in a document.
    """
    @property

    def DocumentObjectType(self)->'DocumentObjectType':
        """
        Gets the type of the document object.

        Returns:
            DocumentObjectType: The type of the document object.
        """
        GetDllLibDoc().BookmarkStart_get_DocumentObjectType.argtypes=[c_void_p]
        GetDllLibDoc().BookmarkStart_get_DocumentObjectType.restype=c_int
        ret = CallCFunction(GetDllLibDoc().BookmarkStart_get_DocumentObjectType,self.Ptr)
        objwraped = DocumentObjectType(ret)
        return objwraped

    @property

    def Name(self)->str:
        """
        Gets the bookmark name.

        Returns:
            str: The bookmark name.
        """
        GetDllLibDoc().BookmarkStart_get_Name.argtypes=[c_void_p]
        GetDllLibDoc().BookmarkStart_get_Name.restype=c_void_p
        ret = PtrToStr(CallCFunction(GetDllLibDoc().BookmarkStart_get_Name,self.Ptr))
        return ret
