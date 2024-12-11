from enum import Enum
from plum import dispatch
from typing import TypeVar, Union, Generic, List, Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class IfField (  Field) :
    """
    Represents an IfField object.
    """
    @dispatch
    def __init__(self, doc: IDocument):
        """
        Initializes a new instance of the IfField class.

        Args:
            doc (IDocument): The document object.
        """
        intPdoc: c_void_p = doc.Ptr

        GetDllLibDoc().IfField_CreateIfFieldD.argtypes=[c_void_p]
        GetDllLibDoc().IfField_CreateIfFieldD.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().IfField_CreateIfFieldD,intPdoc)
        super(IfField, self).__init__(intPtr)
