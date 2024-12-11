from enum import Enum
from plum import dispatch
from typing import TypeVar, Union, Generic, List, Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class Template (SpireObject) :
    """
    Class represents Attached template of the document.
    """
    @property

    def Path(self)->str:
        """
        Gets or sets the path of the attached template.

        Returns:
            str: The path to attached template document.
        """
        GetDllLibDoc().Template_get_Path.argtypes=[c_void_p]
        GetDllLibDoc().Template_get_Path.restype=c_void_p
        ret = PtrToStr(CallCFunction(GetDllLibDoc().Template_get_Path,self.Ptr))
        return ret


    @Path.setter
    def Path(self, value:str):
        """
        Sets the path of the attached template.

        Args:
            value (str): The path to set.

        Returns:
            None
        """
        valuePtr = StrToPtr(value)
        GetDllLibDoc().Template_set_Path.argtypes=[c_void_p, c_char_p]
        CallCFunction(GetDllLibDoc().Template_set_Path,self.Ptr, valuePtr)

