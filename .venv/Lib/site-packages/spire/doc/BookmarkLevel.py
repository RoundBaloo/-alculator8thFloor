from enum import Enum
from plum import dispatch
from typing import TypeVar, Union, Generic, List, Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class BookmarkLevel(SpireObject):
    """
    Class BookmarkLevel.
    """
#    @property
#
#    def ChildObjects(self)->'List1':
#        """
#    <summary>
#        Gets the child objects.
#    </summary>
#        """
#        GetDllLibDoc().BookmarkLevel_get_ChildObjects.argtypes=[c_void_p]
#        GetDllLibDoc().BookmarkLevel_get_ChildObjects.restype=c_void_p
#        intPtr = GetDllLibDoc().BookmarkLevel_get_ChildObjects(self.Ptr)
#        ret = None if intPtr==None else List1(intPtr)
#        return ret
#

    @property
    def Color(self) -> 'Color':
        """
        Gets or Sets the text color of the bookmark when convert to PDF.
        The default value is the "SaddleBrown" color(#FF8B4513).
        """
        GetDllLibDoc().BookmarkLevel_get_Color.argtypes=[c_void_p]
        GetDllLibDoc().BookmarkLevel_get_Color.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().BookmarkLevel_get_Color,self.Ptr)
        ret = None if intPtr==None else Color(intPtr)
        return ret


    @Color.setter
    def Color(self, value:'Color'):
        GetDllLibDoc().BookmarkLevel_set_Color.argtypes=[c_void_p, c_void_p]
        CallCFunction(GetDllLibDoc().BookmarkLevel_set_Color,self.Ptr, value.Ptr)

    @property
    def Name(self) -> str:
        """
        Gets the name of the bookmark.
        """
        GetDllLibDoc().BookmarkLevel_get_Name.argtypes=[c_void_p]
        GetDllLibDoc().BookmarkLevel_get_Name.restype=c_void_p
        ret = PtrToStr(CallCFunction(GetDllLibDoc().BookmarkLevel_get_Name,self.Ptr))
        return ret

    @property
    def Level(self) -> int:
        """
        Gets or sets the level.
        <value>The level.</value>
        """
        GetDllLibDoc().BookmarkLevel_get_Level.argtypes=[c_void_p]
        GetDllLibDoc().BookmarkLevel_get_Level.restype=c_int
        ret = CallCFunction(GetDllLibDoc().BookmarkLevel_get_Level,self.Ptr)
        return ret

    @property
    def Style(self) -> 'BookmarkTextStyle':
        """
        Sets the text style of the bookmark when convert to PDF.
        The default value is the Bold.
        """
        GetDllLibDoc().BookmarkLevel_get_Style.argtypes=[c_void_p]
        GetDllLibDoc().BookmarkLevel_get_Style.restype=c_int
        ret = CallCFunction(GetDllLibDoc().BookmarkLevel_get_Style,self.Ptr)
        objwraped = BookmarkTextStyle(ret)
        return objwraped

    @Style.setter
    def Style(self, value:'BookmarkTextStyle'):
        GetDllLibDoc().BookmarkLevel_set_Style.argtypes=[c_void_p, c_int]
        CallCFunction(GetDllLibDoc().BookmarkLevel_set_Style,self.Ptr, value.value)

