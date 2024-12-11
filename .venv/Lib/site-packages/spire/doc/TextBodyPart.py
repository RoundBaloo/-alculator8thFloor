from enum import Enum
from plum import dispatch
from typing import TypeVar, Union, Generic, List, Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class TextBodyPart (SpireObject) :
    """
    Represents a text body part.
    """
    @dispatch
    def __init__(self, textBodySelection:TextBodySelection):
        """
        Initializes a new instance of the TextBodyPart class with a TextBodySelection object.
        """
        intPtextBodySelection:c_void_p = textBodySelection.Ptr

        GetDllLibDoc().TextBodyPart_CreateTextBodyPartTextBody.argtypes = [c_void_p]
        GetDllLibDoc().TextBodyPart_CreateTextBodyPartTextBody.restype = c_void_p
        intPtr = CallCFunction(GetDllLibDoc().TextBodyPart_CreateTextBodyPartTextBody,intPtextBodySelection)
        super(TextBodyPart, self).__init__(intPtr)

    @dispatch
    def __init__(self, textSelection:TextSelection):
        """
        Initializes a new instance of the TextBodyPart class with a TextSelection object.
        """
        intPtextSelection:c_void_p = textSelection.Ptr

        GetDllLibDoc().TextBodyPart_CreateTextBodyPartT.argtypes = [c_void_p]
        GetDllLibDoc().TextBodyPart_CreateTextBodyPartT.restype = c_void_p
        intPtr = CallCFunction(GetDllLibDoc().TextBodyPart_CreateTextBodyPartT,intPtextSelection)
        super(TextBodyPart, self).__init__(intPtr)
    @dispatch
    def __init__(self, doc:'Document'):
        """
        Initializes a new instance of the TextBodyPart class with a Document object.
        """
        intPdoc:c_void_p = doc.Ptr

        GetDllLibDoc().TextBodyPart_CreateTextBodyPartD.argtypes=[c_void_p]
        GetDllLibDoc().TextBodyPart_CreateTextBodyPartD.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().TextBodyPart_CreateTextBodyPartD,intPdoc)
        super(TextBodyPart, self).__init__(intPtr)

    @property

    def BodyItems(self)->'BodyRegionCollection':
        """
        Gets the body items of the text body part.
        """
        GetDllLibDoc().TextBodyPart_get_BodyItems.argtypes=[c_void_p]
        GetDllLibDoc().TextBodyPart_get_BodyItems.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().TextBodyPart_get_BodyItems,self.Ptr)
        ret = None if intPtr==None else BodyRegionCollection(intPtr)
        return ret


    def Clear(self):
        """
        Clears the text body part.
        """
        GetDllLibDoc().TextBodyPart_Clear.argtypes=[c_void_p]
        CallCFunction(GetDllLibDoc().TextBodyPart_Clear,self.Ptr)

    @dispatch

    def Copy(self ,textSel:TextSelection):
        """
        Copies the specified text selection to the text body part.
        """
        intPtrtextSel:c_void_p = textSel.Ptr

        GetDllLibDoc().TextBodyPart_Copy.argtypes=[c_void_p ,c_void_p]
        CallCFunction(GetDllLibDoc().TextBodyPart_Copy,self.Ptr, intPtrtextSel)

    @dispatch

    def Copy(self ,textSel:TextBodySelection):
        """
        Copies the specified text body selection to the text body part.
        """
        intPtrtextSel:c_void_p = textSel.Ptr

        GetDllLibDoc().TextBodyPart_CopyT.argtypes=[c_void_p ,c_void_p]
        CallCFunction(GetDllLibDoc().TextBodyPart_CopyT,self.Ptr, intPtrtextSel)

    @dispatch

    def Copy(self ,bodyItem:BodyRegion,clone:bool):
        """
        Copies the specified body region to the text body part.
        """
        intPtrbodyItem:c_void_p = bodyItem.Ptr

        GetDllLibDoc().TextBodyPart_CopyBC.argtypes=[c_void_p ,c_void_p,c_bool]
        CallCFunction(GetDllLibDoc().TextBodyPart_CopyBC,self.Ptr, intPtrbodyItem,clone)

    @dispatch

    def Copy(self ,pItem:ParagraphBase,clone:bool):
        """
        Copies the specified paragraph item to the text body part.
        """
        intPtrpItem:c_void_p = pItem.Ptr

        GetDllLibDoc().TextBodyPart_CopyPC.argtypes=[c_void_p ,c_void_p,c_bool]
        CallCFunction(GetDllLibDoc().TextBodyPart_CopyPC,self.Ptr, intPtrpItem,clone)

    @dispatch

    def PasteAfter(self ,bodyItem:BodyRegion):
        """
        Pastes the text body part after the specified body region.
        """
        intPtrbodyItem:c_void_p = bodyItem.Ptr

        GetDllLibDoc().TextBodyPart_PasteAfter.argtypes=[c_void_p ,c_void_p]
        CallCFunction(GetDllLibDoc().TextBodyPart_PasteAfter,self.Ptr, intPtrbodyItem)

    @dispatch

    def PasteAfter(self ,paragraphItem:ParagraphBase):
        """
        Pastes the text body part after the specified paragraph item.
        """
        intPtrparagraphItem:c_void_p = paragraphItem.Ptr

        GetDllLibDoc().TextBodyPart_PasteAfterP.argtypes=[c_void_p ,c_void_p]
        CallCFunction(GetDllLibDoc().TextBodyPart_PasteAfterP,self.Ptr, intPtrparagraphItem)

    @dispatch

    def PasteAt(self ,textBody:IBody,itemIndex:int):
        """
        Pastes the text body part at the specified index in the text body.
        """
        intPtrtextBody:c_void_p = textBody.Ptr

        GetDllLibDoc().TextBodyPart_PasteAt.argtypes=[c_void_p ,c_void_p,c_int]
        CallCFunction(GetDllLibDoc().TextBodyPart_PasteAt,self.Ptr, intPtrtextBody,itemIndex)

    @dispatch

    def PasteAt(self ,textBody:IBody,itemIndex:int,pItemIndex:int):
        """
        Pastes the text body part at the specified index in the text body and paragraph item.
        """
        intPtrtextBody:c_void_p = textBody.Ptr

        GetDllLibDoc().TextBodyPart_PasteAtTIP.argtypes=[c_void_p ,c_void_p,c_int,c_int]
        CallCFunction(GetDllLibDoc().TextBodyPart_PasteAtTIP,self.Ptr, intPtrtextBody,itemIndex,pItemIndex)


    def PasteAtEnd(self ,textBody:'IBody'):
        """
        Pastes the text body part at the end of the specified text body.
        """
        intPtrtextBody:c_void_p = textBody.Ptr

        GetDllLibDoc().TextBodyPart_PasteAtEnd.argtypes=[c_void_p ,c_void_p]
        CallCFunction(GetDllLibDoc().TextBodyPart_PasteAtEnd,self.Ptr, intPtrtextBody)

