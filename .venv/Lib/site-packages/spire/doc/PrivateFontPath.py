from enum import Enum
from plum import dispatch
from typing import TypeVar, Union, Generic, List, Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class PrivateFontPath (SpireObject) :
    """
    Represents a private font path.
    """
    @dispatch
    def __init__(self, fontName:str, fontPath:str):
        fontNamePtr = StrToPtr(fontName)
        fontPathPtr = StrToPtr(fontPath)
        GetDllLibDoc().PrivateFontPath_CreatePrivateFontPathFF.argtypes=[c_char_p,c_char_p]
        GetDllLibDoc().PrivateFontPath_CreatePrivateFontPathFF.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().PrivateFontPath_CreatePrivateFontPathFF,fontNamePtr,fontPathPtr)
        super(PrivateFontPath, self).__init__(intPtr)
    @dispatch
    def __init__(self, fontName:str, fontPath:str,useArabicConcatenationRules:bool):

        fontNamePtr = StrToPtr(fontName)
        fontPathPtr = StrToPtr(fontPath)
        GetDllLibDoc().PrivateFontPath_CreatePrivateFontPathFFU.argtypes=[c_char_p,c_char_p,c_bool]
        GetDllLibDoc().PrivateFontPath_CreatePrivateFontPathFFU.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().PrivateFontPath_CreatePrivateFontPathFFU,fontNamePtr,fontPathPtr,useArabicConcatenationRules)
        super(PrivateFontPath, self).__init__(intPtr)
    @dispatch
    def __init__(self, fontName:str, fontStyle:FontStyle, fontPath:str):

        fontNamePtr = StrToPtr(fontName)
        fontPathPtr = StrToPtr(fontPath)
        iTypetype:c_int = fontStyle.value;

        GetDllLibDoc().PrivateFontPath_CreatePrivateFontPathFFF.argtypes=[c_char_p,c_int,c_char_p]
        GetDllLibDoc().PrivateFontPath_CreatePrivateFontPathFFF.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().PrivateFontPath_CreatePrivateFontPathFFF,fontNamePtr,iTypetype,fontPathPtr)
        super(PrivateFontPath, self).__init__(intPtr)
    @dispatch
    def __init__(self, fontName:str, fontStyle:FontStyle, fontPath:str,useArabicConcatenationRules:bool):

        fontNamePtr = StrToPtr(fontName)
        fontPathPtr = StrToPtr(fontPath)
        iTypetype:c_int = fontStyle.value;

        GetDllLibDoc().PrivateFontPath_CreatePrivateFontPathFFFU.argtypes=[c_char_p,c_int,c_char_p,c_bool]
        GetDllLibDoc().PrivateFontPath_CreatePrivateFontPathFFFU.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().PrivateFontPath_CreatePrivateFontPathFFFU,fontNamePtr,iTypetype,fontPathPtr,useArabicConcatenationRules)
        super(PrivateFontPath, self).__init__(intPtr)
    @property

    def FontPath(self)->str:
        """
        Gets or sets the path of the font.

        Returns:
            str: The path of the font.
        """
        GetDllLibDoc().PrivateFontPath_get_FontPath.argtypes=[c_void_p]
        GetDllLibDoc().PrivateFontPath_get_FontPath.restype=c_void_p
        ret = PtrToStr(CallCFunction(GetDllLibDoc().PrivateFontPath_get_FontPath,self.Ptr))
        return ret


    @FontPath.setter
    def FontPath(self, value:str):
        """
        Sets the path of the font.

        Args:
            value (str): The path of the font.
        """
        valuePtr = StrToPtr(value)
        GetDllLibDoc().PrivateFontPath_set_FontPath.argtypes=[c_void_p, c_char_p]
        CallCFunction(GetDllLibDoc().PrivateFontPath_set_FontPath,self.Ptr, valuePtr)

    @property

    def FontName(self)->str:
        """
        Gets or sets the name of the font.

        Returns:
            str: The name of the font.
        """
        GetDllLibDoc().PrivateFontPath_get_FontName.argtypes=[c_void_p]
        GetDllLibDoc().PrivateFontPath_get_FontName.restype=c_void_p
        ret = PtrToStr(CallCFunction(GetDllLibDoc().PrivateFontPath_get_FontName,self.Ptr))
        return ret


    @FontName.setter
    def FontName(self, value:str):
        """
        Sets the name of the font.

        Args:
            value (str): The name of the font.
        """
        valuePtr = StrToPtr(value)
        GetDllLibDoc().PrivateFontPath_set_FontName.argtypes=[c_void_p, c_char_p]
        CallCFunction(GetDllLibDoc().PrivateFontPath_set_FontName,self.Ptr, valuePtr)

#    @property
#
#    def FontStyle(self)->'FontStyle':
#        """
#    <summary>
#        Gets of sets the style of the font.
#    </summary>
#        """
#        GetDllLibDoc().PrivateFontPath_get_FontStyle.argtypes=[c_void_p]
#        GetDllLibDoc().PrivateFontPath_get_FontStyle.restype=c_int
#        ret = GetDllLibDoc().PrivateFontPath_get_FontStyle(self.Ptr)
#        objwraped = FontStyle(ret)
#        return objwraped


#    @FontStyle.setter
#    def FontStyle(self, value:'FontStyle'):
#        GetDllLibDoc().PrivateFontPath_set_FontStyle.argtypes=[c_void_p, c_int]
#        GetDllLibDoc().PrivateFontPath_set_FontStyle(self.Ptr, value.value)


    @property
    def UseArabicConcatenationRules(self)->bool:
        """
        Gets or sets a value indicating whether to use arabic concatenation rules.

        Returns:
            bool: True if arabic concatenation rules are used, False otherwise.
        """
        GetDllLibDoc().PrivateFontPath_get_UseArabicConcatenationRules.argtypes=[c_void_p]
        GetDllLibDoc().PrivateFontPath_get_UseArabicConcatenationRules.restype=c_bool
        ret = CallCFunction(GetDllLibDoc().PrivateFontPath_get_UseArabicConcatenationRules,self.Ptr)
        return ret

    @UseArabicConcatenationRules.setter
    def UseArabicConcatenationRules(self, value:bool):
        """
        Sets a value indicating whether to use arabic concatenation rules.

        Args:
            value (bool): True to use arabic concatenation rules, False otherwise.
        """
        GetDllLibDoc().PrivateFontPath_set_UseArabicConcatenationRules.argtypes=[c_void_p, c_bool]
        CallCFunction(GetDllLibDoc().PrivateFontPath_set_UseArabicConcatenationRules,self.Ptr, value)

