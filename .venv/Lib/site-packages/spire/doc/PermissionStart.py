from enum import Enum
from plum import dispatch
from typing import TypeVar, Union, Generic, List, Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class PermissionStart (  ParagraphBase, IDocumentObject) :
    """
    Represents a permission start in a document.
    """
    @dispatch
    def __init__(self, doc:IDocument, idStr:str):
        """
        Initializes a new instance of the PermissionStart class.

        Args:
            doc (IDocument): The document object.
            idStr (str): The permission start id.
        """
        idStrPtr = StrToPtr(idStr)
        intPdoc:c_void_p =  doc.Ptr

        GetDllLibDoc().PermissionStart_CreatePermissionStartDI.argtypes=[c_void_p,c_char_p]
        GetDllLibDoc().PermissionStart_CreatePermissionStartDI.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().PermissionStart_CreatePermissionStartDI,intPdoc,idStrPtr)
        super(PermissionStart, self).__init__(intPtr)

    @property

    def DocumentObjectType(self)->'DocumentObjectType':
        """
        Gets the type of the document object.

        Returns:
            DocumentObjectType: The type of the document object.
        """
        GetDllLibDoc().PermissionStart_get_DocumentObjectType.argtypes=[c_void_p]
        GetDllLibDoc().PermissionStart_get_DocumentObjectType.restype=c_int
        ret = CallCFunction(GetDllLibDoc().PermissionStart_get_DocumentObjectType,self.Ptr)
        objwraped = DocumentObjectType(ret)
        return objwraped

    @property

    def Id(self)->str:
        """
        Gets the permission start id.

        Returns:
            str: The permission start id.
        """
        GetDllLibDoc().PermissionStart_get_Id.argtypes=[c_void_p]
        GetDllLibDoc().PermissionStart_get_Id.restype=c_void_p
        ret = PtrToStr(CallCFunction(GetDllLibDoc().PermissionStart_get_Id,self.Ptr))
        return ret


    @property

    def EditorGroup(self)->'EditingGroup':
        """
        Gets the permission editor group.

        Returns:
            EditingGroup: The permission editor group.
        """
        GetDllLibDoc().PermissionStart_get_EditorGroup.argtypes=[c_void_p]
        GetDllLibDoc().PermissionStart_get_EditorGroup.restype=c_int
        ret = CallCFunction(GetDllLibDoc().PermissionStart_get_EditorGroup,self.Ptr)
        objwraped = EditingGroup(ret)
        return objwraped

    @EditorGroup.setter
    def EditorGroup(self, value:'EditingGroup'):
        """
        Sets the permission editor group.

        Args:
            value (EditingGroup): The permission editor group.
        """
        GetDllLibDoc().PermissionStart_set_EditorGroup.argtypes=[c_void_p, c_int]
        CallCFunction(GetDllLibDoc().PermissionStart_set_EditorGroup,self.Ptr, value.value)

