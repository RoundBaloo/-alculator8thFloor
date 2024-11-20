from enum import Enum
from plum import dispatch
from typing import TypeVar, Union, Generic, List, Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class Style (  DocumentSerializable, IStyle) :
    """
    Represents a style in a document.
    """
    @property

    def CharacterFormat(self)->'CharacterFormat':
        """
        Gets the character format of the style.
        """
        GetDllLibDoc().Style_get_CharacterFormat.argtypes=[c_void_p]
        GetDllLibDoc().Style_get_CharacterFormat.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().Style_get_CharacterFormat,self.Ptr)
        ret = None if intPtr==None else CharacterFormat(intPtr)
        return ret


    @property

    def Name(self)->str:
        """
        Gets or sets the name of the style.
        """
        GetDllLibDoc().Style_get_Name.argtypes=[c_void_p]
        GetDllLibDoc().Style_get_Name.restype=c_void_p
        ret = PtrToStr(CallCFunction(GetDllLibDoc().Style_get_Name,self.Ptr))
        return ret


    @Name.setter
    def Name(self, value:str):
        valuePtr = StrToPtr(value)
        GetDllLibDoc().Style_set_Name.argtypes=[c_void_p, c_char_p]
        CallCFunction(GetDllLibDoc().Style_set_Name,self.Ptr, valuePtr)

    @property

    def StyleId(self)->str:
        """
        Gets or sets the style id.
        """
        GetDllLibDoc().Style_get_StyleId.argtypes=[c_void_p]
        GetDllLibDoc().Style_get_StyleId.restype=c_void_p
        ret = PtrToStr(CallCFunction(GetDllLibDoc().Style_get_StyleId,self.Ptr))
        return ret

    @property

    def GetStyleType(self)->'StyleType':
        """
        Gets the style type.
        """
        GetDllLibDoc().Style_get_StyleType.argtypes=[c_void_p]
        GetDllLibDoc().Style_get_StyleType.restype=c_int
        ret = CallCFunction(GetDllLibDoc().Style_get_StyleType,self.Ptr)
        objwraped = StyleType(ret)
        return objwraped

    #@property

    #def DefaultStyleType(self)->'BuiltinStyle':
    #    """

    #    """
    #    GetDllLibDoc().Style_get_DefaultStyleType.argtypes=[c_void_p]
    #    GetDllLibDoc().Style_get_DefaultStyleType.restype=c_int
    #    ret = GetDllLibDoc().Style_get_DefaultStyleType(self.Ptr)
    #    objwraped = BuiltinStyle(ret)
    #    return objwraped

    @property
    def IsCustomStyle(self)->bool:
        """
        Gets or sets a value indicating whether this instance is a custom style.
        """
        GetDllLibDoc().Style_get_IsCustomStyle.argtypes=[c_void_p]
        GetDllLibDoc().Style_get_IsCustomStyle.restype=c_bool
        ret = CallCFunction(GetDllLibDoc().Style_get_IsCustomStyle,self.Ptr)
        return ret

    @IsCustomStyle.setter
    def IsCustomStyle(self, value:bool):
        GetDllLibDoc().Style_set_IsCustomStyle.argtypes=[c_void_p, c_bool]
        CallCFunction(GetDllLibDoc().Style_set_IsCustomStyle,self.Ptr, value)

    @property
    def IsHeading(self)->bool:
        """
        Gets a value indicating whether this style is a heading style.
        """
        GetDllLibDoc().Style_get_IsHeading.argtypes=[c_void_p]
        GetDllLibDoc().Style_get_IsHeading.restype=c_bool
        ret = CallCFunction(GetDllLibDoc().Style_get_IsHeading,self.Ptr)
        return ret

    @dispatch

    def ApplyBaseStyle(self ,styleName:str):
        """
        Applies a base style to this style.
        """
        styleNamePtr = StrToPtr(styleName)
        
        GetDllLibDoc().Style_ApplyBaseStyle.argtypes=[c_void_p ,c_char_p]
        CallCFunction(GetDllLibDoc().Style_ApplyBaseStyle,self.Ptr, styleNamePtr)

    @dispatch

    def ApplyBaseStyle(self ,bStyle:BuiltinStyle):
        """
        Applies a base style to this style.
        """
        enumbStyle:c_int = bStyle.value

        GetDllLibDoc().Style_ApplyBaseStyleB.argtypes=[c_void_p ,c_int]
        CallCFunction(GetDllLibDoc().Style_ApplyBaseStyleB,self.Ptr, enumbStyle)


    def Clone(self)->'IStyle':
        """
        Creates a deep copy of this style.
        """
        GetDllLibDoc().Style_Clone.argtypes=[c_void_p]
        GetDllLibDoc().Style_Clone.restype=IntPtrWithTypeName
        intPtr = CallCFunction(GetDllLibDoc().Style_Clone,self.Ptr)
        ret = None if intPtr==None else Style._create(intPtr)
        return ret


    @staticmethod
    @dispatch

    def CreateBuiltinStyle(bStyle:BuiltinStyle,doc:Document)->'Style':
        """
        Creates a new built-in style in the specified document.
        """
        enumbStyle:c_int = bStyle.value
        intPtrdoc:c_void_p = doc.Ptr

        GetDllLibDoc().Style_CreateBuiltinStyle.argtypes=[ c_int,c_void_p]
        GetDllLibDoc().Style_CreateBuiltinStyle.restype=IntPtrWithTypeName
        intPtr = CallCFunction(GetDllLibDoc().Style_CreateBuiltinStyle, enumbStyle,intPtrdoc)
        ret = None if intPtr==None else Style._create(intPtr)
        return ret


    @staticmethod
    @dispatch

    def CreateBuiltinStyle(bStyle:BuiltinStyle,type:StyleType,doc:Document)->IStyle:
        """
        Creates a new built-in style of the specified type in the specified document.
        """
        enumbStyle:c_int = bStyle.value
        enumtype:c_int = type.value
        intPtrdoc:c_void_p = doc.Ptr

        GetDllLibDoc().Style_CreateBuiltinStyleBTD.argtypes=[ c_int,c_int,c_void_p]
        GetDllLibDoc().Style_CreateBuiltinStyleBTD.restype=IntPtrWithTypeName
        intPtr = CallCFunction(GetDllLibDoc().Style_CreateBuiltinStyleBTD, enumbStyle,enumtype,intPtrdoc)
        ret = None if intPtr==None else Style._create(intPtr)
        return ret

    @staticmethod
    def _create(intPtrWithTypeName:IntPtrWithTypeName)->'Style':
        ret= None
        if intPtrWithTypeName == None:
            return ret
        intPtr = intPtrWithTypeName.intPtr[0] + (intPtrWithTypeName.intPtr[1]<<32)
        strName = PtrToStr(intPtrWithTypeName.typeName)

        if (strName == "Spire.Doc.Documents.ListStyle"):
            from spire.doc import ListStyle
            ret = ListStyle(intPtr)
        elif (strName == "Spire.Doc.Documents.ParagraphStyle"):
            from spire.doc import ParagraphStyle
            ret = ParagraphStyle(intPtr)
        else:
            ret = Style(intPtr)
			
        return ret

    @staticmethod

    def NameToBuiltIn(styleName:str)->'BuiltinStyle':
        """
        Converts a style name to a built-in style.
        """
        styleNamePtr = StrToPtr(styleName)
        GetDllLibDoc().Style_NameToBuiltIn.argtypes=[c_char_p]
        GetDllLibDoc().Style_NameToBuiltIn.restype=c_int
        ret = CallCFunction(GetDllLibDoc().Style_NameToBuiltIn,styleNamePtr)
        objwraped = BuiltinStyle(ret)
        return objwraped

