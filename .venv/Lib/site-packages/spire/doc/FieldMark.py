from enum import Enum
from plum import dispatch
from typing import TypeVar, Union, Generic, List, Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class FieldMark (  ParagraphBase, IDocumentObject) :
    """
    Represents a field mark in a document.
    """
    @dispatch
    def __init__(self,doc:IDocument,fieldMarkType:FieldMarkType):
        """
        Initializes a new instance of the FieldMark class.

        Args:
            doc (IDocument): The document that contains the field mark.
            fieldMarkType (FieldMarkType): The type of the field mark.
        """
        intPdoc:c_void_p =  doc.Ptr
        iTypetype:c_int = fieldMarkType.value

        GetDllLibDoc().FieldMark_CreateFieldMarkDT.argtypes=[c_void_p,c_int]
        GetDllLibDoc().FieldMark_CreateFieldMarkDT.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().FieldMark_CreateFieldMarkDT,intPdoc,iTypetype)
        super(FieldMark, self).__init__(intPtr)

    @property

    def DocumentObjectType(self)->'DocumentObjectType':
        """
        Gets the type of the document object.

        Returns:
            DocumentObjectType: The type of the document object.
        """
        GetDllLibDoc().FieldMark_get_DocumentObjectType.argtypes=[c_void_p]
        GetDllLibDoc().FieldMark_get_DocumentObjectType.restype=c_int
        ret = CallCFunction(GetDllLibDoc().FieldMark_get_DocumentObjectType,self.Ptr)
        objwraped = DocumentObjectType(ret)
        return objwraped

    @property

    def CharacterFormat(self)->'CharacterFormat':
        """
        Gets the character format of the field mark.

        Returns:
            CharacterFormat: The character format of the field mark.
        """
        GetDllLibDoc().FieldMark_get_CharacterFormat.argtypes=[c_void_p]
        GetDllLibDoc().FieldMark_get_CharacterFormat.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().FieldMark_get_CharacterFormat,self.Ptr)
        ret = None if intPtr==None else CharacterFormat(intPtr)
        return ret


    @property

    def Type(self)->'FieldMarkType':
        """
        Gets or sets the type of the field mark.

        Returns:
            FieldMarkType: The type of the field mark.
        """
        GetDllLibDoc().FieldMark_get_Type.argtypes=[c_void_p]
        GetDllLibDoc().FieldMark_get_Type.restype=c_int
        ret = CallCFunction(GetDllLibDoc().FieldMark_get_Type,self.Ptr)
        objwraped = FieldMarkType(ret)
        return objwraped

    @Type.setter
    def Type(self, value:'FieldMarkType'):
        """
        Sets the type of the field mark.

        Args:
            value (FieldMarkType): The type of the field mark.
        """
        GetDllLibDoc().FieldMark_set_Type.argtypes=[c_void_p, c_int]
        CallCFunction(GetDllLibDoc().FieldMark_set_Type,self.Ptr, value.value)

