from enum import Enum
from plum import dispatch
from typing import TypeVar, Union, Generic, List, Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class TablePositioning (  AttrCollection) :
    """
    Table Positioning
    """
    @property

    def HorizPositionAbs(self)->'HorizontalPosition':
        """
        Gets or sets the absolute horizontal position for table.
        """
        GetDllLibDoc().TablePositioning_get_HorizPositionAbs.argtypes=[c_void_p]
        GetDllLibDoc().TablePositioning_get_HorizPositionAbs.restype=c_int
        ret = CallCFunction(GetDllLibDoc().TablePositioning_get_HorizPositionAbs,self.Ptr)
        objwraped = HorizontalPosition(ret)
        return objwraped

    @HorizPositionAbs.setter
    def HorizPositionAbs(self, value:'HorizontalPosition'):
        GetDllLibDoc().TablePositioning_set_HorizPositionAbs.argtypes=[c_void_p, c_int]
        CallCFunction(GetDllLibDoc().TablePositioning_set_HorizPositionAbs,self.Ptr, value.value)

    @property

    def VertPositionAbs(self)->'VerticalPosition':
        """
        Gets or sets the absolute vertical position for table.
        """
        GetDllLibDoc().TablePositioning_get_VertPositionAbs.argtypes=[c_void_p]
        GetDllLibDoc().TablePositioning_get_VertPositionAbs.restype=c_int
        ret = CallCFunction(GetDllLibDoc().TablePositioning_get_VertPositionAbs,self.Ptr)
        objwraped = VerticalPosition(ret)
        return objwraped

    @VertPositionAbs.setter
    def VertPositionAbs(self, value:'VerticalPosition'):
        GetDllLibDoc().TablePositioning_set_VertPositionAbs.argtypes=[c_void_p, c_int]
        CallCFunction(GetDllLibDoc().TablePositioning_set_VertPositionAbs,self.Ptr, value.value)

    @property
    def HorizPosition(self)->float:
        """
        Gets or sets the horizontal position for table.
        """
        GetDllLibDoc().TablePositioning_get_HorizPosition.argtypes=[c_void_p]
        GetDllLibDoc().TablePositioning_get_HorizPosition.restype=c_float
        ret = CallCFunction(GetDllLibDoc().TablePositioning_get_HorizPosition,self.Ptr)
        return ret

    @HorizPosition.setter
    def HorizPosition(self, value:float):
        GetDllLibDoc().TablePositioning_set_HorizPosition.argtypes=[c_void_p, c_float]
        CallCFunction(GetDllLibDoc().TablePositioning_set_HorizPosition,self.Ptr, value)

    @property
    def VertPosition(self)->float:
        """
        Gets or sets the vertical position for table.
        """
        GetDllLibDoc().TablePositioning_get_VertPosition.argtypes=[c_void_p]
        GetDllLibDoc().TablePositioning_get_VertPosition.restype=c_float
        ret = CallCFunction(GetDllLibDoc().TablePositioning_get_VertPosition,self.Ptr)
        return ret

    @VertPosition.setter
    def VertPosition(self, value:float):
        GetDllLibDoc().TablePositioning_set_VertPosition.argtypes=[c_void_p, c_float]
        CallCFunction(GetDllLibDoc().TablePositioning_set_VertPosition,self.Ptr, value)

    @property

    def HorizRelationTo(self)->'HorizontalRelation':
        """
        Gets or sets the horizontal relation of the table.
        """
        GetDllLibDoc().TablePositioning_get_HorizRelationTo.argtypes=[c_void_p]
        GetDllLibDoc().TablePositioning_get_HorizRelationTo.restype=c_int
        ret = CallCFunction(GetDllLibDoc().TablePositioning_get_HorizRelationTo,self.Ptr)
        objwraped = HorizontalRelation(ret)
        return objwraped

    @HorizRelationTo.setter
    def HorizRelationTo(self, value:'HorizontalRelation'):
        GetDllLibDoc().TablePositioning_set_HorizRelationTo.argtypes=[c_void_p, c_int]
        CallCFunction(GetDllLibDoc().TablePositioning_set_HorizRelationTo,self.Ptr, value.value)

    @property

    def VertRelationTo(self)->'VerticalRelation':
        """
        Gets or sets the horizontal relation of the table.
        """
        GetDllLibDoc().TablePositioning_get_VertRelationTo.argtypes=[c_void_p]
        GetDllLibDoc().TablePositioning_get_VertRelationTo.restype=c_int
        ret = CallCFunction(GetDllLibDoc().TablePositioning_get_VertRelationTo,self.Ptr)
        objwraped = VerticalRelation(ret)
        return objwraped

    @VertRelationTo.setter
    def VertRelationTo(self, value:'VerticalRelation'):
        GetDllLibDoc().TablePositioning_set_VertRelationTo.argtypes=[c_void_p, c_int]
        CallCFunction(GetDllLibDoc().TablePositioning_set_VertRelationTo,self.Ptr, value.value)

    @property
    def DistanceFromTop(self)->float:
        """
        Gets or sets the distance from top.
        """
        GetDllLibDoc().TablePositioning_get_DistanceFromTop.argtypes=[c_void_p]
        GetDllLibDoc().TablePositioning_get_DistanceFromTop.restype=c_float
        ret = CallCFunction(GetDllLibDoc().TablePositioning_get_DistanceFromTop,self.Ptr)
        return ret

    @DistanceFromTop.setter
    def DistanceFromTop(self, value:float):
        GetDllLibDoc().TablePositioning_set_DistanceFromTop.argtypes=[c_void_p, c_float]
        CallCFunction(GetDllLibDoc().TablePositioning_set_DistanceFromTop,self.Ptr, value)

    @property
    def DistanceFromBottom(self)->float:
        """
        Gets or sets the distance from bottom.
        """
        GetDllLibDoc().TablePositioning_get_DistanceFromBottom.argtypes=[c_void_p]
        GetDllLibDoc().TablePositioning_get_DistanceFromBottom.restype=c_float
        ret = CallCFunction(GetDllLibDoc().TablePositioning_get_DistanceFromBottom,self.Ptr)
        return ret

    @DistanceFromBottom.setter
    def DistanceFromBottom(self, value:float):
        GetDllLibDoc().TablePositioning_set_DistanceFromBottom.argtypes=[c_void_p, c_float]
        CallCFunction(GetDllLibDoc().TablePositioning_set_DistanceFromBottom,self.Ptr, value)

    @property
    def DistanceFromLeft(self)->float:
        """
        Gets or sets the distance from left.
        """
        GetDllLibDoc().TablePositioning_get_DistanceFromLeft.argtypes=[c_void_p]
        GetDllLibDoc().TablePositioning_get_DistanceFromLeft.restype=c_float
        ret = CallCFunction(GetDllLibDoc().TablePositioning_get_DistanceFromLeft,self.Ptr)
        return ret

    @DistanceFromLeft.setter
    def DistanceFromLeft(self, value:float):
        GetDllLibDoc().TablePositioning_set_DistanceFromLeft.argtypes=[c_void_p, c_float]
        CallCFunction(GetDllLibDoc().TablePositioning_set_DistanceFromLeft,self.Ptr, value)

    @property
    def DistanceFromRight(self)->float:
        """
        Gets or sets the distance from right.
        """
        GetDllLibDoc().TablePositioning_get_DistanceFromRight.argtypes=[c_void_p]
        GetDllLibDoc().TablePositioning_get_DistanceFromRight.restype=c_float
        ret = CallCFunction(GetDllLibDoc().TablePositioning_get_DistanceFromRight,self.Ptr)
        return ret

    @DistanceFromRight.setter
    def DistanceFromRight(self, value:float):
        GetDllLibDoc().TablePositioning_set_DistanceFromRight.argtypes=[c_void_p, c_float]
        CallCFunction(GetDllLibDoc().TablePositioning_set_DistanceFromRight,self.Ptr, value)

    def ClearFormatting(self):
        """
        Clears the table positioning.
        """
        GetDllLibDoc().TablePositioning_ClearFormatting.argtypes=[c_void_p]
        CallCFunction(GetDllLibDoc().TablePositioning_ClearFormatting,self.Ptr)

    @dispatch

    def Equals(self ,obj:SpireObject)->bool:
        """
        Equals method.
        """
        intPtrobj:c_void_p = obj.Ptr

        GetDllLibDoc().TablePositioning_Equals.argtypes=[c_void_p ,c_void_p]
        GetDllLibDoc().TablePositioning_Equals.restype=c_bool
        ret = CallCFunction(GetDllLibDoc().TablePositioning_Equals,self.Ptr, intPtrobj)
        return ret

    @dispatch

    def Equals(self ,other:'TablePositioning')->bool:
        """
        Equals method.
        """
        intPtrother:c_void_p = other.Ptr

        GetDllLibDoc().TablePositioning_EqualsO.argtypes=[c_void_p ,c_void_p]
        GetDllLibDoc().TablePositioning_EqualsO.restype=c_bool
        ret = CallCFunction(GetDllLibDoc().TablePositioning_EqualsO,self.Ptr, intPtrother)
        return ret

