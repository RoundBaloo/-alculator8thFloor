from enum import Enum
from plum import dispatch
from typing import TypeVar, Union, Generic, List, Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class EntityEntry (SpireObject) :
    """
    Represents an entry in the entity.
    """
    @property

    def Current(self)->'DocumentObject':
        """
        Gets the current document object.
        """
        GetDllLibDoc().EntityEntry_get_Current.argtypes=[c_void_p]
        GetDllLibDoc().EntityEntry_get_Current.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().EntityEntry_get_Current,self.Ptr)
        ret = None if intPtr==None else DocumentObject(intPtr)
        return ret


    @Current.setter
    def Current(self, value:'DocumentObject'):
        """
        Sets the current document object.
        """
        GetDllLibDoc().EntityEntry_set_Current.argtypes=[c_void_p, c_void_p]
        CallCFunction(GetDllLibDoc().EntityEntry_set_Current,self.Ptr, value.Ptr)

    @property
    def Index(self)->int:
        """
        Gets the index of the entity entry.
        """
        GetDllLibDoc().EntityEntry_get_Index.argtypes=[c_void_p]
        GetDllLibDoc().EntityEntry_get_Index.restype=c_int
        ret = CallCFunction(GetDllLibDoc().EntityEntry_get_Index,self.Ptr)
        return ret

    @Index.setter
    def Index(self, value:int):
        """
        Sets the index of the entity entry.
        """
        GetDllLibDoc().EntityEntry_set_Index.argtypes=[c_void_p, c_int]
        CallCFunction(GetDllLibDoc().EntityEntry_set_Index,self.Ptr, value)

    def Fetch(self)->bool:
        """
        Fetches the entity entry.
        """
        GetDllLibDoc().EntityEntry_Fetch.argtypes=[c_void_p]
        GetDllLibDoc().EntityEntry_Fetch.restype=c_bool
        ret = CallCFunction(GetDllLibDoc().EntityEntry_Fetch,self.Ptr)
        return ret
