from enum import Enum
from plum import dispatch
from typing import TypeVar, Union, Generic, List, Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class MarginsF (  WordAttrCollection) :
    """
    Represents a collection of margins for a document.
    """
    @dispatch
    def __init__(self, left:float, top:float, right:float, bottom:float):
        """
        Initializes a new instance of the MarginsF class.

        Args:
            left (float): The left margin.
            top (float): The top margin.
            right (float): The right margin.
            bottom (float): The bottom margin.
        """
        GetDllLibDoc().MarginsF_CreateMarginsFLTRB.argtypes=[c_float,c_float,c_float,c_float]
        GetDllLibDoc().MarginsF_CreateMarginsFLTRB.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().MarginsF_CreateMarginsFLTRB,left, top, right, bottom)
        super(MarginsF, self).__init__(intPtr)


    @property
    def All(self)->float:
        """
        Gets or sets the value of all margins.

        Returns:
            float: The value of all margins.
        """
        GetDllLibDoc().MarginsF_get_All.argtypes=[c_void_p]
        GetDllLibDoc().MarginsF_get_All.restype=c_float
        ret = CallCFunction(GetDllLibDoc().MarginsF_get_All,self.Ptr)
        return ret

    @All.setter
    def All(self, value:float):
        """
        Sets the value of all margins.

        Args:
            value (float): The value to set for all margins.
        """
        GetDllLibDoc().MarginsF_set_All.argtypes=[c_void_p, c_float]
        CallCFunction(GetDllLibDoc().MarginsF_set_All,self.Ptr, value)

    @property
    def Left(self)->float:
        """
        Gets or sets the left margin.

        Returns:
            float: The left margin.
        """
        GetDllLibDoc().MarginsF_get_Left.argtypes=[c_void_p]
        GetDllLibDoc().MarginsF_get_Left.restype=c_float
        ret = CallCFunction(GetDllLibDoc().MarginsF_get_Left,self.Ptr)
        return ret

    @Left.setter
    def Left(self, value:float):
        """
        Sets the left margin.

        Args:
            value (float): The value to set for the left margin.
        """
        GetDllLibDoc().MarginsF_set_Left.argtypes=[c_void_p, c_float]
        CallCFunction(GetDllLibDoc().MarginsF_set_Left,self.Ptr, value)

    @property
    def Right(self)->float:
        """
        Gets or sets the right margin.

        Returns:
            float: The right margin.
        """
        GetDllLibDoc().MarginsF_get_Right.argtypes=[c_void_p]
        GetDllLibDoc().MarginsF_get_Right.restype=c_float
        ret = CallCFunction(GetDllLibDoc().MarginsF_get_Right,self.Ptr)
        return ret

    @Right.setter
    def Right(self, value:float):
        """
        Sets the right margin.

        Args:
            value (float): The value to set for the right margin.
        """
        GetDllLibDoc().MarginsF_set_Right.argtypes=[c_void_p, c_float]
        CallCFunction(GetDllLibDoc().MarginsF_set_Right,self.Ptr, value)

    @property
    def Top(self)->float:
        """
        Gets or sets the top margin.

        Returns:
            float: The top margin.
        """
        GetDllLibDoc().MarginsF_get_Top.argtypes=[c_void_p]
        GetDllLibDoc().MarginsF_get_Top.restype=c_float
        ret = CallCFunction(GetDllLibDoc().MarginsF_get_Top,self.Ptr)
        return ret

    @Top.setter
    def Top(self, value:float):
        """
        Sets the top margin.

        Args:
            value (float): The value to set for the top margin.
        """
        GetDllLibDoc().MarginsF_set_Top.argtypes=[c_void_p, c_float]
        CallCFunction(GetDllLibDoc().MarginsF_set_Top,self.Ptr, value)

    @property
    def Bottom(self)->float:
        """
        Gets or sets the bottom margin.

        Returns:
            float: The bottom margin.
        """
        GetDllLibDoc().MarginsF_get_Bottom.argtypes=[c_void_p]
        GetDllLibDoc().MarginsF_get_Bottom.restype=c_float
        ret = CallCFunction(GetDllLibDoc().MarginsF_get_Bottom,self.Ptr)
        return ret

    @Bottom.setter
    def Bottom(self, value:float):
        """
        Sets the bottom margin.

        Args:
            value (float): The value to set for the bottom margin.
        """
        GetDllLibDoc().MarginsF_set_Bottom.argtypes=[c_void_p, c_float]
        CallCFunction(GetDllLibDoc().MarginsF_set_Bottom,self.Ptr, value)


    def Clone(self)->'MarginsF':
        """
        Creates a new instance of the MarginsF class that is a copy of the current instance.

        Returns:
            MarginsF: A new instance that is a copy of this instance.
        """
        GetDllLibDoc().MarginsF_Clone.argtypes=[c_void_p]
        GetDllLibDoc().MarginsF_Clone.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().MarginsF_Clone,self.Ptr)
        ret = None if intPtr==None else MarginsF(intPtr)
        return ret


