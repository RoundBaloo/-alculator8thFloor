from enum import Enum
from plum import dispatch
from typing import TypeVar, Union, Generic, List, Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class PermissionCollection (  CollectionEx) :
    """
    A collection of Permission objects that represent the permission in the document.
    """
    @dispatch

    def get_Item(self ,id:str)->Permission:
        """
        Gets the Permission with the specified id.
        """
        idPtr = StrToPtr(id)
        GetDllLibDoc().PermissionCollection_get_Item.argtypes=[c_void_p ,c_char_p]
        GetDllLibDoc().PermissionCollection_get_Item.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().PermissionCollection_get_Item,self.Ptr, idPtr)
        ret = None if intPtr==None else Permission(intPtr)
        return ret


    @dispatch

    def get_Item(self ,index:int)->Permission:
        """
        Gets the Permission at the specified index.
        """
        
        GetDllLibDoc().PermissionCollection_get_ItemI.argtypes=[c_void_p ,c_int]
        GetDllLibDoc().PermissionCollection_get_ItemI.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().PermissionCollection_get_ItemI,self.Ptr, index)
        ret = None if intPtr==None else Permission(intPtr)
        return ret



    def FindById(self ,id:str)->'Permission':
        """
        Finds Permission object by specified id.
        """
        idPtr = StrToPtr(id)
        GetDllLibDoc().PermissionCollection_FindById.argtypes=[c_void_p ,c_char_p]
        GetDllLibDoc().PermissionCollection_FindById.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().PermissionCollection_FindById,self.Ptr, idPtr)
        ret = None if intPtr==None else Permission(intPtr)
        return ret



    def RemoveAt(self ,index:int):
        """
        Removes a permission at the specified index.
        """
        
        GetDllLibDoc().PermissionCollection_RemoveAt.argtypes=[c_void_p ,c_int]
        CallCFunction(GetDllLibDoc().PermissionCollection_RemoveAt,self.Ptr, index)


    def Remove(self ,permission:'Permission'):
        """
        Removes the specified permission.
        """
        intPtrpermission:c_void_p = permission.Ptr

        GetDllLibDoc().PermissionCollection_Remove.argtypes=[c_void_p ,c_void_p]
        CallCFunction(GetDllLibDoc().PermissionCollection_Remove,self.Ptr, intPtrpermission)

    def Clear(self):
        """
        Removes all permissions from the document.
        """
        GetDllLibDoc().PermissionCollection_Clear.argtypes=[c_void_p]
        CallCFunction(GetDllLibDoc().PermissionCollection_Clear,self.Ptr)

