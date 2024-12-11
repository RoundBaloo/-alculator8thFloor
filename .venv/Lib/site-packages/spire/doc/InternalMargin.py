from enum import Enum
from plum import dispatch
from typing import TypeVar,Union,Generic,List,Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class InternalMargin (SpireObject) :
    """
    Represents an internal margin.
    """
    def SetAll(self, value:float):
        """
        Sets all internal margins to the specified value.

        Args:
            value (float): The value to set all internal margins to.
        """
        GetDllLibDoc().InternalMargin_set_All.argtypes=[c_void_p, c_float]
        CallCFunction(GetDllLibDoc().InternalMargin_set_All,self.Ptr, value)

    @property
    def Left(self)->float:
        """
        Gets or sets the internal left margin (in points).

        Returns:
            float: The internal left margin.
        """
        GetDllLibDoc().InternalMargin_get_Left.argtypes=[c_void_p]
        GetDllLibDoc().InternalMargin_get_Left.restype=c_float
        ret = CallCFunction(GetDllLibDoc().InternalMargin_get_Left,self.Ptr)
        return ret

    @Left.setter
    def Left(self, value:float):
        """
        Sets the internal left margin (in points).

        Args:
            value (float): The value to set the internal left margin to.
        """
        GetDllLibDoc().InternalMargin_set_Left.argtypes=[c_void_p, c_float]
        CallCFunction(GetDllLibDoc().InternalMargin_set_Left,self.Ptr, value)

    @property
    def Right(self)->float:
        """
        Gets or sets the internal right margin (in points).

        Returns:
            float: The internal right margin.
        """
        GetDllLibDoc().InternalMargin_get_Right.argtypes=[c_void_p]
        GetDllLibDoc().InternalMargin_get_Right.restype=c_float
        ret = CallCFunction(GetDllLibDoc().InternalMargin_get_Right,self.Ptr)
        return ret

    @Right.setter
    def Right(self, value:float):
        """
        Sets the internal right margin (in points).

        Args:
            value (float): The value to set the internal right margin to.
        """
        GetDllLibDoc().InternalMargin_set_Right.argtypes=[c_void_p, c_float]
        CallCFunction(GetDllLibDoc().InternalMargin_set_Right,self.Ptr, value)

    @property
    def Top(self)->float:
        """
        Gets or sets the internal top margin (in points).

        Returns:
            float: The internal top margin.
        """
        GetDllLibDoc().InternalMargin_get_Top.argtypes=[c_void_p]
        GetDllLibDoc().InternalMargin_get_Top.restype=c_float
        ret = CallCFunction(GetDllLibDoc().InternalMargin_get_Top,self.Ptr)
        return ret

    @Top.setter
    def Top(self, value:float):
        """
        Sets the internal top margin (in points).

        Args:
            value (float): The value to set the internal top margin to.
        """
        GetDllLibDoc().InternalMargin_set_Top.argtypes=[c_void_p, c_float]
        CallCFunction(GetDllLibDoc().InternalMargin_set_Top,self.Ptr, value)

    @property
    def Bottom(self)->float:
        """
        Gets or sets the internal bottom margin (in points).

        Returns:
            float: The internal bottom margin.
        """
        GetDllLibDoc().InternalMargin_get_Bottom.argtypes=[c_void_p]
        GetDllLibDoc().InternalMargin_get_Bottom.restype=c_float
        ret = CallCFunction(GetDllLibDoc().InternalMargin_get_Bottom,self.Ptr)
        return ret

    @Bottom.setter
    def Bottom(self, value:float):
        """
        Sets the internal bottom margin (in points).

        Args:
            value (float): The value to set the internal bottom margin to.
        """
        GetDllLibDoc().InternalMargin_set_Bottom.argtypes=[c_void_p, c_float]
        CallCFunction(GetDllLibDoc().InternalMargin_set_Bottom,self.Ptr, value)

