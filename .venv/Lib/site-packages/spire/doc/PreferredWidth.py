from enum import Enum
from plum import dispatch
from typing import TypeVar, Union, Generic, List, Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class PreferredWidth (SpireObject) :
    """
    An PreferredWidth class that specifies the preferred total width of the table
    of which this row is a part.
    """
    @dispatch
    def __init__(self,widthType:WidthType, value:int):
        """
        Initializes a new instance of the PreferredWidth class.

        Args:
            widthType: A WidthType enum element that specifies the units of measurement for the value.
            value: An integer value that specifies the preferred width.
        """
        iTypetype:c_int = widthType.value

        GetDllLibDoc().PreferredWidth_CreatePreferredWidthTV.argtypes=[c_int,c_int]
        GetDllLibDoc().PreferredWidth_CreatePreferredWidthTV.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().PreferredWidth_CreatePreferredWidthTV,iTypetype,value)
        super(PreferredWidth, self).__init__(intPtr)

    @property
    def Value(self)->float:
        """
        Gets the double value that specifies the preferred width.

        Returns:
            A float value that specifies the preferred width.
        """
        GetDllLibDoc().PreferredWidth_get_Value.argtypes=[c_void_p]
        GetDllLibDoc().PreferredWidth_get_Value.restype=c_float
        ret = CallCFunction(GetDllLibDoc().PreferredWidth_get_Value,self.Ptr)
        return ret

    @property

    def Type(self)->'WidthType':
        """
        Gets the enum element from WidthType that specifies the units of measurement for the value.

        Returns:
            A WidthType enum element that specifies the units of measurement for the value.
        """
        GetDllLibDoc().PreferredWidth_get_Type.argtypes=[c_void_p]
        GetDllLibDoc().PreferredWidth_get_Type.restype=c_int
        ret = CallCFunction(GetDllLibDoc().PreferredWidth_get_Type,self.Ptr)
        objwraped = WidthType(ret)
        return objwraped

    @staticmethod

    def get_Auto()->'PreferredWidth':
        """
        Gets an instance of PreferredWidth that indicates the preferred width is auto.

        Returns:
            An instance of PreferredWidth that indicates the preferred width is auto.
        """
        #GetDllLibDoc().PreferredWidth_get_Auto.argtypes=[]
        GetDllLibDoc().PreferredWidth_get_Auto.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().PreferredWidth_get_Auto,)
        ret = None if intPtr==None else PreferredWidth(intPtr)
        return ret


    @staticmethod

    def get_None()->'PreferredWidth':
        """
        Gets an instance of PreferredWidth that indicates the preferred width is not specified.

        Returns:
            An instance of PreferredWidth that indicates the preferred width is not specified.
        """
        #GetDllLibDoc().PreferredWidth_get_None.argtypes=[]
        GetDllLibDoc().PreferredWidth_get_None.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().PreferredWidth_get_None,)
        ret = None if intPtr==None else PreferredWidth(intPtr)
        return ret



    def Equals(self ,obj:'SpireObject')->bool:
        """
        Determines whether the specified object is equal to the current object.

        Args:
            obj: A SpireObject to compare with the current object.

        Returns:
            True if the specified object is equal to the current object; otherwise, False.
        """
        intPtrobj:c_void_p = obj.Ptr

        GetDllLibDoc().PreferredWidth_Equals.argtypes=[c_void_p ,c_void_p]
        GetDllLibDoc().PreferredWidth_Equals.restype=c_bool
        ret = CallCFunction(GetDllLibDoc().PreferredWidth_Equals,self.Ptr, intPtrobj)
        return ret

    def GetHashCode(self)->int:
        """
        Serves as the default hash function.

        Returns:
            An integer hash code for the current object.
        """
        GetDllLibDoc().PreferredWidth_GetHashCode.argtypes=[c_void_p]
        GetDllLibDoc().PreferredWidth_GetHashCode.restype=c_int
        ret = CallCFunction(GetDllLibDoc().PreferredWidth_GetHashCode,self.Ptr)
        return ret

