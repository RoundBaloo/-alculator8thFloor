from enum import Enum
from plum import dispatch
from typing import TypeVar,Union,Generic,List,Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class TextBox (  ShapeObject, ITextBox, ICompositeObject) :
    """
    Represents a text box in a document.
    """
    @dispatch
    def __init__(self, doc:IDocument):
        """
        Initializes a new instance of the TextBox class.

        Args:
            doc (IDocument): The document to which the text box belongs.
        """
        intPdoc:c_void_p =  doc.Ptr

        GetDllLibDoc().TextBox_CreateTextBoxD.argtypes=[c_void_p]
        GetDllLibDoc().TextBox_CreateTextBoxD.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().TextBox_CreateTextBoxD,intPdoc)
        super(TextBox, self).__init__(intPtr)

    @property

    def ChildObjects(self)->'DocumentObjectCollection':
        """
        Gets the child entities.

        Returns:
            DocumentObjectCollection: The child entities.
        """
        GetDllLibDoc().TextBox_get_ChildObjects.argtypes=[c_void_p]
        GetDllLibDoc().TextBox_get_ChildObjects.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().TextBox_get_ChildObjects,self.Ptr)
        ret = None if intPtr==None else DocumentObjectCollection(intPtr)
        return ret


    @property

    def DocumentObjectType(self)->'DocumentObjectType':
        """
        Gets the type of the document object.

        Returns:
            DocumentObjectType: The type of the document object.
        """
        GetDllLibDoc().TextBox_get_DocumentObjectType.argtypes=[c_void_p]
        GetDllLibDoc().TextBox_get_DocumentObjectType.restype=c_int
        ret = CallCFunction(GetDllLibDoc().TextBox_get_DocumentObjectType,self.Ptr)
        objwraped = DocumentObjectType(ret)
        return objwraped

    @property

    def Format(self)->'TextBoxFormat':
        """
        Gets the format value.

        Returns:
            TextBoxFormat: The format value.
        """
        GetDllLibDoc().TextBox_get_Format.argtypes=[c_void_p]
        GetDllLibDoc().TextBox_get_Format.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().TextBox_get_Format,self.Ptr)
        from spire.doc import TextBoxFormat
        ret = None if intPtr==None else TextBoxFormat(intPtr)
        return ret


    @property

    def Body(self)->'Body':
        """
        Gets or sets the text body value.

        Returns:
            Body: The text body value.
        """
        GetDllLibDoc().TextBox_get_Body.argtypes=[c_void_p]
        GetDllLibDoc().TextBox_get_Body.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().TextBox_get_Body,self.Ptr)
        ret = None if intPtr==None else Body(intPtr)
        return ret


    @property

    def CharacterFormat(self)->'CharacterFormat':
        """
        Gets the character format.

        Returns:
            CharacterFormat: The character format.
        """
        GetDllLibDoc().TextBox_get_CharacterFormat.argtypes=[c_void_p]
        GetDllLibDoc().TextBox_get_CharacterFormat.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().TextBox_get_CharacterFormat,self.Ptr)
        ret = None if intPtr==None else CharacterFormat(intPtr)
        return ret


