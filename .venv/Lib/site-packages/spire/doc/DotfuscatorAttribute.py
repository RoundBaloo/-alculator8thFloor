from enum import Enum
from plum import dispatch
from typing import TypeVar, Union, Generic, List, Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class DotfuscatorAttribute(SpireObject):
    """
    This class represents a Dotfuscator attribute.
    """

    def a(self) -> str:
        """
        Returns the value of attribute 'a'.
        """
        GetDllLibDoc().DotfuscatorAttribute_a.argtypes=[c_void_p]
        GetDllLibDoc().DotfuscatorAttribute_a.restype=c_void_p
        ret = PtrToStr(CallCFunction(GetDllLibDoc().DotfuscatorAttribute_a,self.Ptr))
        return ret


    def c(self)->int:
        """
        Returns the value of attribute 'c'.
        """
        GetDllLibDoc().DotfuscatorAttribute_c.argtypes=[c_void_p]
        GetDllLibDoc().DotfuscatorAttribute_c.restype=c_int
        ret = CallCFunction(GetDllLibDoc().DotfuscatorAttribute_c,self.Ptr)
        return ret
