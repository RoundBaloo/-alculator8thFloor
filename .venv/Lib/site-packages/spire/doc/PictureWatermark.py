from enum import Enum
from plum import dispatch
from typing import TypeVar, Union, Generic, List, Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class PictureWatermark (  WatermarkBase) :
    """
    Represents a picture watermark.
    """
    def __init__(self):
        """
        Initializes a new instance of the PictureWatermark class.
        """
        GetDllLibDoc().PictureWatermark_CreatePictureWatermark.restype = c_void_p
        intPtr = CallCFunction(GetDllLibDoc().PictureWatermark_CreatePictureWatermark,)
        super(PictureWatermark, self).__init__(intPtr)


    @property
    def Scaling(self)->float:
        """
        Gets or sets the picture scaling in percents.
        """
        GetDllLibDoc().PictureWatermark_get_Scaling.argtypes=[c_void_p]
        GetDllLibDoc().PictureWatermark_get_Scaling.restype=c_float
        ret = CallCFunction(GetDllLibDoc().PictureWatermark_get_Scaling,self.Ptr)
        return ret

    @Scaling.setter
    def Scaling(self, value:float):
        """
        Sets the picture scaling in percents.
        """
        GetDllLibDoc().PictureWatermark_set_Scaling.argtypes=[c_void_p, c_float]
        CallCFunction(GetDllLibDoc().PictureWatermark_set_Scaling,self.Ptr, value)

    @property
    def IsWashout(self)->bool:
        """
        Gets or sets the washout property for the picture watermark.
        """
        GetDllLibDoc().PictureWatermark_get_IsWashout.argtypes=[c_void_p]
        GetDllLibDoc().PictureWatermark_get_IsWashout.restype=c_bool
        ret = CallCFunction(GetDllLibDoc().PictureWatermark_get_IsWashout,self.Ptr)
        return ret

    @IsWashout.setter
    def IsWashout(self, value:bool):
        """
        Sets the washout property for the picture watermark.
        """
        GetDllLibDoc().PictureWatermark_set_IsWashout.argtypes=[c_void_p, c_bool]
        CallCFunction(GetDllLibDoc().PictureWatermark_set_IsWashout,self.Ptr, value)

    @dispatch

    def SetPicture(self ,ImgFile:str):
        """
        Sets the picture using the image file.
        """
        ImgFilePtr = StrToPtr(ImgFile)
        GetDllLibDoc().PictureWatermark_SetPicture.argtypes=[c_void_p ,c_char_p]
        CallCFunction(GetDllLibDoc().PictureWatermark_SetPicture,self.Ptr, ImgFilePtr)

    @dispatch

    def SetPicture(self ,imgStream:Stream):
        """
        Sets the picture using the image stream.
        """
        intPtrimgStream:c_void_p = imgStream.Ptr

        GetDllLibDoc().PictureWatermark_SetPictureI.argtypes=[c_void_p ,c_void_p]
        CallCFunction(GetDllLibDoc().PictureWatermark_SetPictureI,self.Ptr, intPtrimgStream)

