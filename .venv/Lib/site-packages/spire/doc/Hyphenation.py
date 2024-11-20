from enum import Enum
from plum import dispatch
from typing import TypeVar, Union, Generic, List, Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class Hyphenation (SpireObject) :
    """
    Class represents Hyphenation settings of the document.
    """
    @property
    def AutoHyphenation(self)->bool:
        """
        Get the value of AutoHyphenation property.
        """
        GetDllLibDoc().Hyphenation_get_AutoHyphenation.argtypes=[c_void_p]
        GetDllLibDoc().Hyphenation_get_AutoHyphenation.restype=c_bool
        ret = CallCFunction(GetDllLibDoc().Hyphenation_get_AutoHyphenation,self.Ptr)
        return ret

    @AutoHyphenation.setter
    def AutoHyphenation(self, value:bool):
        """
        Set the value of AutoHyphenation property.
        """
        GetDllLibDoc().Hyphenation_set_AutoHyphenation.argtypes=[c_void_p, c_bool]
        CallCFunction(GetDllLibDoc().Hyphenation_set_AutoHyphenation,self.Ptr, value)

    @property
    def HyphenateCaps(self)->bool:
        """
        Get the value of HyphenateCaps property.
        """
        GetDllLibDoc().Hyphenation_get_HyphenateCaps.argtypes=[c_void_p]
        GetDllLibDoc().Hyphenation_get_HyphenateCaps.restype=c_bool
        ret = CallCFunction(GetDllLibDoc().Hyphenation_get_HyphenateCaps,self.Ptr)
        return ret

    @HyphenateCaps.setter
    def HyphenateCaps(self, value:bool):
        """
        Set the value of HyphenateCaps property.
        """
        GetDllLibDoc().Hyphenation_set_HyphenateCaps.argtypes=[c_void_p, c_bool]
        CallCFunction(GetDllLibDoc().Hyphenation_set_HyphenateCaps,self.Ptr, value)

    @property
    def HyphenationZone(self)->float:
        """
        Get the value of HyphenationZone property.
        """
        GetDllLibDoc().Hyphenation_get_HyphenationZone.argtypes=[c_void_p]
        GetDllLibDoc().Hyphenation_get_HyphenationZone.restype=c_float
        ret = CallCFunction(GetDllLibDoc().Hyphenation_get_HyphenationZone,self.Ptr)
        return ret

    @HyphenationZone.setter
    def HyphenationZone(self, value:float):
        """
        Set the value of HyphenationZone property.
        """
        GetDllLibDoc().Hyphenation_set_HyphenationZone.argtypes=[c_void_p, c_float]
        CallCFunction(GetDllLibDoc().Hyphenation_set_HyphenationZone,self.Ptr, value)

    @property
    def ConsecutiveHyphensLimit(self)->int:
        """
        Get the value of ConsecutiveHyphensLimit property.
        """
        GetDllLibDoc().Hyphenation_get_ConsecutiveHyphensLimit.argtypes=[c_void_p]
        GetDllLibDoc().Hyphenation_get_ConsecutiveHyphensLimit.restype=c_int
        ret = CallCFunction(GetDllLibDoc().Hyphenation_get_ConsecutiveHyphensLimit,self.Ptr)
        return ret

    @ConsecutiveHyphensLimit.setter
    def ConsecutiveHyphensLimit(self, value:int):
        """
        Set the value of ConsecutiveHyphensLimit property.
        """
        GetDllLibDoc().Hyphenation_set_ConsecutiveHyphensLimit.argtypes=[c_void_p, c_int]
        CallCFunction(GetDllLibDoc().Hyphenation_set_ConsecutiveHyphensLimit,self.Ptr, value)

