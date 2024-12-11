from enum import Enum
from plum import dispatch
from typing import TypeVar, Union, Generic, List, Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class SdtDate (  SdtControlProperties) :
    """
    Represents a date control.
    """
    @dispatch
    def __init__(self):
        """
        Initializes a new instance of the SdtDate class.
        """
        GetDllLibDoc().SdtDate_CreateSdtDate.restype = c_void_p
        intPtr = CallCFunction(GetDllLibDoc().SdtDate_CreateSdtDate,)
        super(SdtDate, self).__init__(intPtr)

    @property
    def Lid(self)->int:
        """
        Gets or sets the language ID of the date control.
        """
        GetDllLibDoc().SdtDate_get_Lid.argtypes=[c_void_p]
        GetDllLibDoc().SdtDate_get_Lid.restype=c_int
        ret = CallCFunction(GetDllLibDoc().SdtDate_get_Lid,self.Ptr)
        return ret

    @Lid.setter
    def Lid(self, value:int):
        """
        Sets the language ID of the date control.
        """
        GetDllLibDoc().SdtDate_set_Lid.argtypes=[c_void_p, c_int]
        CallCFunction(GetDllLibDoc().SdtDate_set_Lid,self.Ptr, value)

    @property

    def DateFormat(self)->str:
        """
        Gets or sets the date format of the date control.
        """
        GetDllLibDoc().SdtDate_get_DateFormat.argtypes=[c_void_p]
        GetDllLibDoc().SdtDate_get_DateFormat.restype=c_void_p
        ret = PtrToStr(CallCFunction(GetDllLibDoc().SdtDate_get_DateFormat,self.Ptr))
        return ret


    @DateFormat.setter
    def DateFormat(self, value:str):
        """
        Sets the date format of the date control.
        """
        valuePtr = StrToPtr(value)
        GetDllLibDoc().SdtDate_set_DateFormat.argtypes=[c_void_p, c_char_p]
        CallCFunction(GetDllLibDoc().SdtDate_set_DateFormat,self.Ptr, valuePtr)

    @property

    def CalendarType(self)->'CalendarType':
        """
        Gets or sets the calendar type of the date control.
        """
        GetDllLibDoc().SdtDate_get_CalendarType.argtypes=[c_void_p]
        GetDllLibDoc().SdtDate_get_CalendarType.restype=c_int
        ret = CallCFunction(GetDllLibDoc().SdtDate_get_CalendarType,self.Ptr)
        objwraped = CalendarType(ret)
        return objwraped

    @CalendarType.setter
    def CalendarType(self, value:'CalendarType'):
        """
        Sets the calendar type of the date control.
        """
        GetDllLibDoc().SdtDate_set_CalendarType.argtypes=[c_void_p, c_int]
        CallCFunction(GetDllLibDoc().SdtDate_set_CalendarType,self.Ptr, value.value)

    @property

    def FullDate(self)->'DateTime':
        """
        Gets or sets the full date of the date control.
        """
        GetDllLibDoc().SdtDate_get_FullDate.argtypes=[c_void_p]
        GetDllLibDoc().SdtDate_get_FullDate.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().SdtDate_get_FullDate,self.Ptr)
        ret = None if intPtr==None else DateTime(intPtr)
        return ret


    @FullDate.setter
    def FullDate(self, value:'DateTime'):
        """
        Sets the full date of the date control.
        """
        GetDllLibDoc().SdtDate_set_FullDate.argtypes=[c_void_p, c_void_p]
        CallCFunction(GetDllLibDoc().SdtDate_set_FullDate,self.Ptr, value.Ptr)

