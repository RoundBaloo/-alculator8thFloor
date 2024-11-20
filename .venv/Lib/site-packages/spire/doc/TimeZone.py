from enum import Enum
from plum import dispatch
from typing import TypeVar, Union, Generic, List, Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class TimeZone (SpireObject) :
    """
    Represents a time zone.
    """
    @staticmethod

    def get_CurrentTimeZone()->'TimeZone':
        """
        Gets the current time zone.
        Returns:
            TimeZone: The current time zone.
        """
        #GetDllLibDoc().TimeZone_get_CurrentTimeZone.argtypes=[]
        GetDllLibDoc().TimeZone_get_CurrentTimeZone.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().TimeZone_get_CurrentTimeZone,)
        ret = None if intPtr==None else TimeZone(intPtr)
        return ret



    def ToUniversalTime(self ,time:'DateTime')->'DateTime':
        """
        Converts a specified time to Coordinated Universal Time (UTC).
        Args:
            time (DateTime): The time to convert.
        Returns:
            DateTime: The converted time in UTC.
        """
        intPtrtime:c_void_p = time.Ptr

        GetDllLibDoc().TimeZone_ToUniversalTime.argtypes=[c_void_p ,c_void_p]
        GetDllLibDoc().TimeZone_ToUniversalTime.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().TimeZone_ToUniversalTime,self.Ptr, intPtrtime)
        ret = None if intPtr==None else DateTime(intPtr)
        return ret



    def ToLocalTime(self ,time:'DateTime')->'DateTime':
        """
        Converts a specified time to the local time of the time zone.
        Args:
            time (DateTime): The time to convert.
        Returns:
            DateTime: The converted local time.
        """
        intPtrtime:c_void_p = time.Ptr

        GetDllLibDoc().TimeZone_ToLocalTime.argtypes=[c_void_p ,c_void_p]
        GetDllLibDoc().TimeZone_ToLocalTime.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().TimeZone_ToLocalTime,self.Ptr, intPtrtime)
        ret = None if intPtr==None else DateTime(intPtr)
        return ret


    @dispatch

    def IsDaylightSavingTime(self ,time:DateTime)->bool:
        """
        Determines whether a specified time is daylight saving time.
        Args:
            time (DateTime): The time to check.
        Returns:
            bool: True if the specified time is daylight saving time, False otherwise.
        """
        intPtrtime:c_void_p = time.Ptr

        GetDllLibDoc().TimeZone_IsDaylightSavingTime.argtypes=[c_void_p ,c_void_p]
        GetDllLibDoc().TimeZone_IsDaylightSavingTime.restype=c_bool
        ret = CallCFunction(GetDllLibDoc().TimeZone_IsDaylightSavingTime,self.Ptr, intPtrtime)
        return ret

#    @staticmethod
#    @dispatch
#
#    def IsDaylightSavingTime(time:DateTime,daylightTimes:'DaylightTime')->bool:
#        """
#
#        """
#        intPtrtime:c_void_p = time.Ptr
#        intPtrdaylightTimes:c_void_p = daylightTimes.Ptr
#
#        GetDllLibDoc().TimeZone_IsDaylightSavingTimeTD.argtypes=[ c_void_p,c_void_p]
#        GetDllLibDoc().TimeZone_IsDaylightSavingTimeTD.restype=c_bool
#        ret = GetDllLibDoc().TimeZone_IsDaylightSavingTimeTD( intPtrtime,intPtrdaylightTimes)
#        return ret


    @property

    def StandardName(self)->str:
        """
        Gets the standard name of the time zone.
        Returns:
            str: The standard name of the time zone.
        """
        GetDllLibDoc().TimeZone_get_StandardName.argtypes=[c_void_p]
        GetDllLibDoc().TimeZone_get_StandardName.restype=c_void_p
        ret = PtrToStr(CallCFunction(GetDllLibDoc().TimeZone_get_StandardName,self.Ptr))
        return ret


    @property

    def DaylightName(self)->str:
        """
        Gets the daylight name of the time zone.
        Returns:
            str: The daylight name of the time zone.
        """
        GetDllLibDoc().TimeZone_get_DaylightName.argtypes=[c_void_p]
        GetDllLibDoc().TimeZone_get_DaylightName.restype=c_void_p
        ret = PtrToStr(CallCFunction(GetDllLibDoc().TimeZone_get_DaylightName,self.Ptr))
        return ret



    def GetUtcOffset(self ,time:'DateTime')->'TimeSpan':
        """
        Gets the UTC offset for a specified time.
        Args:
            time (DateTime): The time to get the UTC offset for.
        Returns:
            TimeSpan: The UTC offset for the specified time.
        """
        intPtrtime:c_void_p = time.Ptr

        GetDllLibDoc().TimeZone_GetUtcOffset.argtypes=[c_void_p ,c_void_p]
        GetDllLibDoc().TimeZone_GetUtcOffset.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().TimeZone_GetUtcOffset,self.Ptr, intPtrtime)
        ret = None if intPtr==None else TimeSpan(intPtr)
        return ret


#
#    def GetDaylightChanges(self ,year:int)->'DaylightTime':
#        """
#
#        """
#        
#        GetDllLibDoc().TimeZone_GetDaylightChanges.argtypes=[c_void_p ,c_int]
#        GetDllLibDoc().TimeZone_GetDaylightChanges.restype=c_void_p
#        intPtr = GetDllLibDoc().TimeZone_GetDaylightChanges(self.Ptr, year)
#        ret = None if intPtr==None else DaylightTime(intPtr)
#        return ret
#


