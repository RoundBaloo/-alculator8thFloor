from enum import Enum
from plum import dispatch
from typing import TypeVar, Union, Generic, List, Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class SdtText (  SdtControlProperties) :
    """
    Represents a structured document tag for text.
    """
    @dispatch
    def __init__(self, isRichText:bool):
        """
        Initializes a new instance of the SdtText class.

        Args:
            isRichText: A boolean value indicating whether the text is rich text.
        """
        GetDllLibDoc().SdtText_CreateSdtTextI.argtypes=[c_bool]
        GetDllLibDoc().SdtText_CreateSdtTextI.restype = c_void_p
        intPtr = CallCFunction(GetDllLibDoc().SdtText_CreateSdtTextI,isRichText)
        super(SdtText, self).__init__(intPtr)

    @property
    def IsMultiline(self)->bool:
        """
        Gets or sets a value indicating whether soft line breaks can be added to the contents of this structured document tag when this document is modified.

        Returns:
            A boolean value indicating whether soft line breaks are allowed.
        """
        GetDllLibDoc().SdtText_get_IsMultiline.argtypes=[c_void_p]
        GetDllLibDoc().SdtText_get_IsMultiline.restype=c_bool
        ret = CallCFunction(GetDllLibDoc().SdtText_get_IsMultiline,self.Ptr)
        return ret

    @IsMultiline.setter
    def IsMultiline(self, value:bool):
        """
        Sets a value indicating whether soft line breaks can be added to the contents of this structured document tag when this document is modified.

        Args:
            value: A boolean value indicating whether soft line breaks are allowed.
        """
        GetDllLibDoc().SdtText_set_IsMultiline.argtypes=[c_void_p, c_bool]
        CallCFunction(GetDllLibDoc().SdtText_set_IsMultiline,self.Ptr, value)

