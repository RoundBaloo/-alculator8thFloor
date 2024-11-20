from enum import Enum
from plum import dispatch
from typing import TypeVar, Union, Generic, List, Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class CustomXmlPart(SpireObject):
    """
    Represents a custom XML part.
    """
    @property

    def Id(self)->str:
        """
        Gets or sets the ID of the custom XML part.
        """
        GetDllLibDoc().CustomXmlPart_get_Id.argtypes=[c_void_p]
        GetDllLibDoc().CustomXmlPart_get_Id.restype=c_void_p
        ret = PtrToStr(CallCFunction(GetDllLibDoc().CustomXmlPart_get_Id,self.Ptr))
        return ret


    @Id.setter
    def Id(self, value:str):
        """
        Sets the ID of the custom XML part.
        """
        valuePtr = StrToPtr(value)
        GetDllLibDoc().CustomXmlPart_set_Id.argtypes=[c_void_p, c_char_p]
        CallCFunction(GetDllLibDoc().CustomXmlPart_set_Id,self.Ptr, valuePtr)

#    @property
#
#    def Data(self)->List['Byte']:
#        """
#
#        """
#        GetDllLibDoc().CustomXmlPart_get_Data.argtypes=[c_void_p]
#        GetDllLibDoc().CustomXmlPart_get_Data.restype=IntPtrArray
#        intPtrArray = GetDllLibDoc().CustomXmlPart_get_Data(self.Ptr)
#        ret = GetVectorFromArray(intPtrArray, Byte)
#        return ret


#    @Data.setter
#    def Data(self, value:List['Byte']):
#        vCount = len(value)
#        ArrayType = c_void_p * vCount
#        vArray = ArrayType()
#        for i in range(0, vCount):
#            vArray[i] = value[i].Ptr
#        GetDllLibDoc().CustomXmlPart_set_Data.argtypes=[c_void_p, ArrayType, c_int]
#        GetDllLibDoc().CustomXmlPart_set_Data(self.Ptr, vArray, vCount)



    def Clone(self)->'CustomXmlPart':
        """
        Creates a deep copy of the custom XML part.
        """
        GetDllLibDoc().CustomXmlPart_Clone.argtypes=[c_void_p]
        GetDllLibDoc().CustomXmlPart_Clone.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().CustomXmlPart_Clone,self.Ptr)
        ret = None if intPtr==None else CustomXmlPart(intPtr)
        return ret


