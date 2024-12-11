from enum import Enum
from plum import dispatch
from typing import TypeVar, Union, Generic, List, Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class XDLSHolder (SpireObject) :
    """
    Represents an XDLSHolder object.
    """
    @property
    def ID(self)->int:
        """
        Gets the ID of the XDLSHolder.
        """
        GetDllLibDoc().XDLSHolder_get_ID.argtypes=[c_void_p]
        GetDllLibDoc().XDLSHolder_get_ID.restype=c_int
        ret = CallCFunction(GetDllLibDoc().XDLSHolder_get_ID,self.Ptr)
        return ret

    @ID.setter
    def ID(self, value:int):
        """
        Sets the ID of the XDLSHolder.
        """
        GetDllLibDoc().XDLSHolder_set_ID.argtypes=[c_void_p, c_int]
        CallCFunction(GetDllLibDoc().XDLSHolder_set_ID,self.Ptr, value)

    @property
    def Cleared(self)->bool:
        """
        Gets the Cleared status of the XDLSHolder.
        """
        GetDllLibDoc().XDLSHolder_get_Cleared.argtypes=[c_void_p]
        GetDllLibDoc().XDLSHolder_get_Cleared.restype=c_bool
        ret = CallCFunction(GetDllLibDoc().XDLSHolder_get_Cleared,self.Ptr)
        return ret

    @Cleared.setter
    def Cleared(self, value:bool):
        """
        Sets the Cleared status of the XDLSHolder.
        """
        GetDllLibDoc().XDLSHolder_set_Cleared.argtypes=[c_void_p, c_bool]
        CallCFunction(GetDllLibDoc().XDLSHolder_set_Cleared,self.Ptr, value)

    @property
    def EnableID(self)->bool:
        """
        Gets the EnableID status of the XDLSHolder.
        """
        GetDllLibDoc().XDLSHolder_get_EnableID.argtypes=[c_void_p]
        GetDllLibDoc().XDLSHolder_get_EnableID.restype=c_bool
        ret = CallCFunction(GetDllLibDoc().XDLSHolder_get_EnableID,self.Ptr)
        return ret

    @EnableID.setter
    def EnableID(self, value:bool):
        """
        Sets the EnableID status of the XDLSHolder.
        """
        GetDllLibDoc().XDLSHolder_set_EnableID.argtypes=[c_void_p, c_bool]
        CallCFunction(GetDllLibDoc().XDLSHolder_set_EnableID,self.Ptr, value)

    @property
    def SkipMe(self)->bool:
        """
        Gets the SkipMe status of the XDLSHolder.
        """
        GetDllLibDoc().XDLSHolder_get_SkipMe.argtypes=[c_void_p]
        GetDllLibDoc().XDLSHolder_get_SkipMe.restype=c_bool
        ret = CallCFunction(GetDllLibDoc().XDLSHolder_get_SkipMe,self.Ptr)
        return ret

    @SkipMe.setter
    def SkipMe(self, value:bool):
        """
        Sets the SkipMe status of the XDLSHolder.
        """
        GetDllLibDoc().XDLSHolder_set_SkipMe.argtypes=[c_void_p, c_bool]
        CallCFunction(GetDllLibDoc().XDLSHolder_set_SkipMe,self.Ptr, value)

    def Dispose(self):
        """
        Disposes the XDLSHolder object.
        """
        GetDllLibDoc().XDLSHolder_Dispose.argtypes=[c_void_p]
        CallCFunction(GetDllLibDoc().XDLSHolder_Dispose,self.Ptr)


    def AddElement(self ,tagName:str,value:'SpireObject'):
        """
        Adds an element to the XDLSHolder.
        """
        tagNamePtr = StrToPtr(tagName)
        intPtrvalue:c_void_p = value.Ptr

        GetDllLibDoc().XDLSHolder_AddElement.argtypes=[c_void_p ,c_char_p,c_void_p]
        CallCFunction(GetDllLibDoc().XDLSHolder_AddElement,self.Ptr, tagNamePtr,intPtrvalue)


    def AddRefElement(self ,tagName:str,value:'SpireObject'):
        """
        Adds a reference element to the XDLSHolder.
        """
        tagNamePtr = StrToPtr(tagName)
        intPtrvalue:c_void_p = value.Ptr

        GetDllLibDoc().XDLSHolder_AddRefElement.argtypes=[c_void_p ,c_char_p,c_void_p]
        CallCFunction(GetDllLibDoc().XDLSHolder_AddRefElement,self.Ptr, tagNamePtr,intPtrvalue)


    def WriteHolder(self ,writer:'IXDLSContentWriter'):
        """
        Writes the XDLSHolder using the specified writer.
        """
        intPtrwriter:c_void_p = writer.Ptr

        GetDllLibDoc().XDLSHolder_WriteHolder.argtypes=[c_void_p ,c_void_p]
        CallCFunction(GetDllLibDoc().XDLSHolder_WriteHolder,self.Ptr, intPtrwriter)


    def ReadHolder(self ,reader:'IXDLSContentReader')->bool:
        """
        Reads the XDLSHolder using the specified reader.
        """
        intPtrreader:c_void_p = reader.Ptr

        GetDllLibDoc().XDLSHolder_ReadHolder.argtypes=[c_void_p ,c_void_p]
        GetDllLibDoc().XDLSHolder_ReadHolder.restype=c_bool
        ret = CallCFunction(GetDllLibDoc().XDLSHolder_ReadHolder,self.Ptr, intPtrreader)
        return ret


    def AfterDeserialization(self ,owner:'IDocumentSerializable'):
        """
        Performs actions after deserialization using the specified owner.
        """
        intPtrowner:c_void_p = owner.Ptr

        GetDllLibDoc().XDLSHolder_AfterDeserialization.argtypes=[c_void_p ,c_void_p]
        CallCFunction(GetDllLibDoc().XDLSHolder_AfterDeserialization,self.Ptr, intPtrowner)

    def BeforeSerialization(self):
        """
        Performs actions before serialization.
        """
        GetDllLibDoc().XDLSHolder_BeforeSerialization.argtypes=[c_void_p]
        CallCFunction(GetDllLibDoc().XDLSHolder_BeforeSerialization,self.Ptr)

