from enum import Enum
from plum import dispatch
from typing import TypeVar, Union, Generic, List, Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class ViewSetup (  DocumentSerializable) :
    """
    Represents the setup for a view.
    """
    @property
    def ZoomPercent(self)->int:
        """
        Returns or sets the zooming value in percents.

        Returns:
            int: The zoom percent.
        """
        GetDllLibDoc().ViewSetup_get_ZoomPercent.argtypes=[c_void_p]
        GetDllLibDoc().ViewSetup_get_ZoomPercent.restype=c_int
        ret = CallCFunction(GetDllLibDoc().ViewSetup_get_ZoomPercent,self.Ptr)
        return ret

    @ZoomPercent.setter
    def ZoomPercent(self, value:int):
        """
        Sets the zooming value in percents.

        Args:
            value (int): The zoom percent.
        """
        GetDllLibDoc().ViewSetup_set_ZoomPercent.argtypes=[c_void_p, c_int]
        CallCFunction(GetDllLibDoc().ViewSetup_set_ZoomPercent,self.Ptr, value)

    @property

    def ZoomType(self)->'ZoomType':
        """
        Returns or sets the zooming type.

        Returns:
            ZoomType: The type of the zoom.
        """
        GetDllLibDoc().ViewSetup_get_ZoomType.argtypes=[c_void_p]
        GetDllLibDoc().ViewSetup_get_ZoomType.restype=c_int
        ret = CallCFunction(GetDllLibDoc().ViewSetup_get_ZoomType,self.Ptr)
        objwraped = ZoomType(ret)
        return objwraped

    @ZoomType.setter
    def ZoomType(self, value:'ZoomType'):
        """
        Sets the zooming type.

        Args:
            value (ZoomType): The type of the zoom.
        """
        GetDllLibDoc().ViewSetup_set_ZoomType.argtypes=[c_void_p, c_int]
        CallCFunction(GetDllLibDoc().ViewSetup_set_ZoomType,self.Ptr, value.value)

    @property

    def DocumentViewType(self)->'DocumentViewType':
        """
        Returns or sets the document view mode.

        Returns:
            DocumentViewType: The type of the document view.
        """
        GetDllLibDoc().ViewSetup_get_DocumentViewType.argtypes=[c_void_p]
        GetDllLibDoc().ViewSetup_get_DocumentViewType.restype=c_int
        ret = CallCFunction(GetDllLibDoc().ViewSetup_get_DocumentViewType,self.Ptr)
        objwraped = DocumentViewType(ret)
        return objwraped

    @DocumentViewType.setter
    def DocumentViewType(self, value:'DocumentViewType'):
        """
        Sets the document view mode.

        Args:
            value (DocumentViewType): The type of the document view.
        """
        GetDllLibDoc().ViewSetup_set_DocumentViewType.argtypes=[c_void_p, c_int]
        CallCFunction(GetDllLibDoc().ViewSetup_set_DocumentViewType,self.Ptr, value.value)

    @staticmethod
    def DEF_ZOOMING()->int:
        """
        Returns the constant value for Zoom.

        Returns:
            int: The constant value for Zoom.
        """
        #GetDllLibDoc().ViewSetup_DEF_ZOOMING.argtypes=[]
        GetDllLibDoc().ViewSetup_DEF_ZOOMING.restype=c_int
        ret = CallCFunction(GetDllLibDoc().ViewSetup_DEF_ZOOMING,)
        return ret

