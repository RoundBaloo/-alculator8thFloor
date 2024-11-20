from enum import Enum
from plum import dispatch
from typing import TypeVar, Union, Generic, List, Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class TextRange (  ParagraphBase, ITextRange) :
    """
    Represents a text range in a document.
    """
    @dispatch
    def __init__(self, doc:'IDocument'):
        """
        Initializes a new instance of the TextRange class.

        Args:
            doc: The document to which the text range belongs.
        """
        intPdoc:c_void_p = doc.Ptr

        GetDllLibDoc().TextRange_CreateTextRangeD.argtypes=[c_void_p]
        GetDllLibDoc().TextRange_CreateTextRangeD.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().TextRange_CreateTextRangeD,intPdoc)
        super(TextRange, self).__init__(intPtr)

    @property

    def DocumentObjectType(self)->'DocumentObjectType':
        """
        Gets the type of the document object.

        Returns:
            The type of the document object.
        """
        GetDllLibDoc().TextRange_get_DocumentObjectType.argtypes=[c_void_p]
        GetDllLibDoc().TextRange_get_DocumentObjectType.restype=c_int
        ret = CallCFunction(GetDllLibDoc().TextRange_get_DocumentObjectType,self.Ptr)
        objwraped = DocumentObjectType(ret)
        return objwraped

    @property

    def Text(self)->str:
        """
        Gets or sets the text.

        Returns:
            The text.
        """
        GetDllLibDoc().TextRange_get_Text.argtypes=[c_void_p]
        GetDllLibDoc().TextRange_get_Text.restype=c_void_p
        ret = PtrToStr(CallCFunction(GetDllLibDoc().TextRange_get_Text,self.Ptr))
        return ret


    @Text.setter
    def Text(self, value:str):
        """
        Sets the text.

        Args:
            value: The text to set.
        """
        valuePtr = StrToPtr(value)
        GetDllLibDoc().TextRange_set_Text.argtypes=[c_void_p, c_char_p]
        CallCFunction(GetDllLibDoc().TextRange_set_Text,self.Ptr, valuePtr)

    @property

    def CharacterFormat(self)->'CharacterFormat':
        """
        Gets the character format.

        Returns:
            The character format.
        """
        GetDllLibDoc().TextRange_get_CharacterFormat.argtypes=[c_void_p]
        GetDllLibDoc().TextRange_get_CharacterFormat.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().TextRange_get_CharacterFormat,self.Ptr)
        from spire.doc import CharacterFormat
        ret = None if intPtr==None else CharacterFormat(intPtr)
        return ret


