from enum import Enum
from plum import dispatch
from typing import TypeVar, Union, Generic, List, Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class ShapeGroup (  ShapeBase, IDocumentObject) :
    """
    Represents a group of shapes in a document.
    """
    @property

    def DocumentObjectType(self)->'DocumentObjectType':
        """
        Gets the document object type of the shape group.
        """
        GetDllLibDoc().ShapeGroup_get_DocumentObjectType.argtypes=[c_void_p]
        GetDllLibDoc().ShapeGroup_get_DocumentObjectType.restype=c_int
        ret = CallCFunction(GetDllLibDoc().ShapeGroup_get_DocumentObjectType,self.Ptr)
        objwraped = DocumentObjectType(ret)
        return objwraped

