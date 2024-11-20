from enum import Enum
from plum import dispatch
from typing import TypeVar, Union, Generic, List, Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class ClipboardData(SpireObject):
    """
    Represents clipboard data.
    """
    @property
    def Format(self)->int:
        """
        Gets or sets the clipboard format.
        """
        GetDllLibDoc().ClipboardData_get_Format.argtypes=[c_void_p]
        GetDllLibDoc().ClipboardData_get_Format.restype=c_int
        ret = CallCFunction(GetDllLibDoc().ClipboardData_get_Format,self.Ptr)
        return ret

    @Format.setter
    def Format(self, value:int):
        GetDllLibDoc().ClipboardData_set_Format.argtypes=[c_void_p, c_int]
        CallCFunction(GetDllLibDoc().ClipboardData_set_Format,self.Ptr, value)

#    @property
#
#    def Data(self)->List['Byte']:
#        """
#    <summary>
#        Clipboard data.
#    </summary>
#        """
#        GetDllLibDoc().ClipboardData_get_Data.argtypes=[c_void_p]
#        GetDllLibDoc().ClipboardData_get_Data.restype=IntPtrArray
#        intPtrArray = GetDllLibDoc().ClipboardData_get_Data(self.Ptr)
#        ret = GetVectorFromArray(intPtrArray, Byte)
#        return ret


#    @Data.setter
#    def Data(self, value:List['Byte']):
#        vCount = len(value)
#        ArrayType = c_void_p * vCount
#        vArray = ArrayType()
#        for i in range(0, vCount):
#            vArray[i] = value[i].Ptr
#        GetDllLibDoc().ClipboardData_set_Data.argtypes=[c_void_p, ArrayType, c_int]
#        GetDllLibDoc().ClipboardData_set_Data(self.Ptr, vArray, vCount)



    def Clone(self)->'SpireObject':
        """
        Creates a copy of the current object.
        Returns:
            A copy of the current object.
        """
        GetDllLibDoc().ClipboardData_Clone.argtypes=[c_void_p]
        GetDllLibDoc().ClipboardData_Clone.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().ClipboardData_Clone,self.Ptr)
        ret = None if intPtr==None else SpireObject(intPtr)
        return ret



    def Serialize(self ,stream:'Stream')->int:
        """
        Serializes the clipboard data to a stream.
        Args:
            stream: The stream to serialize to.
        Returns:
            The number of bytes written to the stream.
        """
        intPtrstream:c_void_p = stream.Ptr

        GetDllLibDoc().ClipboardData_Serialize.argtypes=[c_void_p ,c_void_p]
        GetDllLibDoc().ClipboardData_Serialize.restype=c_int
        ret = CallCFunction(GetDllLibDoc().ClipboardData_Serialize,self.Ptr, intPtrstream)
        return ret


    def Parse(self ,stream:'Stream'):
        """
        Parses the clipboard data from a stream.
        Args:
            stream: The stream to parse from.
        """
        intPtrstream:c_void_p = stream.Ptr

        GetDllLibDoc().ClipboardData_Parse.argtypes=[c_void_p ,c_void_p]
        CallCFunction(GetDllLibDoc().ClipboardData_Parse,self.Ptr, intPtrstream)

