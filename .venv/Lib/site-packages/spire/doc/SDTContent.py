from enum import Enum
from plum import dispatch
from typing import TypeVar, Union, Generic, List, Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class SDTContent (  Body, IDocumentObject) :
    """
    Represents the content of a structured document tag.
    """
    @property

    def DocumentObjectType(self)->'DocumentObjectType':
        """
        Gets the document object type of the SDT content.
        """
        GetDllLibDoc().SDTContent_get_DocumentObjectType.argtypes=[c_void_p]
        GetDllLibDoc().SDTContent_get_DocumentObjectType.restype=c_int
        ret = CallCFunction(GetDllLibDoc().SDTContent_get_DocumentObjectType,self.Ptr)
        objwraped = DocumentObjectType(ret)
        return objwraped

