from enum import Enum
from plum import dispatch
from typing import TypeVar, Union, Generic, List, Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class BuiltinDocumentProperties (  SummaryDocumentProperties) :
    """
    Class representing the built-in document properties.
    """
    @property

    def Category(self)->str:
        """
        Gets or sets the category of the document.
        """
        GetDllLibDoc().BuiltinDocumentProperties_get_Category.argtypes=[c_void_p]
        GetDllLibDoc().BuiltinDocumentProperties_get_Category.restype=c_void_p
        ret = PtrToStr(CallCFunction(GetDllLibDoc().BuiltinDocumentProperties_get_Category,self.Ptr))
        return ret


    @Category.setter
    def Category(self, value:str):
        valuePtr = StrToPtr(value)
        GetDllLibDoc().BuiltinDocumentProperties_set_Category.argtypes=[c_void_p, c_char_p]
        CallCFunction(GetDllLibDoc().BuiltinDocumentProperties_set_Category,self.Ptr, valuePtr)

    @property
    def BytesCount(self)->int:
        """
        Gets the number of bytes in the document.
        """
        GetDllLibDoc().BuiltinDocumentProperties_get_BytesCount.argtypes=[c_void_p]
        GetDllLibDoc().BuiltinDocumentProperties_get_BytesCount.restype=c_int
        ret = CallCFunction(GetDllLibDoc().BuiltinDocumentProperties_get_BytesCount,self.Ptr)
        return ret

    @property
    def LinesCount(self)->int:
        """
        Gets the number of lines in the document.
        """
        GetDllLibDoc().BuiltinDocumentProperties_get_LinesCount.argtypes=[c_void_p]
        GetDllLibDoc().BuiltinDocumentProperties_get_LinesCount.restype=c_int
        ret = CallCFunction(GetDllLibDoc().BuiltinDocumentProperties_get_LinesCount,self.Ptr)
        return ret

    @property
    def ParagraphCount(self)->int:
        """
        Gets the number of paragraphs in the document.
        """
        GetDllLibDoc().BuiltinDocumentProperties_get_ParagraphCount.argtypes=[c_void_p]
        GetDllLibDoc().BuiltinDocumentProperties_get_ParagraphCount.restype=c_int
        ret = CallCFunction(GetDllLibDoc().BuiltinDocumentProperties_get_ParagraphCount,self.Ptr)
        return ret

    @property
    def CharCountWithSpace(self)->int:
        """
        Gets the document characters count (including spaces).
        """
        GetDllLibDoc().BuiltinDocumentProperties_get_CharCountWithSpace.argtypes=[c_void_p]
        GetDllLibDoc().BuiltinDocumentProperties_get_CharCountWithSpace.restype=c_int
        ret = CallCFunction(GetDllLibDoc().BuiltinDocumentProperties_get_CharCountWithSpace,self.Ptr)
        return ret

    @property
    def SlideCount(self)->int:
        """
        Gets the slide count.
        """
        GetDllLibDoc().BuiltinDocumentProperties_get_SlideCount.argtypes=[c_void_p]
        GetDllLibDoc().BuiltinDocumentProperties_get_SlideCount.restype=c_int
        ret = CallCFunction(GetDllLibDoc().BuiltinDocumentProperties_get_SlideCount,self.Ptr)
        return ret

    @property
    def NoteCount(self)->int:
        """
        Gets the note count.
        """
        GetDllLibDoc().BuiltinDocumentProperties_get_NoteCount.argtypes=[c_void_p]
        GetDllLibDoc().BuiltinDocumentProperties_get_NoteCount.restype=c_int
        ret = CallCFunction(GetDllLibDoc().BuiltinDocumentProperties_get_NoteCount,self.Ptr)
        return ret

    @property
    def HiddenCount(self)->int:
        """
        Gets the hidden count.
        """
        GetDllLibDoc().BuiltinDocumentProperties_get_HiddenCount.argtypes=[c_void_p]
        GetDllLibDoc().BuiltinDocumentProperties_get_HiddenCount.restype=c_int
        ret = CallCFunction(GetDllLibDoc().BuiltinDocumentProperties_get_HiddenCount,self.Ptr)
        return ret

    @property

    def Company(self)->str:
        """
        Gets or sets the company property.
        """
        GetDllLibDoc().BuiltinDocumentProperties_get_Company.argtypes=[c_void_p]
        GetDllLibDoc().BuiltinDocumentProperties_get_Company.restype=c_void_p
        ret = PtrToStr(CallCFunction(GetDllLibDoc().BuiltinDocumentProperties_get_Company,self.Ptr))
        return ret


    @Company.setter
    def Company(self, value:str):
        valuePtr = StrToPtr(value)
        GetDllLibDoc().BuiltinDocumentProperties_set_Company.argtypes=[c_void_p, c_char_p]
        CallCFunction(GetDllLibDoc().BuiltinDocumentProperties_set_Company,self.Ptr, valuePtr)

    @property

    def HyperLinkBase(self)->str:
        """
        Gets or sets the HyperLinkBase property.
        """
        GetDllLibDoc().BuiltinDocumentProperties_get_HyperLinkBase.argtypes=[c_void_p]
        GetDllLibDoc().BuiltinDocumentProperties_get_HyperLinkBase.restype=c_void_p
        ret = PtrToStr(CallCFunction(GetDllLibDoc().BuiltinDocumentProperties_get_HyperLinkBase,self.Ptr))
        return ret


    @HyperLinkBase.setter
    def HyperLinkBase(self, value:str):
        valuePtr = StrToPtr(value)
        GetDllLibDoc().BuiltinDocumentProperties_set_HyperLinkBase.argtypes=[c_void_p, c_char_p]
        CallCFunction(GetDllLibDoc().BuiltinDocumentProperties_set_HyperLinkBase,self.Ptr, valuePtr)

    @property

    def Manager(self)->str:
        """
        Gets or sets the Manager property.
        """
        GetDllLibDoc().BuiltinDocumentProperties_get_Manager.argtypes=[c_void_p]
        GetDllLibDoc().BuiltinDocumentProperties_get_Manager.restype=c_void_p
        ret = PtrToStr(CallCFunction(GetDllLibDoc().BuiltinDocumentProperties_get_Manager,self.Ptr))
        return ret


    @Manager.setter
    def Manager(self, value:str):
        valuePtr = StrToPtr(value)
        GetDllLibDoc().BuiltinDocumentProperties_set_Manager.argtypes=[c_void_p, c_char_p]
        CallCFunction(GetDllLibDoc().BuiltinDocumentProperties_set_Manager,self.Ptr, valuePtr)

    @property

    def ContentStatus(self)->str:
        """
        Gets or sets the document status.
        """
        GetDllLibDoc().BuiltinDocumentProperties_get_ContentStatus.argtypes=[c_void_p]
        GetDllLibDoc().BuiltinDocumentProperties_get_ContentStatus.restype=c_void_p
        ret = PtrToStr(CallCFunction(GetDllLibDoc().BuiltinDocumentProperties_get_ContentStatus,self.Ptr))
        return ret


    @ContentStatus.setter
    def ContentStatus(self, value:str):
        valuePtr = StrToPtr(value)
        GetDllLibDoc().BuiltinDocumentProperties_set_ContentStatus.argtypes=[c_void_p, c_char_p]
        CallCFunction(GetDllLibDoc().BuiltinDocumentProperties_set_ContentStatus,self.Ptr, valuePtr)


    def Clone(self)->'BuiltinDocumentProperties':
        """
        Clones the BuiltinDocumentProperties object.
        """
        GetDllLibDoc().BuiltinDocumentProperties_Clone.argtypes=[c_void_p]
        GetDllLibDoc().BuiltinDocumentProperties_Clone.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().BuiltinDocumentProperties_Clone,self.Ptr)
        ret = None if intPtr==None else BuiltinDocumentProperties(intPtr)
        return ret
