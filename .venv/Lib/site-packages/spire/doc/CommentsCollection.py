from enum import Enum
from plum import dispatch
from typing import TypeVar, Union, Generic, List, Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class CommentsCollection(CollectionEx):
    """
    A collection of Comment objects that represent the comments in the document.
    """

    def get_Item(self ,index:int)->'Comment':
        """
        Gets the comment at the specified index.

        Args:
            index: The index of the comment.

        Returns:
            The comment at the specified index.
        """
        
        GetDllLibDoc().CommentsCollection_get_Item.argtypes=[c_void_p ,c_int]
        GetDllLibDoc().CommentsCollection_get_Item.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().CommentsCollection_get_Item,self.Ptr, index)
        ret = None if intPtr==None else Comment(intPtr)
        return ret


    def Counts(self)->int:
        """
        Counts the number of comments in this instance.

        Returns:
            The number of comments in this instance.
        """
        GetDllLibDoc().CommentsCollection_Counts.argtypes=[c_void_p]
        GetDllLibDoc().CommentsCollection_Counts.restype=c_int
        ret = CallCFunction(GetDllLibDoc().CommentsCollection_Counts,self.Ptr)
        return ret


    def RemoveAt(self ,index:int):
        """
        Removes a comment at the specified index.

        Args:
            index: The index of the comment to remove.
        """
        
        GetDllLibDoc().CommentsCollection_RemoveAt.argtypes=[c_void_p ,c_int]
        CallCFunction(GetDllLibDoc().CommentsCollection_RemoveAt,self.Ptr, index)

    def Clear(self):
        """
        Removes all the comments from the document.
        """
        GetDllLibDoc().CommentsCollection_Clear.argtypes=[c_void_p]
        CallCFunction(GetDllLibDoc().CommentsCollection_Clear,self.Ptr)


    def Remove(self ,comment:'Comment'):
        """
        Removes the specified comment.

        Args:
            comment: The comment to remove.
        """
        intPtrcomment:c_void_p = comment.Ptr

        GetDllLibDoc().CommentsCollection_Remove.argtypes=[c_void_p ,c_void_p]
        CallCFunction(GetDllLibDoc().CommentsCollection_Remove,self.Ptr, intPtrcomment)

