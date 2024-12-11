from enum import Enum
from plum import dispatch
from typing import TypeVar, Union, Generic, List, Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class FormField (  Field) :
    """
    Represents a form field.
    """
    @property

    def FormFieldType(self)->'FormFieldType':
        """
        Gets the type of this form field.
        """
        GetDllLibDoc().FormField_get_FormFieldType.argtypes=[c_void_p]
        GetDllLibDoc().FormField_get_FormFieldType.restype=c_int
        ret = CallCFunction(GetDllLibDoc().FormField_get_FormFieldType,self.Ptr)
        objwraped = FormFieldType(ret)
        return objwraped

    @property

    def Name(self)->str:
        """
        Gets or sets the form field title name (bookmark name).
        The name is unique in the document.
        """
        GetDllLibDoc().FormField_get_Name.argtypes=[c_void_p]
        GetDllLibDoc().FormField_get_Name.restype=c_void_p
        ret = PtrToStr(CallCFunction(GetDllLibDoc().FormField_get_Name,self.Ptr))
        return ret


    @Name.setter
    def Name(self, value:str):
        """
        Sets the form field title name (bookmark name).
        The name is unique in the document.
        """
        valuePtr = StrToPtr(value)
        GetDllLibDoc().FormField_set_Name.argtypes=[c_void_p, c_char_p]
        CallCFunction(GetDllLibDoc().FormField_set_Name,self.Ptr, valuePtr)

    @property

    def Help(self)->str:
        """
        Gets or sets the form field help.
        """
        GetDllLibDoc().FormField_get_Help.argtypes=[c_void_p]
        GetDllLibDoc().FormField_get_Help.restype=c_void_p
        ret = PtrToStr(CallCFunction(GetDllLibDoc().FormField_get_Help,self.Ptr))
        return ret


    @Help.setter
    def Help(self, value:str):
        """
        Sets the form field help.
        """
        valuePtr = StrToPtr(value)
        GetDllLibDoc().FormField_set_Help.argtypes=[c_void_p, c_char_p]
        CallCFunction(GetDllLibDoc().FormField_set_Help,self.Ptr, valuePtr)

    @property

    def StatusBarHelp(self)->str:
        """
        Gets or sets the status bar help.
        """
        GetDllLibDoc().FormField_get_StatusBarHelp.argtypes=[c_void_p]
        GetDllLibDoc().FormField_get_StatusBarHelp.restype=c_void_p
        ret = PtrToStr(CallCFunction(GetDllLibDoc().FormField_get_StatusBarHelp,self.Ptr))
        return ret


    @StatusBarHelp.setter
    def StatusBarHelp(self, value:str):
        """
        Sets the status bar help.
        """
        valuePtr = StrToPtr(value)
        GetDllLibDoc().FormField_set_StatusBarHelp.argtypes=[c_void_p, c_char_p]
        CallCFunction(GetDllLibDoc().FormField_set_StatusBarHelp,self.Ptr, valuePtr)

    @property

    def MacroOnStart(self)->str:
        """
        Returns or sets the name of macros on start.
        """
        GetDllLibDoc().FormField_get_MacroOnStart.argtypes=[c_void_p]
        GetDllLibDoc().FormField_get_MacroOnStart.restype=c_void_p
        ret = PtrToStr(CallCFunction(GetDllLibDoc().FormField_get_MacroOnStart,self.Ptr))
        return ret


    @MacroOnStart.setter
    def MacroOnStart(self, value:str):
        """
        Sets the name of macros on start.
        """
        valuePtr = StrToPtr(value)
        GetDllLibDoc().FormField_set_MacroOnStart.argtypes=[c_void_p, c_char_p]
        CallCFunction(GetDllLibDoc().FormField_set_MacroOnStart,self.Ptr, valuePtr)

    @property

    def MacroOnEnd(self)->str:
        """
        Returns or sets the name of macros on end.
        """
        GetDllLibDoc().FormField_get_MacroOnEnd.argtypes=[c_void_p]
        GetDllLibDoc().FormField_get_MacroOnEnd.restype=c_void_p
        ret = PtrToStr(CallCFunction(GetDllLibDoc().FormField_get_MacroOnEnd,self.Ptr))
        return ret


    @MacroOnEnd.setter
    def MacroOnEnd(self, value:str):
        """
        Sets the name of macros on end.
        """
        valuePtr = StrToPtr(value)
        GetDllLibDoc().FormField_set_MacroOnEnd.argtypes=[c_void_p, c_char_p]
        CallCFunction(GetDllLibDoc().FormField_set_MacroOnEnd,self.Ptr, valuePtr)

    @property
    def Enabled(self)->bool:
        """
        Gets or sets the Enabled property (true if form field enabled).
        """
        GetDllLibDoc().FormField_get_Enabled.argtypes=[c_void_p]
        GetDllLibDoc().FormField_get_Enabled.restype=c_bool
        ret = CallCFunction(GetDllLibDoc().FormField_get_Enabled,self.Ptr)
        return ret

    @Enabled.setter
    def Enabled(self, value:bool):
        """
        Sets the Enabled property (true if form field enabled).
        """
        GetDllLibDoc().FormField_set_Enabled.argtypes=[c_void_p, c_bool]
        CallCFunction(GetDllLibDoc().FormField_set_Enabled,self.Ptr, value)

    @property
    def CalculateOnExit(self)->bool:
        """
        Gets or sets the calculate on exit property.
        """
        GetDllLibDoc().FormField_get_CalculateOnExit.argtypes=[c_void_p]
        GetDllLibDoc().FormField_get_CalculateOnExit.restype=c_bool
        ret = CallCFunction(GetDllLibDoc().FormField_get_CalculateOnExit,self.Ptr)
        return ret

    @CalculateOnExit.setter
    def CalculateOnExit(self, value:bool):
        """
        Sets the calculate on exit property.
        """
        GetDllLibDoc().FormField_set_CalculateOnExit.argtypes=[c_void_p, c_bool]
        CallCFunction(GetDllLibDoc().FormField_set_CalculateOnExit,self.Ptr, value)

