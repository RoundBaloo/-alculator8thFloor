from enum import Enum
from plum import dispatch
from typing import TypeVar, Union, Generic, List, Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class BodyRegion(DocumentBase, IBodyRegion):
    """
    Represents a body region in a document.
    """

    @property
    def OwnerTextBody(self) -> 'Body':
        """
        Gets the owner text body.

        Returns:
            The owner text body.
        """
        GetDllLibDoc().BodyRegion_get_OwnerTextBody.argtypes=[c_void_p]
        GetDllLibDoc().BodyRegion_get_OwnerTextBody.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().BodyRegion_get_OwnerTextBody,self.Ptr)
        from spire.doc import Body
        ret = None if intPtr==None else Body(intPtr)
        return ret

    @property
    def IsInsertRevision(self) -> bool:
        """
        Gets a value indicating whether this item was inserted to the document.

        Returns:
            A boolean value indicating whether this item was inserted to the document.
        """
        GetDllLibDoc().BodyRegion_get_IsInsertRevision.argtypes=[c_void_p]
        GetDllLibDoc().BodyRegion_get_IsInsertRevision.restype=c_bool
        ret = CallCFunction(GetDllLibDoc().BodyRegion_get_IsInsertRevision,self.Ptr)
        return ret

    @property
    def InsertRevision(self) -> 'EditRevision':
        """
        Gets the insert revision for this object.
        Note that this can be null if it does not have an insert revision.

        Returns:
            The insert revision for this object.
        """
        GetDllLibDoc().BodyRegion_get_InsertRevision.argtypes=[c_void_p]
        GetDllLibDoc().BodyRegion_get_InsertRevision.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().BodyRegion_get_InsertRevision,self.Ptr)
        from spire.doc import EditRevision
        ret = None if intPtr==None else EditRevision(intPtr)
        return ret

    @property
    def IsDeleteRevision(self) -> bool:
        """
        Gets a value indicating whether this item was deleted from the document.

        Returns:
            A boolean value indicating whether this item was deleted from the document.
        """
        GetDllLibDoc().BodyRegion_get_IsDeleteRevision.argtypes=[c_void_p]
        GetDllLibDoc().BodyRegion_get_IsDeleteRevision.restype=c_bool
        ret = CallCFunction(GetDllLibDoc().BodyRegion_get_IsDeleteRevision,self.Ptr)
        return ret

    @property
    def DeleteRevision(self) -> 'EditRevision':
        """
        Gets the delete revision for this object.
        Note that this can be null if it does not have a delete revision.

        Returns:
            The delete revision for this object.
        """
        GetDllLibDoc().BodyRegion_get_DeleteRevision.argtypes=[c_void_p]
        GetDllLibDoc().BodyRegion_get_DeleteRevision.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().BodyRegion_get_DeleteRevision,self.Ptr)
        from spire.doc import EditRevision
        ret = None if intPtr==None else EditRevision(intPtr)
        return ret


#
#    def Find(self ,pattern:'Regex')->'TextSelection':
#        """
#
#        """
#        intPtrpattern:c_void_p = pattern.Ptr
#
#        GetDllLibDoc().BodyRegion_Find.argtypes=[c_void_p ,c_void_p]
#        GetDllLibDoc().BodyRegion_Find.restype=c_void_p
#        intPtr = GetDllLibDoc().BodyRegion_Find(self.Ptr, intPtrpattern)
#        ret = None if intPtr==None else TextSelection(intPtr)
#        return ret
#


#    @dispatch
#
#    def Replace(self ,pattern:'Regex',replace:str)->int:
#        """
#
#        """
#        intPtrpattern:c_void_p = pattern.Ptr
#        replacePtr = StrToPtr(replace)
#        GetDllLibDoc().BodyRegion_Replace.argtypes=[c_void_p ,c_void_p,c_char_p]
#        GetDllLibDoc().BodyRegion_Replace.restype=c_int
#        ret = GetDllLibDoc().BodyRegion_Replace(self.Ptr, intPtrpattern,replacePtr)
#        return ret


    @dispatch
    def Replace(self, given: str, replace: str, caseSensitive: bool, wholeWord: bool) -> int:
        """
        Replaces the given text with the specified replacement text in the body region.

        Args:
            given: The text to be replaced.
            replace: The replacement text.
            caseSensitive: A boolean value indicating whether the replacement should be case-sensitive.
            wholeWord: A boolean value indicating whether the replacement should be done only for whole words.

        Returns:
            The number of replacements made.
        """
        givenPtr = StrToPtr(given)
        replacePtr = StrToPtr(replace)
        GetDllLibDoc().BodyRegion_ReplaceGRCW.argtypes=[c_void_p ,c_char_p,c_char_p,c_bool,c_bool]
        GetDllLibDoc().BodyRegion_ReplaceGRCW.restype=c_int
        ret = CallCFunction(GetDllLibDoc().BodyRegion_ReplaceGRCW,self.Ptr, givenPtr,replacePtr,caseSensitive,wholeWord)
        return ret

#    @dispatch
#
#    def Replace(self ,pattern:'Regex',textSelection:TextSelection)->int:
#        """
#
#        """
#        intPtrpattern:c_void_p = pattern.Ptr
#        intPtrtextSelection:c_void_p = textSelection.Ptr
#
#        GetDllLibDoc().BodyRegion_ReplacePT.argtypes=[c_void_p ,c_void_p,c_void_p]
#        GetDllLibDoc().BodyRegion_ReplacePT.restype=c_int
#        ret = GetDllLibDoc().BodyRegion_ReplacePT(self.Ptr, intPtrpattern,intPtrtextSelection)
#        return ret


#    @dispatch
#
#    def Replace(self ,pattern:'Regex',textSelection:TextSelection,saveFormatting:bool)->int:
#        """
#
#        """
#        intPtrpattern:c_void_p = pattern.Ptr
#        intPtrtextSelection:c_void_p = textSelection.Ptr
#
#        GetDllLibDoc().BodyRegion_ReplacePTS.argtypes=[c_void_p ,c_void_p,c_void_p,c_bool]
#        GetDllLibDoc().BodyRegion_ReplacePTS.restype=c_int
#        ret = GetDllLibDoc().BodyRegion_ReplacePTS(self.Ptr, intPtrpattern,intPtrtextSelection,saveFormatting)
#        return ret


