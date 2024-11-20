from enum import Enum
from plum import dispatch
from typing import TypeVar, Union, Generic, List, Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class Permission (SpireObject) :
    """
    Represents a permission.
    """
    @property

    def Id(self)->str:
        """
        Gets the permission id.
        """
        GetDllLibDoc().Permission_get_Id.argtypes=[c_void_p]
        GetDllLibDoc().Permission_get_Id.restype=c_void_p
        ret = PtrToStr(CallCFunction(GetDllLibDoc().Permission_get_Id,self.Ptr))
        return ret


    @property

    def EditorGroup(self)->'EditingGroup':
        """
        Gets the permission's editor group.
        """
        GetDllLibDoc().Permission_get_EditorGroup.argtypes=[c_void_p]
        GetDllLibDoc().Permission_get_EditorGroup.restype=c_int
        ret = CallCFunction(GetDllLibDoc().Permission_get_EditorGroup,self.Ptr)
        objwraped = EditingGroup(ret)
        return objwraped

    @property

    def PermissionStart(self)->'PermissionStart':
        """
        Gets the permission start.
        """
        GetDllLibDoc().Permission_get_PermissionStart.argtypes=[c_void_p]
        GetDllLibDoc().Permission_get_PermissionStart.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().Permission_get_PermissionStart,self.Ptr)
        ret = None if intPtr==None else PermissionStart(intPtr)
        return ret


    @property

    def PermissionEnd(self)->'PermissionEnd':
        """
        Gets the permission end.
        """
        GetDllLibDoc().Permission_get_PermissionEnd.argtypes=[c_void_p]
        GetDllLibDoc().Permission_get_PermissionEnd.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().Permission_get_PermissionEnd,self.Ptr)
        ret = None if intPtr==None else PermissionEnd(intPtr)
        return ret


