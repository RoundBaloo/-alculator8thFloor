from enum import Enum
from plum import dispatch
from typing import TypeVar, Union, Generic, List, Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class DocumentProperties(SpireObject):
    """
    Class DocumentProperties of the document.
    """
    @property
    def FormFieldShading(self) -> bool:
        """
        Specifies whether to apply shading on form fields.
        """
        GetDllLibDoc().DocumentProperties_get_FormFieldShading.argtypes=[c_void_p]
        GetDllLibDoc().DocumentProperties_get_FormFieldShading.restype=c_bool
        ret = CallCFunction(GetDllLibDoc().DocumentProperties_get_FormFieldShading,self.Ptr)
        return ret

    @FormFieldShading.setter
    def FormFieldShading(self, value:bool):
        """
        Sets whether to apply shading on form fields.
        """
        GetDllLibDoc().DocumentProperties_set_FormFieldShading.argtypes=[c_void_p, c_bool]
        CallCFunction(GetDllLibDoc().DocumentProperties_set_FormFieldShading,self.Ptr, value)

    @property
    def Version(self) -> 'DocumentVersion':
        """
        Gets the document version.
        Returns:
            The DocumentVersion
        """
        GetDllLibDoc().DocumentProperties_get_Version.argtypes=[c_void_p]
        GetDllLibDoc().DocumentProperties_get_Version.restype=c_int
        ret = CallCFunction(GetDllLibDoc().DocumentProperties_get_Version,self.Ptr)
        objwraped = DocumentVersion(ret)
        return objwraped

