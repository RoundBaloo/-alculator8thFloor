from enum import Enum
from plum import dispatch
from typing import TypeVar, Union, Generic, List, Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class Symbol (  ParagraphBase, IDocumentObject) :
    """
    Represents a symbol in a document.
    """
    @property

    def DocumentObjectType(self)->'DocumentObjectType':
        """
        Gets the type of the document object.

        Returns:
            DocumentObjectType: The type of the document object.
        """
        GetDllLibDoc().Symbol_get_DocumentObjectType.argtypes=[c_void_p]
        GetDllLibDoc().Symbol_get_DocumentObjectType.restype=c_int
        ret = CallCFunction(GetDllLibDoc().Symbol_get_DocumentObjectType,self.Ptr)
        objwraped = DocumentObjectType(ret)
        return objwraped

    @property

    def CharacterFormat(self)->'CharacterFormat':
        """
        Gets the character format for the symbol.

        Returns:
            CharacterFormat: The character format for the symbol.
        """
        GetDllLibDoc().Symbol_get_CharacterFormat.argtypes=[c_void_p]
        GetDllLibDoc().Symbol_get_CharacterFormat.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().Symbol_get_CharacterFormat,self.Ptr)
        ret = None if intPtr==None else CharacterFormat(intPtr)
        return ret


    @property

    def FontName(self)->str:
        """
        Returns or sets the symbol's font name.

        Returns:
            str: The symbol's font name.
        """
        GetDllLibDoc().Symbol_get_FontName.argtypes=[c_void_p]
        GetDllLibDoc().Symbol_get_FontName.restype=c_void_p
        ret = PtrToStr(CallCFunction(GetDllLibDoc().Symbol_get_FontName,self.Ptr))
        return ret


    @FontName.setter
    def FontName(self, value:str):
        valuePtr = StrToPtr(value)
        GetDllLibDoc().Symbol_set_FontName.argtypes=[c_void_p, c_char_p]
        CallCFunction(GetDllLibDoc().Symbol_set_FontName,self.Ptr, valuePtr)

    @property
    def CharacterCode(self)->int:
        """
        Returns or sets the symbol's character code.

        Returns:
            int: The symbol's character code.
        """
        GetDllLibDoc().Symbol_get_CharacterCode.argtypes=[c_void_p]
        GetDllLibDoc().Symbol_get_CharacterCode.restype=c_int
        ret = CallCFunction(GetDllLibDoc().Symbol_get_CharacterCode,self.Ptr)
        return ret

    @CharacterCode.setter
    def CharacterCode(self, value:int):
        GetDllLibDoc().Symbol_set_CharacterCode.argtypes=[c_void_p, c_int]
        CallCFunction(GetDllLibDoc().Symbol_set_CharacterCode,self.Ptr, value)

