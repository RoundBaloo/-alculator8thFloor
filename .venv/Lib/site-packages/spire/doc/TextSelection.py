from enum import Enum
from plum import dispatch
from typing import TypeVar, Union, Generic, List, Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

#class TextSelection (  IEnumerable[TextRange]):
class TextSelection (  SpireObject):
    """
    Represents a text selection.
    """
    @property

    def SelectedText(self)->str:
        """
        Gets the selected text.
        """
        GetDllLibDoc().TextSelection_get_SelectedText.argtypes=[c_void_p]
        GetDllLibDoc().TextSelection_get_SelectedText.restype=c_void_p
        ret = PtrToStr(CallCFunction(GetDllLibDoc().TextSelection_get_SelectedText,self.Ptr))
        return ret



    def get_Item(self ,index:int)->str:
        """
        Gets the text at the specified index.
        """
        
        GetDllLibDoc().TextSelection_get_Item.argtypes=[c_void_p ,c_int]
        GetDllLibDoc().TextSelection_get_Item.restype=c_void_p
        ret = PtrToStr(CallCFunction(GetDllLibDoc().TextSelection_get_Item,self.Ptr, index))
        return ret



    def set_Item(self ,index:int,value:str):
        """
        Sets the text at the specified index.
        """
        valuePtr = StrToPtr(value)
        GetDllLibDoc().TextSelection_set_Item.argtypes=[c_void_p ,c_int,c_char_p]
        CallCFunction(GetDllLibDoc().TextSelection_set_Item,self.Ptr, index,valuePtr)

    @property
    def Count(self)->int:
        """
        Gets the number of text items in the selection.
        """
        GetDllLibDoc().TextSelection_get_Count.argtypes=[c_void_p]
        GetDllLibDoc().TextSelection_get_Count.restype=c_int
        ret = CallCFunction(GetDllLibDoc().TextSelection_get_Count,self.Ptr)
        return ret


    def GetRanges(self)->List['TextRange']:
        """
        Gets the ranges in one paragraph.
        @return List[TextRange]
        """
        GetDllLibDoc().TextSelection_GetRanges.argtypes=[c_void_p]
        GetDllLibDoc().TextSelection_GetRanges.restype=IntPtrArray
        intPtrArray = CallCFunction(GetDllLibDoc().TextSelection_GetRanges,self.Ptr)
        ret = GetObjVectorFromArray(intPtrArray, TextRange)
        return ret


    @dispatch

    def GetAsRange(self)->List[TextRange]:
        """

             Gets as range. more than one paragraph,every paragraph to one text range.
            
             @return List[TextRange]
        
        """
        GetDllLibDoc().TextSelection_GetAsRange.argtypes=[c_void_p]
        GetDllLibDoc().TextSelection_GetAsRange.restype=IntPtrArray
        intPtrArray = CallCFunction(GetDllLibDoc().TextSelection_GetAsRange,self.Ptr)
        ret = GetObjVectorFromArray(intPtrArray, TextRange)
        return ret


    @dispatch

    def GetAsRange(self ,isCopyFormat:bool)->List[TextRange]:
        """

            Gets as range. more than one paragraph,every paragraph to one text range.
            @param isCopyFormat Is copy existing formats to textrange
            @return List[TextRange]
        
        """
        
        GetDllLibDoc().TextSelection_GetAsRangeI.argtypes=[c_void_p ,c_bool]
        GetDllLibDoc().TextSelection_GetAsRangeI.restype=IntPtrArray
        intPtrArray =CallCFunction(GetDllLibDoc().TextSelection_GetAsRangeI,self.Ptr, isCopyFormat)
        ret = GetObjVectorFromArray(intPtrArray, TextRange)
        return ret


    @dispatch

    def GetAsOneRange(self)->TextRange:
        """
        Gets the selection as a single text range.
        """
        GetDllLibDoc().TextSelection_GetAsOneRange.argtypes=[c_void_p]
        GetDllLibDoc().TextSelection_GetAsOneRange.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().TextSelection_GetAsOneRange,self.Ptr)
        ret = None if intPtr==None else TextRange(intPtr)
        return ret


    @dispatch

    def GetAsOneRange(self ,IsCopyFormat:bool)->TextRange:
        """
        Gets the selection as a single text range.
        Args:
            IsCopyFormat(bool): Indicates whether to copy existing formats to the text range.
        """
        
        GetDllLibDoc().TextSelection_GetAsOneRangeI.argtypes=[c_void_p ,c_bool]
        GetDllLibDoc().TextSelection_GetAsOneRangeI.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().TextSelection_GetAsOneRangeI,self.Ptr, IsCopyFormat)
        ret = None if intPtr==None else TextRange(intPtr)
        return ret



    def GetEnumerator(self)->'IEnumerator':
        """
        Gets an enumerator for the text selection.
        """
        GetDllLibDoc().TextSelection_GetEnumerator.argtypes=[c_void_p]
        GetDllLibDoc().TextSelection_GetEnumerator.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().TextSelection_GetEnumerator,self.Ptr)
        ret = None if intPtr==None else IEnumerator(intPtr)
        return ret


