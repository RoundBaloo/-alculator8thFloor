from enum import Enum
from plum import dispatch
from typing import TypeVar, Union, Generic, List, Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class FootEndnoteOptions (  WordAttrCollection) :
    """
    Represents the options for footnotes and endnotes.
    """

    @property
    def NumberFormat(self) -> 'FootnoteNumberFormat':
        """
        Gets or sets the numbering format for footnotes and endnotes.
        """
        GetDllLibDoc().FootEndnoteOptions_get_NumberFormat.argtypes=[c_void_p]
        GetDllLibDoc().FootEndnoteOptions_get_NumberFormat.restype=c_int
        ret = CallCFunction(GetDllLibDoc().FootEndnoteOptions_get_NumberFormat,self.Ptr)
        objwraped = FootnoteNumberFormat(ret)
        return objwraped

    @NumberFormat.setter
    def NumberFormat(self, value:'FootnoteNumberFormat'):
        """
        Sets the numbering format for footnotes and endnotes.
        """
        GetDllLibDoc().FootEndnoteOptions_set_NumberFormat.argtypes=[c_void_p, c_int]
        CallCFunction(GetDllLibDoc().FootEndnoteOptions_set_NumberFormat,self.Ptr, value.value)

    @property

    def Position(self)->'FootnotePosition':
        """
        Gets or sets the position of footnotes and endnotes in the document.
        """
        GetDllLibDoc().FootEndnoteOptions_get_Position.argtypes=[c_void_p]
        GetDllLibDoc().FootEndnoteOptions_get_Position.restype=c_int
        ret = CallCFunction(GetDllLibDoc().FootEndnoteOptions_get_Position,self.Ptr)
        objwraped = FootnotePosition(ret)
        return objwraped

    @Position.setter
    def Position(self, value:'FootnotePosition'):
        """
        Sets the position of footnotes and endnotes in the document.
        """
        GetDllLibDoc().FootEndnoteOptions_set_Position.argtypes=[c_void_p, c_int]
        CallCFunction(GetDllLibDoc().FootEndnoteOptions_set_Position,self.Ptr, value.value)

    @property

    def RestartRule(self)->'FootnoteRestartRule':
        """
        Gets or sets the restart rule for footnotes and endnotes.
        """
        GetDllLibDoc().FootEndnoteOptions_get_RestartRule.argtypes=[c_void_p]
        GetDllLibDoc().FootEndnoteOptions_get_RestartRule.restype=c_int
        ret = CallCFunction(GetDllLibDoc().FootEndnoteOptions_get_RestartRule,self.Ptr)
        objwraped = FootnoteRestartRule(ret)
        return objwraped

    @RestartRule.setter
    def RestartRule(self, value:'FootnoteRestartRule'):
        """
        Sets the restart rule for footnotes and endnotes.
        """
        GetDllLibDoc().FootEndnoteOptions_set_RestartRule.argtypes=[c_void_p, c_int]
        CallCFunction(GetDllLibDoc().FootEndnoteOptions_set_RestartRule,self.Ptr, value.value)

    @property
    def StartNumber(self)->int:
        """
        Gets or sets the start number for footnotes and endnotes.
        """
        GetDllLibDoc().FootEndnoteOptions_get_StartNumber.argtypes=[c_void_p]
        GetDllLibDoc().FootEndnoteOptions_get_StartNumber.restype=c_int
        ret = CallCFunction(GetDllLibDoc().FootEndnoteOptions_get_StartNumber,self.Ptr)
        return ret

    @StartNumber.setter
    def StartNumber(self, value:int):
        """
        Sets the start number for footnotes and endnotes.
        """
        GetDllLibDoc().FootEndnoteOptions_set_StartNumber.argtypes=[c_void_p, c_int]
        CallCFunction(GetDllLibDoc().FootEndnoteOptions_set_StartNumber,self.Ptr, value)

