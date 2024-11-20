from enum import Enum
from plum import dispatch
from typing import TypeVar, Union, Generic, List, Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class Footnote (  ParagraphBase, ICompositeObject) :
    """
    Represents a footnote in a document.
    """
    @property
    def UseAbsolutePos(self)->bool:
        """
        Gets or sets a value indicating whether the footnote uses absolute position.
        """
        GetDllLibDoc().Footnote_get_UseAbsolutePos.argtypes=[c_void_p]
        GetDllLibDoc().Footnote_get_UseAbsolutePos.restype=c_bool
        ret = CallCFunction(GetDllLibDoc().Footnote_get_UseAbsolutePos,self.Ptr)
        return ret

    @UseAbsolutePos.setter
    def UseAbsolutePos(self, value:bool):
        GetDllLibDoc().Footnote_set_UseAbsolutePos.argtypes=[c_void_p, c_bool]
        CallCFunction(GetDllLibDoc().Footnote_set_UseAbsolutePos,self.Ptr, value)

    @property
    def DocumentObjectType(self) -> 'DocumentObjectType':
        """
        Gets the type of the document object.
        """
        GetDllLibDoc().Footnote_get_DocumentObjectType.argtypes=[c_void_p]
        GetDllLibDoc().Footnote_get_DocumentObjectType.restype=c_int
        ret = CallCFunction(GetDllLibDoc().Footnote_get_DocumentObjectType,self.Ptr)
        objwraped = DocumentObjectType(ret)
        return objwraped

    @property
    def FootnoteType(self) -> 'FootnoteType':
        """
        Gets or sets the type of the footnote: footnote or endnote.
        """
        GetDllLibDoc().Footnote_get_FootnoteType.argtypes=[c_void_p]
        GetDllLibDoc().Footnote_get_FootnoteType.restype=c_int
        ret = CallCFunction(GetDllLibDoc().Footnote_get_FootnoteType,self.Ptr)
        objwraped = FootnoteType(ret)
        return objwraped

    @FootnoteType.setter
    def FootnoteType(self, value:'FootnoteType'):
        GetDllLibDoc().Footnote_set_FootnoteType.argtypes=[c_void_p, c_int]
        CallCFunction(GetDllLibDoc().Footnote_set_FootnoteType,self.Ptr, value.value)

    @property
    def IsAutoNumbered(self) -> bool:
        """
        Gets or sets a value indicating whether the footnote is auto numbered.
        """
        GetDllLibDoc().Footnote_get_IsAutoNumbered.argtypes=[c_void_p]
        GetDllLibDoc().Footnote_get_IsAutoNumbered.restype=c_bool
        ret = CallCFunction(GetDllLibDoc().Footnote_get_IsAutoNumbered,self.Ptr)
        return ret

    @IsAutoNumbered.setter
    def IsAutoNumbered(self, value:bool):
        GetDllLibDoc().Footnote_set_IsAutoNumbered.argtypes=[c_void_p, c_bool]
        CallCFunction(GetDllLibDoc().Footnote_set_IsAutoNumbered,self.Ptr, value)

    @property
    def TextBody(self) -> 'Body':
        """
        Gets the text body of the footnote.
        """
        GetDllLibDoc().Footnote_get_TextBody.argtypes=[c_void_p]
        GetDllLibDoc().Footnote_get_TextBody.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().Footnote_get_TextBody,self.Ptr)
        ret = None if intPtr==None else Body(intPtr)
        return ret

    @property
    def MarkerCharacterFormat(self) -> 'CharacterFormat':
        """
        Gets the marker character format.
        """
        GetDllLibDoc().Footnote_get_MarkerCharacterFormat.argtypes=[c_void_p]
        GetDllLibDoc().Footnote_get_MarkerCharacterFormat.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().Footnote_get_MarkerCharacterFormat,self.Ptr)
        ret = None if intPtr==None else CharacterFormat(intPtr)
        return ret


    @property
    def SymbolCode(self)->int:
        """
        Gets the marker symbol code.
        """
        GetDllLibDoc().Footnote_get_SymbolCode.argtypes=[c_void_p]
        GetDllLibDoc().Footnote_get_SymbolCode.restype=c_int
        ret = CallCFunction(GetDllLibDoc().Footnote_get_SymbolCode,self.Ptr)
        return ret

    @SymbolCode.setter
    def SymbolCode(self, value:int):
        GetDllLibDoc().Footnote_set_SymbolCode.argtypes=[c_void_p, c_int]
        CallCFunction(GetDllLibDoc().Footnote_set_SymbolCode,self.Ptr, value)

    @property
    def CustomMarker(self) -> str:
        """
        Gets the custom footnote marker.
        """
        GetDllLibDoc().Footnote_get_CustomMarker.argtypes=[c_void_p]
        GetDllLibDoc().Footnote_get_CustomMarker.restype=c_void_p
        ret = PtrToStr(CallCFunction(GetDllLibDoc().Footnote_get_CustomMarker,self.Ptr))
        return ret


    @CustomMarker.setter
    def CustomMarker(self, value:str):
        valuePtr = StrToPtr(value)
        GetDllLibDoc().Footnote_set_CustomMarker.argtypes=[c_void_p, c_char_p]
        CallCFunction(GetDllLibDoc().Footnote_set_CustomMarker,self.Ptr, valuePtr)

    @property

    def ChildObjects(self)->'DocumentObjectCollection':
        """
        Gets the child objects of the footnote.
        """
        GetDllLibDoc().Footnote_get_ChildObjects.argtypes=[c_void_p]
        GetDllLibDoc().Footnote_get_ChildObjects.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().Footnote_get_ChildObjects,self.Ptr)
        ret = None if intPtr==None else DocumentObjectCollection(intPtr)
        return ret


    def EnsureMinimum(self):
        """
        Ensures that the footnote has the minimum required elements.
        """
        GetDllLibDoc().Footnote_EnsureMinimum.argtypes=[c_void_p]
        CallCFunction(GetDllLibDoc().Footnote_EnsureMinimum,self.Ptr)

