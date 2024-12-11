from enum import Enum
from plum import dispatch
from typing import TypeVar, Union, Generic, List, Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class Endnote(SpireObject):
    """
    Represents an endnote.
    """
    @property
    def Separator(self) -> 'Body':
        """
        Gets or sets the separator for the endnote.
        """
        GetDllLibDoc().Endnote_get_Separator.argtypes=[c_void_p]
        GetDllLibDoc().Endnote_get_Separator.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().Endnote_get_Separator,self.Ptr)
        ret = None if intPtr==None else Body(intPtr)
        return ret


    @Separator.setter
    def Separator(self, value:'Body'):
        """
        Sets the separator for the endnote.
        """
        GetDllLibDoc().Endnote_set_Separator.argtypes=[c_void_p, c_void_p]
        CallCFunction(GetDllLibDoc().Endnote_set_Separator,self.Ptr, value.Ptr)

    @property

    def ContinuationSeparator(self)->'Body':
        """
        Gets or sets the continuation separator for the endnote.
        """
        GetDllLibDoc().Endnote_get_ContinuationSeparator.argtypes=[c_void_p]
        GetDllLibDoc().Endnote_get_ContinuationSeparator.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().Endnote_get_ContinuationSeparator,self.Ptr)
        ret = None if intPtr==None else Body(intPtr)
        return ret


    @ContinuationSeparator.setter
    def ContinuationSeparator(self, value:'Body'):
        """
        Sets the continuation separator for the endnote.
        """
        GetDllLibDoc().Endnote_set_ContinuationSeparator.argtypes=[c_void_p, c_void_p]
        CallCFunction(GetDllLibDoc().Endnote_set_ContinuationSeparator,self.Ptr, value.Ptr)

    @property

    def ContinuationNotice(self)->'Body':
        """
        Gets or sets the continuation notice for the endnote.
        """
        GetDllLibDoc().Endnote_get_ContinuationNotice.argtypes=[c_void_p]
        GetDllLibDoc().Endnote_get_ContinuationNotice.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().Endnote_get_ContinuationNotice,self.Ptr)
        ret = None if intPtr==None else Body(intPtr)
        return ret


    @ContinuationNotice.setter
    def ContinuationNotice(self, value:'Body'):
        """
        Sets the continuation notice for the endnote.
        """
        GetDllLibDoc().Endnote_set_ContinuationNotice.argtypes=[c_void_p, c_void_p]
        CallCFunction(GetDllLibDoc().Endnote_set_ContinuationNotice,self.Ptr, value.Ptr)


    def Clone(self)->'Endnote':
        """
        Creates a deep copy of the endnote.
        """
        GetDllLibDoc().Endnote_Clone.argtypes=[c_void_p]
        GetDllLibDoc().Endnote_Clone.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().Endnote_Clone,self.Ptr)
        ret = None if intPtr==None else Endnote(intPtr)
        return ret
