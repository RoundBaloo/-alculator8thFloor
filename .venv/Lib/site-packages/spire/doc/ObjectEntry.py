from enum import Enum
from plum import dispatch
from typing import TypeVar, Union, Generic, List, Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class ObjectEntry (SpireObject) :
    """
    Represents an object entry.
    """
    @property

    def Current(self)->'DocumentObject':
        """
        Gets the current document object.
        """
        GetDllLibDoc().ObjectEntry_get_Current.argtypes=[c_void_p]
        GetDllLibDoc().ObjectEntry_get_Current.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().ObjectEntry_get_Current,self.Ptr)
        ret = None if intPtr==None else DocumentObject(intPtr)
        return ret


    @Current.setter
    def Current(self, value:'DocumentObject'):
        """
        Sets the current document object.
        """
        GetDllLibDoc().ObjectEntry_set_Current.argtypes=[c_void_p, c_void_p]
        CallCFunction(GetDllLibDoc().ObjectEntry_set_Current,self.Ptr, value.Ptr)

    @property
    def Index(self)->int:
        """
        Gets the index.
        """
        GetDllLibDoc().ObjectEntry_get_Index.argtypes=[c_void_p]
        GetDllLibDoc().ObjectEntry_get_Index.restype=c_int
        ret = CallCFunction(GetDllLibDoc().ObjectEntry_get_Index,self.Ptr)
        return ret

    @Index.setter
    def Index(self, value:int):
        """
        Sets the index.
        """
        GetDllLibDoc().ObjectEntry_set_Index.argtypes=[c_void_p, c_int]
        CallCFunction(GetDllLibDoc().ObjectEntry_set_Index,self.Ptr, value)

    def Fetch(self)->bool:
        """
        Fetches the object entry.
        """
        GetDllLibDoc().ObjectEntry_Fetch.argtypes=[c_void_p]
        GetDllLibDoc().ObjectEntry_Fetch.restype=c_bool
        ret = CallCFunction(GetDllLibDoc().ObjectEntry_Fetch,self.Ptr)
        return ret

