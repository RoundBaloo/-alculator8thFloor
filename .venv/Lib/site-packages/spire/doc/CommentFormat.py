from enum import Enum
from plum import dispatch
from typing import TypeVar, Union, Generic, List, Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class CommentFormat(DocumentSerializable):
    """
    Represents a comment format.
    """

    @property
    def DateTime(self) -> 'DateTime':
        """
        Gets or sets the DateTime.

        Returns:
            The DateTime.
        """
        GetDllLibDoc().CommentFormat_get_DateTime.argtypes=[c_void_p]
        GetDllLibDoc().CommentFormat_get_DateTime.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().CommentFormat_get_DateTime,self.Ptr)
        ret = None if intPtr==None else DateTime(intPtr)
        return ret

    @DateTime.setter
    def DateTime(self, value:'DateTime'):
        """
        Sets the DateTime.

        Args:
            value: The DateTime.
        """
        GetDllLibDoc().CommentFormat_set_DateTime.argtypes=[c_void_p, c_void_p]
        CallCFunction(GetDllLibDoc().CommentFormat_set_DateTime,self.Ptr, value.Ptr)

    @property
    def Initial(self) -> str:
        """
        Gets or sets the user initials.

        Returns:
            The user initials.
        """
        GetDllLibDoc().CommentFormat_get_Initial.argtypes=[c_void_p]
        GetDllLibDoc().CommentFormat_get_Initial.restype=c_void_p
        ret = PtrToStr(CallCFunction(GetDllLibDoc().CommentFormat_get_Initial,self.Ptr))
        return ret


    @Initial.setter
    def Initial(self, value:str):
        """
        Sets the user initials.

        Args:
            value: The user initials.
        """
        valuePtr = StrToPtr(value)
        GetDllLibDoc().CommentFormat_set_Initial.argtypes=[c_void_p, c_char_p]
        CallCFunction(GetDllLibDoc().CommentFormat_set_Initial,self.Ptr, valuePtr)

    @property

    def Author(self)->str:
        """
        Gets or sets the user.

        Returns:
            The user.
        """
        GetDllLibDoc().CommentFormat_get_Author.argtypes=[c_void_p]
        GetDllLibDoc().CommentFormat_get_Author.restype=c_void_p
        ret = PtrToStr(CallCFunction(GetDllLibDoc().CommentFormat_get_Author,self.Ptr))
        return ret


    @Author.setter
    def Author(self, value:str):
        """
        Sets the user.

        Args:
            value: The user.
        """
        valuePtr = StrToPtr(value)
        GetDllLibDoc().CommentFormat_set_Author.argtypes=[c_void_p, c_char_p]
        CallCFunction(GetDllLibDoc().CommentFormat_set_Author,self.Ptr, valuePtr)

    @property
    def CommentId(self)->int:
        """
        Gets or sets the id of the comment.

        Returns:
            The comment id.
        """
        GetDllLibDoc().CommentFormat_get_CommentId.argtypes=[c_void_p]
        GetDllLibDoc().CommentFormat_get_CommentId.restype=c_int
        ret = CallCFunction(GetDllLibDoc().CommentFormat_get_CommentId,self.Ptr)
        return ret

    @CommentId.setter
    def CommentId(self, value:int):
        """
        Sets the id of the comment.

        Args:
            value: The comment id.
        """
        GetDllLibDoc().CommentFormat_set_CommentId.argtypes=[c_void_p, c_int]
        CallCFunction(GetDllLibDoc().CommentFormat_set_CommentId,self.Ptr, value)


    def Clone(self ,doc:'IDocument')->'CommentFormat':
        """
        Creates a new object that is a copy of the current instance.

        Args:
            doc: The document.

        Returns:
            A new object that is a copy of this instance.
        """
        intPtrdoc:c_void_p = doc.Ptr

        GetDllLibDoc().CommentFormat_Clone.argtypes=[c_void_p ,c_void_p]
        GetDllLibDoc().CommentFormat_Clone.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().CommentFormat_Clone,self.Ptr, intPtrdoc)
        ret = None if intPtr==None else CommentFormat(intPtr)
        return ret


