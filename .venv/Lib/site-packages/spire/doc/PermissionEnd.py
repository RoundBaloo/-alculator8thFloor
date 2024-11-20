from enum import Enum
from plum import dispatch
from typing import TypeVar, Union, Generic, List, Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class PermissionEnd (  ParagraphBase, IDocumentObject) :
    """
    Represents a permission end in a document.
    """
    @dispatch
    def __init__(self, document:IDocument, idStr:str):
        """
        Initializes a new instance of the PermissionEnd class.

        Args:
            document: The document object.
            idStr: The permission ID.
        """
        idStrPtr = StrToPtr(idStr)
        intPdocument:c_void_p =  document.Ptr

        GetDllLibDoc().PermissionEnd_CreatePermissionEndDI.argtypes=[c_void_p,c_char_p]
        GetDllLibDoc().PermissionEnd_CreatePermissionEndDI.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().PermissionEnd_CreatePermissionEndDI,intPdocument,idStrPtr)
        super(PermissionEnd, self).__init__(intPtr)

    @property

    def DocumentObjectType(self)->'DocumentObjectType':
        """
        Gets the type of the document object.

        Returns:
            The type of the document object.
        """
        GetDllLibDoc().PermissionEnd_get_DocumentObjectType.argtypes=[c_void_p]
        GetDllLibDoc().PermissionEnd_get_DocumentObjectType.restype=c_int
        ret = CallCFunction(GetDllLibDoc().PermissionEnd_get_DocumentObjectType,self.Ptr)
        objwraped = DocumentObjectType(ret)
        return objwraped

    @property

    def Id(self)->str:
        """
        Gets the permission ID.

        Returns:
            The permission ID.
        """
        GetDllLibDoc().PermissionEnd_get_Id.argtypes=[c_void_p]
        GetDllLibDoc().PermissionEnd_get_Id.restype=c_void_p
        ret = PtrToStr(CallCFunction(GetDllLibDoc().PermissionEnd_get_Id,self.Ptr))
        return ret


    @property

    def EditorGroup(self)->'EditingGroup':
        """
        Gets the permission editor group.

        Returns:
            The permission editor group.
        """
        GetDllLibDoc().PermissionEnd_get_EditorGroup.argtypes=[c_void_p]
        GetDllLibDoc().PermissionEnd_get_EditorGroup.restype=c_int
        ret = CallCFunction(GetDllLibDoc().PermissionEnd_get_EditorGroup,self.Ptr)
        objwraped = EditingGroup(ret)
        return objwraped

    @EditorGroup.setter
    def EditorGroup(self, value:'EditingGroup'):
        """
        Sets the permission editor group.

        Args:
            value: The permission editor group.
        """
        GetDllLibDoc().PermissionEnd_set_EditorGroup.argtypes=[c_void_p, c_int]
        CallCFunction(GetDllLibDoc().PermissionEnd_set_EditorGroup,self.Ptr, value.value)

