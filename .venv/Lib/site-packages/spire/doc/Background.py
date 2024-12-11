from enum import Enum
from plum import dispatch
from typing import TypeVar, Union, Generic, List, Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class Background(DocumentSerializable):
    """
    Represents the background for a document.
    """

    @property
    def Type(self) -> 'BackgroundType':
        """
        Gets or sets the type of background for the document.
        """
        GetDllLibDoc().Background_get_Type.argtypes=[c_void_p]
        GetDllLibDoc().Background_get_Type.restype=c_int
        ret = CallCFunction(GetDllLibDoc().Background_get_Type,self.Ptr)
        objwraped = BackgroundType(ret)
        return objwraped

    @Type.setter
    def Type(self, value:'BackgroundType'):
        GetDllLibDoc().Background_set_Type.argtypes=[c_void_p, c_int]
        CallCFunction(GetDllLibDoc().Background_set_Type,self.Ptr, value.value)

    @property
    def Color(self) -> 'Color':
        """
        Gets or sets the background color.
        """
        GetDllLibDoc().Background_get_Color.argtypes=[c_void_p]
        GetDllLibDoc().Background_get_Color.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().Background_get_Color,self.Ptr)
        ret = None if intPtr==None else Color(intPtr)
        return ret

    @Color.setter
    def Color(self, value:'Color'):
        GetDllLibDoc().Background_set_Color.argtypes=[c_void_p, c_void_p]
        CallCFunction(GetDllLibDoc().Background_set_Color,self.Ptr, value.Ptr)

    @property
    def Gradient(self) -> 'BackgroundGradient':
        """
        Gets or sets the background gradient.
        """
        GetDllLibDoc().Background_get_Gradient.argtypes=[c_void_p]
        GetDllLibDoc().Background_get_Gradient.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().Background_get_Gradient,self.Ptr)
        from spire.doc import BackgroundGradient
        ret = None if intPtr==None else BackgroundGradient(intPtr)
        return ret

    def GetDirectShapeAttribute(self, key: int) -> 'SpireObject':
        """
        Gets the direct shape attribute with the specified key.
        """
        
        GetDllLibDoc().Background_GetDirectShapeAttribute.argtypes=[c_void_p ,c_int]
        GetDllLibDoc().Background_GetDirectShapeAttribute.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().Background_GetDirectShapeAttribute,self.Ptr, key)
        ret = None if intPtr==None else SpireObject(intPtr)
        return ret

    def GetInheritedShapeAttribute(self, key: int) -> 'SpireObject':
        """
        Gets the inherited shape attribute with the specified key.
        """
        
        GetDllLibDoc().Background_GetInheritedShapeAttribute.argtypes=[c_void_p ,c_int]
        GetDllLibDoc().Background_GetInheritedShapeAttribute.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().Background_GetInheritedShapeAttribute,self.Ptr, key)
        ret = None if intPtr==None else SpireObject(intPtr)
        return ret

    def GetShapeAttribute(self, key: int) -> 'SpireObject':
        """
        Gets the shape attribute with the specified key.
        """
        
        GetDllLibDoc().Background_GetShapeAttribute.argtypes=[c_void_p ,c_int]
        GetDllLibDoc().Background_GetShapeAttribute.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().Background_GetShapeAttribute,self.Ptr, key)
        ret = None if intPtr==None else SpireObject(intPtr)
        return ret

    def SetShapeAttribute(self, key: int, value: 'SpireObject'):
        """
        Sets the shape attribute with the specified key and value.
        """
        intPtrvalue:c_void_p = value.Ptr

        GetDllLibDoc().Background_SetShapeAttribute.argtypes=[c_void_p ,c_int,c_void_p]
        CallCFunction(GetDllLibDoc().Background_SetShapeAttribute,self.Ptr, key,intPtrvalue)

    def SetShapeAttr(self, key: int, value: 'SpireObject'):
        """
        Sets the shape attribute with the specified key and value.
        """
        intPtrvalue:c_void_p = value.Ptr

        GetDllLibDoc().Background_SetShapeAttr.argtypes=[c_void_p ,c_int,c_void_p]
        CallCFunction(GetDllLibDoc().Background_SetShapeAttr,self.Ptr, key,intPtrvalue)

    def RemoveShapeAttribute(self, key: int):
        """
        Removes the shape attribute with the specified key.
        """
        
        GetDllLibDoc().Background_RemoveShapeAttribute.argtypes=[c_void_p ,c_int]
        CallCFunction(GetDllLibDoc().Background_RemoveShapeAttribute,self.Ptr, key)

    def HasKey(self, key: int) -> bool:
        """
        Checks if the background has the specified key.
        """
        
        GetDllLibDoc().Background_HasKey.argtypes=[c_void_p ,c_int]
        GetDllLibDoc().Background_HasKey.restype=c_bool
        ret = CallCFunction(GetDllLibDoc().Background_HasKey,self.Ptr, key)
        return ret

    @dispatch
    def SetPicture(self, imgFile: str):
        """
        Sets the picture using the specified image file.
        """
        imgFilePtr = StrToPtr(imgFile)
        GetDllLibDoc().Background_SetPicture.argtypes=[c_void_p ,c_char_p]
        CallCFunction(GetDllLibDoc().Background_SetPicture,self.Ptr, imgFilePtr)

    @dispatch
    def SetPicture(self, imgStream: Stream):
        """
        Sets the picture using the specified image stream.
        """
        intPtrimgStream:c_void_p = imgStream.Ptr

        GetDllLibDoc().Background_SetPictureI.argtypes=[c_void_p ,c_void_p]
        CallCFunction(GetDllLibDoc().Background_SetPictureI,self.Ptr, intPtrimgStream)

