from enum import Enum
from plum import dispatch
from typing import TypeVar, Union, Generic, List, Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class TextBodySelection (SpireObject) :
    """
    Represents a selection within a text body.
    """
    @dispatch
    def __init__(self,itemStart:ParagraphBase, itemEnd:ParagraphBase):
        """
        Initializes a new instance of the TextBodySelection class with the specified start and end paragraphs.

        Args:
            itemStart (ParagraphBase): The start paragraph of the selection.
            itemEnd (ParagraphBase): The end paragraph of the selection.
        """
        intPitemStart:c_void_p = itemStart.Ptr
        intPitemEnd:c_void_p = itemEnd.Ptr

        GetDllLibDoc().TextBodySelection_CreateTextBodySelectionII.argtypes = [c_void_p,c_void_p]
        GetDllLibDoc().TextBodySelection_CreateTextBodySelectionII.restype = c_void_p
        intPtr = CallCFunction(GetDllLibDoc().TextBodySelection_CreateTextBodySelectionII,intPitemStart,intPitemEnd)
        super(TextBodySelection, self).__init__(intPtr)

    @dispatch
    def __init__(self,textBody:IBody, itemStartIndex:int, itemEndIndex:int, pItemStartIndex:int, pItemEndIndex:int):
        """
        Initializes a new instance of the TextBodySelection class with the specified text body and indices.

        Args:
            textBody (IBody): The text body containing the selection.
            itemStartIndex (int): The index of the start paragraph in the text body.
            itemEndIndex (int): The index of the end paragraph in the text body.
            pItemStartIndex (int): The index of the start paragraph item in the start paragraph.
            pItemEndIndex (int): The index of the end paragraph item in the end paragraph.
        """
         #//int* intPtextBody = textBody->GetIntPtr()
        intPtextBody:c_void_p = textBody.Ptr

        GetDllLibDoc().TextBodySelection_CreateTextBodySelectionTIIPP.argtypes = [c_void_p,c_int,c_int,c_int,c_int]
        GetDllLibDoc().TextBodySelection_CreateTextBodySelectionTIIPP.restype = c_void_p
        intPtr = CallCFunction(GetDllLibDoc().TextBodySelection_CreateTextBodySelectionTIIPP,intPtextBody,itemStartIndex,itemEndIndex,pItemStartIndex,pItemEndIndex)
        super(TextBodySelection, self).__init__(intPtr)

    @property

    def TextBody(self)->'Body':
        """
        Gets the text body containing the selection.

        Returns:
            Body: The text body containing the selection.
        """
        GetDllLibDoc().TextBodySelection_get_TextBody.argtypes=[c_void_p]
        GetDllLibDoc().TextBodySelection_get_TextBody.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().TextBodySelection_get_TextBody,self.Ptr)
        ret = None if intPtr==None else Body(intPtr)
        return ret


    @property
    def ItemStartIndex(self)->int:
        """
        Gets the index of the start paragraph in the text body.

        Returns:
            int: The index of the start paragraph in the text body.
        """
        GetDllLibDoc().TextBodySelection_get_ItemStartIndex.argtypes=[c_void_p]
        GetDllLibDoc().TextBodySelection_get_ItemStartIndex.restype=c_int
        ret = CallCFunction(GetDllLibDoc().TextBodySelection_get_ItemStartIndex,self.Ptr)
        return ret

    @ItemStartIndex.setter
    def ItemStartIndex(self, value:int):
        """
        Sets the index of the start paragraph in the text body.

        Args:
            value (int): The index of the start paragraph in the text body.
        """
        GetDllLibDoc().TextBodySelection_set_ItemStartIndex.argtypes=[c_void_p, c_int]
        CallCFunction(GetDllLibDoc().TextBodySelection_set_ItemStartIndex,self.Ptr, value)

    @property
    def ItemEndIndex(self)->int:
        """
        Gets the index of the end paragraph in the text body.

        Returns:
            int: The index of the end paragraph in the text body.
        """
        GetDllLibDoc().TextBodySelection_get_ItemEndIndex.argtypes=[c_void_p]
        GetDllLibDoc().TextBodySelection_get_ItemEndIndex.restype=c_int
        ret = CallCFunction(GetDllLibDoc().TextBodySelection_get_ItemEndIndex,self.Ptr)
        return ret

    @ItemEndIndex.setter
    def ItemEndIndex(self, value:int):
        """
        Sets the index of the end paragraph in the text body.

        Args:
            value (int): The index of the end paragraph in the text body.
        """
        GetDllLibDoc().TextBodySelection_set_ItemEndIndex.argtypes=[c_void_p, c_int]
        CallCFunction(GetDllLibDoc().TextBodySelection_set_ItemEndIndex,self.Ptr, value)

    @property
    def ParagraphItemStartIndex(self)->int:
        """
        Gets the index of the start paragraph item in the start paragraph.

        Returns:
            int: The index of the start paragraph item in the start paragraph.
        """
        GetDllLibDoc().TextBodySelection_get_ParagraphItemStartIndex.argtypes=[c_void_p]
        GetDllLibDoc().TextBodySelection_get_ParagraphItemStartIndex.restype=c_int
        ret = CallCFunction(GetDllLibDoc().TextBodySelection_get_ParagraphItemStartIndex,self.Ptr)
        return ret

    @ParagraphItemStartIndex.setter
    def ParagraphItemStartIndex(self, value:int):
        """
        Sets the index of the start paragraph item in the start paragraph.

        Args:
            value (int): The index of the start paragraph item in the start paragraph.
        """
        GetDllLibDoc().TextBodySelection_set_ParagraphItemStartIndex.argtypes=[c_void_p, c_int]
        CallCFunction(GetDllLibDoc().TextBodySelection_set_ParagraphItemStartIndex,self.Ptr, value)

    @property
    def ParagraphItemEndIndex(self)->int:
        """
        Gets the index of the end paragraph item in the end paragraph.

        Returns:
            int: The index of the end paragraph item in the end paragraph.
        """
        GetDllLibDoc().TextBodySelection_get_ParagraphItemEndIndex.argtypes=[c_void_p]
        GetDllLibDoc().TextBodySelection_get_ParagraphItemEndIndex.restype=c_int
        ret = CallCFunction(GetDllLibDoc().TextBodySelection_get_ParagraphItemEndIndex,self.Ptr)
        return ret

    @ParagraphItemEndIndex.setter
    def ParagraphItemEndIndex(self, value:int):
        """
        Sets the index of the end paragraph item in the end paragraph.

        Args:
            value (int): The index of the end paragraph item in the end paragraph.
        """
        GetDllLibDoc().TextBodySelection_set_ParagraphItemEndIndex.argtypes=[c_void_p, c_int]
        CallCFunction(GetDllLibDoc().TextBodySelection_set_ParagraphItemEndIndex,self.Ptr, value)

