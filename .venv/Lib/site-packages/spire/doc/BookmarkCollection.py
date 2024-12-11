from enum import Enum
from plum import dispatch
from typing import TypeVar, Union, Generic, List, Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class BookmarkCollection(CollectionEx):
    """
    A collection of Bookmark objects that represent the bookmarks in the document.
    """

    @dispatch
    def get_Item(self, name: str) -> Bookmark:
        """
        Gets the Bookmark with the specified name.
        """
        namePtr = StrToPtr(name)
        GetDllLibDoc().BookmarkCollection_get_Item.argtypes=[c_void_p ,c_char_p]
        GetDllLibDoc().BookmarkCollection_get_Item.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().BookmarkCollection_get_Item,self.Ptr, namePtr)
        ret = None if intPtr==None else Bookmark(intPtr)
        return ret

    @dispatch
    def get_Item(self, index: int) -> Bookmark:
        """
        Gets the Bookmark at the specified index.
        """
        
        GetDllLibDoc().BookmarkCollection_get_ItemI.argtypes=[c_void_p ,c_int]
        GetDllLibDoc().BookmarkCollection_get_ItemI.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().BookmarkCollection_get_ItemI,self.Ptr, index)
        ret = None if intPtr==None else Bookmark(intPtr)
        return ret

    def FindByName(self, name: str) -> 'Bookmark':
        """
        Finds Bookmark object by specified name.
        :param name: The bookmark name
        :returns: The found Bookmark object
        """
        namePtr = StrToPtr(name)
        GetDllLibDoc().BookmarkCollection_FindByName.argtypes=[c_void_p ,c_char_p]
        GetDllLibDoc().BookmarkCollection_FindByName.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().BookmarkCollection_FindByName,self.Ptr, namePtr)
        ret = None if intPtr==None else Bookmark(intPtr)
        return ret

    def RemoveAt(self, index: int):
        """
        Removes a bookmark at the specified index.
        :param index: The index.
        """
        
        GetDllLibDoc().BookmarkCollection_RemoveAt.argtypes=[c_void_p ,c_int]
        CallCFunction(GetDllLibDoc().BookmarkCollection_RemoveAt,self.Ptr, index)

    def Remove(self, bookmark: 'Bookmark'):
        """
        Removes the specified bookmark.
        :param bookmark: The bookmark.
        """
        intPtrbookmark:c_void_p = bookmark.Ptr

        GetDllLibDoc().BookmarkCollection_Remove.argtypes=[c_void_p ,c_void_p]
        CallCFunction(GetDllLibDoc().BookmarkCollection_Remove,self.Ptr, intPtrbookmark)

    def Clear(self):
        """
        Removes all bookmarks from the document.
        """
        GetDllLibDoc().BookmarkCollection_Clear.argtypes=[c_void_p]
        CallCFunction(GetDllLibDoc().BookmarkCollection_Clear,self.Ptr)

