from enum import Enum
from plum import dispatch
from typing import TypeVar, Union, Generic, List, Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class Hyperlink (SpireObject) :
    """
    Represents a hyperlink in a document.
    """
    @property
    def FilePath(self) -> str:
        """
        Gets or sets the file path of the hyperlink.
        """
        GetDllLibDoc().Hyperlink_get_FilePath.argtypes=[c_void_p]
        GetDllLibDoc().Hyperlink_get_FilePath.restype=c_void_p
        ret = PtrToStr(CallCFunction(GetDllLibDoc().Hyperlink_get_FilePath,self.Ptr))
        return ret


    @FilePath.setter
    def FilePath(self, value:str):
        """
        Sets the file path of the hyperlink.
        """
        valuePtr = StrToPtr(value)
        GetDllLibDoc().Hyperlink_set_FilePath.argtypes=[c_void_p, c_char_p]
        CallCFunction(GetDllLibDoc().Hyperlink_set_FilePath,self.Ptr, valuePtr)

    @property

    def Uri(self)->str:
        """
        Gets or sets the URL link of the hyperlink.
        """
        GetDllLibDoc().Hyperlink_get_Uri.argtypes=[c_void_p]
        GetDllLibDoc().Hyperlink_get_Uri.restype=c_void_p
        ret = PtrToStr(CallCFunction(GetDllLibDoc().Hyperlink_get_Uri,self.Ptr))
        return ret


    @Uri.setter
    def Uri(self, value:str):
        """
        Sets the URL link of the hyperlink.
        """
        valuePtr = StrToPtr(value)
        GetDllLibDoc().Hyperlink_set_Uri.argtypes=[c_void_p, c_char_p]
        CallCFunction(GetDllLibDoc().Hyperlink_set_Uri,self.Ptr, valuePtr)

    @property

    def BookmarkName(self)->str:
        """
        Gets or sets the bookmark of the hyperlink.
        """
        GetDllLibDoc().Hyperlink_get_BookmarkName.argtypes=[c_void_p]
        GetDllLibDoc().Hyperlink_get_BookmarkName.restype=c_void_p
        ret = PtrToStr(CallCFunction(GetDllLibDoc().Hyperlink_get_BookmarkName,self.Ptr))
        return ret


    @BookmarkName.setter
    def BookmarkName(self, value:str):
        """
        Sets the bookmark of the hyperlink.
        """
        valuePtr = StrToPtr(value)
        GetDllLibDoc().Hyperlink_set_BookmarkName.argtypes=[c_void_p, c_char_p]
        CallCFunction(GetDllLibDoc().Hyperlink_set_BookmarkName,self.Ptr, valuePtr)

    @property

    def Type(self)->'HyperlinkType':
        """
        Gets or sets the type of the hyperlink.
        """
        GetDllLibDoc().Hyperlink_get_Type.argtypes=[c_void_p]
        GetDllLibDoc().Hyperlink_get_Type.restype=c_int
        ret = CallCFunction(GetDllLibDoc().Hyperlink_get_Type,self.Ptr)
        objwraped = HyperlinkType(ret)
        return objwraped

    @Type.setter
    def Type(self, value:'HyperlinkType'):
        """
        Sets the type of the hyperlink.
        """
        GetDllLibDoc().Hyperlink_set_Type.argtypes=[c_void_p, c_int]
        CallCFunction(GetDllLibDoc().Hyperlink_set_Type,self.Ptr, value.value)

    @property

    def TextToDisplay(self)->str:
        """
        Gets or sets the visible text of the hyperlink in a document.
        """
        GetDllLibDoc().Hyperlink_get_TextToDisplay.argtypes=[c_void_p]
        GetDllLibDoc().Hyperlink_get_TextToDisplay.restype=c_void_p
        ret = PtrToStr(CallCFunction(GetDllLibDoc().Hyperlink_get_TextToDisplay,self.Ptr))
        return ret


    @TextToDisplay.setter
    def TextToDisplay(self, value:str):
        """
        Sets the visible text of the hyperlink in a document.
        """
        valuePtr = StrToPtr(value)
        GetDllLibDoc().Hyperlink_set_TextToDisplay.argtypes=[c_void_p, c_char_p]
        CallCFunction(GetDllLibDoc().Hyperlink_set_TextToDisplay,self.Ptr, valuePtr)

    @property

    def PictureToDisplay(self)->'ShapeObject':
        """
        Gets or sets the image that will be displayed in place of the hyperlink.
        """
        GetDllLibDoc().Hyperlink_get_PictureToDisplay.argtypes=[c_void_p]
        GetDllLibDoc().Hyperlink_get_PictureToDisplay.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().Hyperlink_get_PictureToDisplay,self.Ptr)
        ret = None if intPtr==None else ShapeObject(intPtr)
        return ret


    @PictureToDisplay.setter
    def PictureToDisplay(self, value:'ShapeObject'):
        """
        Sets the image that will be displayed in place of the hyperlink.
        """
        GetDllLibDoc().Hyperlink_set_PictureToDisplay.argtypes=[c_void_p, c_void_p]
        CallCFunction(GetDllLibDoc().Hyperlink_set_PictureToDisplay,self.Ptr, value.Ptr)

    def Dispose(self):
        """
        Disposes the hyperlink object.
        """
        GetDllLibDoc().Hyperlink_Dispose.argtypes=[c_void_p]
        CallCFunction(GetDllLibDoc().Hyperlink_Dispose,self.Ptr)

